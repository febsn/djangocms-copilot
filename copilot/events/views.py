# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..base_views import CopilotView

class EventListView(CopilotView):

    template_name = 'copilot/events/list.html'

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        data = self.client.get('events/').json()
        context['events'] = data['content']
        return context
