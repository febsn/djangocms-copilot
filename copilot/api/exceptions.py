# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class HttpError(Exception):
    def __init__(self, response, *args):
        self.response = response
        self.code = response.status_code
        self.message = "Http remote exception {code}: {reason} ({url})".format(
            code=response.status_code, reason=response.reason, url=response.url)
        super(HttpError, self).__init__(self.message, *args)

