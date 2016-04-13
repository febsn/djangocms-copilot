# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.timezone import now

from ..base_views import CopilotListView
from .api_models import EventManager

class EventListView(CopilotListView):

    template_name = 'copilot/events/list.html'

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        manager = EventManager()
        data = manager.year()
        context['events'] = data['content']
        context['artists'] = data['artists']
        return context
