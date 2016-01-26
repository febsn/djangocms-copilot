# -*- coding: utf-8 -*-

from .base import BaseEntity

class Artist(BaseEntity):
    endpoint = 'artists/'

    def all(self):
        return self._client._get_paginated(self.endpoint)

    
