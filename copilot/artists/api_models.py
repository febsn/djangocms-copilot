# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict

from copilot.conf import settings
from copilot.api import CopilotClient
from copilot.events.api_models import EventManager

import logging
logger = logging.getLogger('djangocms-copilot')

class Artist(object):
    def __init__(self, id, **kwargs):
        super(Artist, self).__init__(**kwargs)
        self.client = CopilotClient(settings.COPILOT_USER)
        self.id = id
        self._get()
        self._assign_assets()
        self.events = EventManager(self.id)

    def _get(self):
        data = self.client.get('artists/{id}'.format(id=self.id)).json()
        props = ['assets', 'bookerSimple', 'stageName', 'web', 'shortBio', 'longBio',
            'facebook', 'myspace', 'mainact']
        for prop in props:
            try:
                setattr(self, prop, data[prop])
            except KeyError:
                logger.warning("Property {prop} is missing in copilot API "
                    "response for Artist {id}".format(prop=prop, id=self.id))

    def _assign_assets(self):
        self.media = defaultdict(list)
        for asset in self.assets:
            for asset_tag in asset['tags']:
                self.media[asset_tag['tagName']].append(asset)

    def news(self, page=1):
        return self.client.get_paginated('artists/{id}/newsEntries'.format(
            id=self.id), page=page).json()

    def videos(self, page=1):
        return self.client.get_paginated('artists/{id}/videoEntries'.format(
            id=self.id), page=page).json()

    def records(self, page=1):
        return self.client.get_paginated('artists/{id}/records'.format(
            id=self.id), page=page).json()

    def images(self):
        for asset in self.assets:
            if asset['mimeType'].startswith('image'):
                yield asset
            continue
