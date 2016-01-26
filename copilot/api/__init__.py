# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from urllib.parse import urljoin
except ImportError:
    # py2
    from urlparse import urljoin

from .base import APIClientBase
from ..conf import settings

class CopilotClient(APIClientBase):
    """
    Copilot public API client
    """

    def __init__(self, copilot_user, root_url="https://www.copilot-office.de/"):
        """
        Initialize the class with you user_id and secret_key
        """
        super(CopilotClient, self).__init__()
        self.base_url = urljoin(root_url, "{user}/{api_resource}/".format(
            user=copilot_user, api_resource='public/api'))
        self.auth = None

    def get_paginated(self, url, page=0, **kwargs):
        kwargs.setdefault('page.size', settings.COPILOT_PAGE_SIZE)
        kwargs['page.page'] = page
        return self.get(url, **kwargs)

    def get(self, url, **kwargs):
        response = self._get(url, **kwargs)
        response.encoding = 'UTF-8'
        return response
