# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, date

from copilot.conf import settings
from copilot.api import CopilotClient

import logging
logger = logging.getLogger('djangocms-copilot')


class BaseApiManager(object):
    def __init__(self, artist_id=None, **kwargs):
        super(BaseApiManager, self).__init__(**kwargs)
        self.client = CopilotClient(settings.COPILOT_USER)
        self.artist_id = artist_id

    def _get_endpoint(self, **kwargs):
        if self.artist_id:
            endpoint = self._get_endpoint_for_artist(**kwargs)
        else:
            endpoint = self._get_endpoint_for_all(**kwargs)
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
        items = self.client.get_paginated(endpoint, **kwargs).json()
        return items

    def all(self):
        """
        Return all items.
        """
        return self._get(self._get_endpoint())
