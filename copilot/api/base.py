# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
try:
    from urllib.parse import urljoin, urlencode
except ImportError:
    from urlparse import urljoin
    from urllib import urlencode

from .exceptions import HttpError

class APIClientBase(object):
    """
    Base class for REST API clients
    """

    def _handle_response(self, response):
        if not 200 <= response.status_code < 300:
            raise HttpError(response)
        return response

    def _post(self, url, data=None):
        """
        Handle authenticated POST requests
        """
        url = urljoin(self.base_url, url)
        r = requests.post(url, auth=self.auth, json=data)
        return self._handle_response(r)

    def _get(self, url, **kwargs):
        """
        Handle authenticated GET requests
        """
        url = urljoin(self.base_url, url)

        if len(kwargs):
            url += '?' + urlencode(kwargs)

        r = requests.get(url, auth=self.auth)
        return self._handle_response(r)

    def _delete(self, url):
        """
        Handle authenticated DELETE requests
        """
        url = urljoin(self.base_url, url)
        r = requests.delete(url, auth=self.auth)
        return self._handle_response(r)

    def _patch(self, url, data=None):
        """
        Handle authenticated PATH requests
        """
        url = urljoin(self.base_url, url)
        r = requests.patch(url, auth=self.auth, json=data)
        return self._handle_response(r)
