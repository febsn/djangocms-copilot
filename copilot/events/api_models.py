# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict
from datetime import date

from copilot.conf import settings
from copilot.api import CopilotClient

import logging
logger = logging.getLogger('djangocms-copilot')


class EventManager(object):

    def __init__(self, artist_id=None, **kwargs):
        super(EventManager, self).__init__(**kwargs)
        self.client = CopilotClient(settings.COPILOT_USER)
        self.artist_id = artist_id
        self._init_years()

    def _init_years(self):
        class YearManager(dict):
            def __init__(self, mgr):
                self.mgr = mgr
            def __getitem__(self, key):
                logger.debug('Events called for year {}'.format(key))
                endpoint = self.mgr._get_endpoint(
                    start_date = date(key, 1, 1),
                    end_date = date(key, 12, 31)
                )
                return self.mgr._get(endpoint)

        self.years = YearManager(self)

    def _get_endpoint(self, **kwargs):
        if self.artist_id:
            endpoint = self._get_endpoint_for_artist(**kwargs)
        else:
            endpoint = self._get_endpoint_for_all(**kwargs)

        if kwargs['start_date']:
            endpoint += '/'+kwargs['start_date'].isoformat()
            if kwargs['end_date']:
                endpoint += '/'+kwargs['end_date'].isoformat()
        return endpoint

    def _get_endpoint_for_all(self, **kwargs):
        return 'events'

    def _get_endpoint_for_artist(self, **kwargs):
        return 'artists/{id}/events'.format(id=self.artist_id)

    def _get_sorting(self):
        return 'dateOfEvent,asc'

    def _get(self, endpoint):
        logger.debug('API call: {}'.format(endpoint))
        kwargs = {
            'page.sort': self._get_sorting(),
        }
        return self.client.get_paginated(endpoint, **kwargs).json()
