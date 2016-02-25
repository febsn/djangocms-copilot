# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..base_views import CopilotListView
from django.utils.timezone import now

class EventListView(CopilotListView):

    template_name = 'copilot/events/list.html'

    def _upcoming(self, **kwargs):
        return self._get_paginated('events/from/{}/'.format(
            now().date().isoformat(), **kwargs)).json()

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        data = self._upcoming(**kwargs)
        context['events'] = data['content']
        return context
