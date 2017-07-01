# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .api import CopilotClient
from .artists.api_models import Artist
from .conf import settings
from .models import News, EventList

class NewsPlugin(CMSPluginBase):
    module = "Copilot"
    name = _("News plugin")
    model = News
    render_template = "copilot/plugins/news.html"
    endpoint = "news"
    cache = False

    def render(self, context, instance, placeholder):
        client = CopilotClient(settings.COPILOT_USER)
        context['news'] = client.get(self.endpoint).json()['content']
        return context
plugin_pool.register_plugin(NewsPlugin)


class EventListPlugin(CMSPluginBase):
    module = "Copilot"
    name =_("Events Plugin")
    model = EventList
    render_template = "copilot/plugins/event_list.html"

    def render(self, context, instance, placeholder):
        client = CopilotClient(settings.COPILOT_USER)
        #TODO pagination/count
        #TODO nice admin interface with choices
        if instance.artist_id:
            artist = Artist(instance.artist_id)
            context['events'] = artist.events.upcoming()['content']
        #TODO context for general event list
        return context
plugin_pool.register_plugin(EventListPlugin)
