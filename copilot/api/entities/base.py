# -*- coding: utf-8 -*-

from copilot.conf import settings

class BaseEntity(object):
    """
    Base API entity. 
    """
    def __init__(self, client):
        super(BaseEntity, self).__init__()
        self._client = client
