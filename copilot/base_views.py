# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.views.generic.base import TemplateView

from .api import CopilotClient

class CopilotView(TemplateView):
    """
    Base View for all Copilot client views.
    """
    def __init__(self, **kwargs):
        super(CopilotView, self).__init__(**kwargs)
        self.client = CopilotClient(settings.COPILOT_USER)

class CopilotListView(CopilotView):
    """
    Base View for all Copilot client list views.
    """

    def get_context_data(self, **kwargs):
        """
        Set the page for later use in _get_paginated
        """
        try:
            self.page = self.request.GET['page']
        except KeyError:
            self.page = 1
        return super(CopilotListView, self).get_context_data(**kwargs)

    def _get_paginated(self, url, **kwargs):
        """
        Get the requested page of the list from the API client
        """
        return self.client.get_paginated(url, self.page, **kwargs)
