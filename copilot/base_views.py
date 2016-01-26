# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.views.generic.base import TemplateView

from .api import CopilotClient

class CopilotView(TemplateView):
    def __init__(self, **kwargs):
        super(CopilotView, self).__init__(**kwargs)
        self.client = CopilotClient(settings.COPILOT_USER)
