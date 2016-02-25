# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

from .api_models import Artist
from copilot.base_views import CopilotView, CopilotListView
from copilot.api.exceptions import HttpError

import json

class ArtistListView(CopilotListView):

    template_name = 'copilot/artists/list.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)
        response = self._get_paginated('artists/')
        data = json.loads(response.text)
        context['artists'] = data['content']
        return context


class ArtistDetailView(CopilotView):

    template_name = 'copilot/artists/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        try:
            context['artist'] = Artist(kwargs['id'])
        except HttpError as e:
            if e.code == 404:
                raise Http404
            else:
                raise e
        return context
