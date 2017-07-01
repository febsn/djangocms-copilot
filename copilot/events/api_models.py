# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, date

from copilot.conf import settings
from copilot.api import CopilotClient

import logging
logger = logging.getLogger('djangocms-copilot')


class EventManager(object):
    ALL_ENDPOINT = 'events/'
    ARTIST_ENDPOINT = 'artists/{id}/events/'
    SORTING = 'dateOfEvent,asc'
    FROM = 'from/{}/'
    ARTIST_FROM = '{}/'
    TO = 'to/{}/'
    ARTIST_TO = '{}/'

    def __init__(self, artist_id=None, **kwargs):
        super(EventManager, self).__init__(**kwargs)
        self.client = CopilotClient(settings.COPILOT_USER)
        self.artist_id = artist_id

    def _get_from(self):
        if self.artist_id:
            return self.ARTIST_FROM
        else:
            return self.FROM

    def _get_to(self):
        if self.artist_id:
            return self.ARTIST_TO
        else:
            return self.TO

    def _get_endpoint(self, **kwargs):
        if self.artist_id:
            endpoint = self._get_endpoint_for_artist(**kwargs)
        else:
            endpoint = self._get_endpoint_for_all(**kwargs)

        try:
            start_date = kwargs['start_date']
            endpoint += self._get_from().format(start_date.isoformat())
            # the API allows only calls with start_date AND end_date, or neither of them.
            # If there is only start_date given, we assume a delta of one year.
            endpoint += self._get_to().format(
                kwargs.get('end_date', date(start_date.year+1, start_date.month, start_date.day)).isoformat()
            )
        except KeyError:
            # no problem if start_date and end_date not given
            pass
        return endpoint

    def _get_endpoint_for_all(self, **kwargs):
        return self.ALL_ENDPOINT

    def _get_endpoint_for_artist(self, **kwargs):
        return self.ARTIST_ENDPOINT.format(id=self.artist_id)

    def _get_sorting(self):
        return self.SORTING

    def _get(self, endpoint, **kwargs):
        logger.debug('API call: {}'.format(endpoint))
        kwargs.setdefault('page.sort', self._get_sorting())
        kwargs['external'] = False
        events = self.client.get_paginated(endpoint, **kwargs).json()
        events['artists'] = {}
        for event in events['content']:
            try:
                event['dateOfEvent'] = datetime.strptime(event['dateOfEvent']+event['start'], '%Y-%m-%d%H:%M:%S.%f')
            except KeyError:
                try:
                    event['dateOfEvent'] = datetime.strptime(event['dateOfEvent'], '%Y-%m-%d')
                except KeyError:
                    pass
            for cast_item in event['cast']:
                try:
                    events['artists'][cast_item['artist']['id']]['events'].append(event)
                except KeyError:
                    events['artists'][cast_item['artist']['id']] = {
                        'artist': cast_item['artist'],
                        'events': [event, ]
                    }
        return events


    def _get_years(self):
        endpoint = self._get_endpoint()
        events = self._get(endpoint)
        years = {}
        for event in events:
            try:
                years[event['dateOfEvent'].year].append(event)
            except KeyError:
                years[event['dateOfEvent'].year] = [event, ]
        return years


    def year(self, year=None):
        """
        Return events for year `year`.
        """
        if year is None:
            year = datetime.now().year
        endpoint = self._get_endpoint(
            start_date=date(year, 1, 1),
            end_date=date(year, 12, 31)
        )
        return self._get(endpoint)

    def prevnext(self, year=None):
        """
        Return events for year `year` and one year before and after.
        """
        if year is None:
            year = datetime.now().year
        endpoint = self._get_endpoint(
            start_date=date(year-1, 1, 1),
            end_date=date(year+1, 12, 31)
        )
        return self._get(endpoint)

    @property
    def years(self):
        try:
            return self._years
        except AttributeError:
            self._years = self._get_years()
            return self._years

    def all(self):
        """
        Return all events.
        """
        return self._get(self._get_endpoint())

    def upcoming(self, **kwargs):
        endpoint = self._get_endpoint(
            start_date=datetime.now().date())
        return self._get(endpoint, **kwargs)

    def __str__(self):
        if self.artist_id:
            return 'EventManager for {}'.format(self.artist_id)
        else:
            return 'EventManager'
