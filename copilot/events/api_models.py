# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict
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
            endpoint += self._get_from().format(kwargs['start_date'].isoformat())
            endpoint += self._get_to().format(kwargs['end_date'].isoformat())
        except KeyError:
            # no problem if start_date or end_date not given
            pass
        return endpoint

    def _get_endpoint_for_all(self, **kwargs):
        return self.ALL_ENDPOINT

    def _get_endpoint_for_artist(self, **kwargs):
        return self.ARTIST_ENDPOINT.format(id=self.artist_id)

    def _get_sorting(self):
        return self.SORTING

    def _get(self, endpoint):
        logger.debug('API call: {}'.format(endpoint))
        kwargs = {
            'page.sort': self._get_sorting(),
            'external': False,
        }
        events = self.client.get_paginated(endpoint, **kwargs).json()
        for event in events['content']:
            try:
                event['dateOfEvent'] = datetime.strptime(event['dateOfEvent']+event['start'], '%Y-%m-%d%H:%M:%S.%f')
            except KeyError:
                try:
                    event['dateOfEvent'] = datetime.strptime(event['dateOfEvent'], '%Y-%m-%d')
                except KeyError:
                    pass
        return events

    def _get_years(self):
        endpoint = self._get_endpoint()
        events = self._get(endpoint)
        years = defaultdict(list)
        for event in events:
            years[event['dateOfEvent'].year].append(event)
        return years

    @property
    def years(self):
        try:
            return self._years
        except AttributeError:
            self._years = self._get_years()
            return self._years

    def all(self):
        return self._get(self._get_endpoint())

    def upcoming(self):
        endpoint = self._get_endpoint(
            start_date=datetime.now().date())
        return self._get(endpoint)

    def __str__(self):
        if self.artist_id:
            return 'EventManager for {}'.format(self.artist_id)
        else:
            return 'EventManager'
