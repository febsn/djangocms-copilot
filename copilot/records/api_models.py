# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, date

from copilot.conf import settings
from copilot.api import CopilotClient

from copilot.base_api_models import BaseApiManager

import logging
logger = logging.getLogger('djangocms-copilot')


class RecordManager(BaseApiManager):
    ALL_ENDPOINT = 'records/'
    ARTIST_ENDPOINT = 'artists/{id}/records/'
    SORTING = 'releaseDate,desc'

    def _get(self, endpoint, **kwargs):
        items = super(RecordManager, self)._get(endpoint, **kwargs)
        for item in items['content']:
            item['releaseDate'] = datetime.strptime(item['releaseDate'], '%Y-%m-%d')
        return items

    def __str__(self):
        if self.artist_id:
            return 'RecordManager for {}'.format(self.artist_id)
        else:
            return 'RecordManager'
