# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.timezone import now

from ..base_views import CopilotView, CopilotListView
from .api_models import RecordManager

class RecordListView(CopilotListView):
    template_name = 'copilot/records/list.html'

    def get_context_data(self, **kwargs):
        context = super(RecordListView, self).get_context_data(**kwargs)
        manager = RecordManager()
        data = manager.all()
        context['records'] = data['content']
        return context

class RecordDetailView(CopilotView):
    template_name = 'copilot/records/detail.html'

    def get_context_data(self, id, **kwargs):
        context = super(RecordDetailView, self).get_context_data(**kwargs)
        context['record'] = self.client.get("records/{}".format(id)).json()
        return context
