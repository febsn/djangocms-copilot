# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .api import CopilotClient
from .artists.api_models import Artist
from .events.api_models import EventManager
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

    def get_render_template(self, context, instance, placeholder):
        if instance.artist_id:
            return "copilot/plugins/artist-event-list.html"
        else:
            return "copilot/plugins/event-list.html"

    def render(self, context, instance, placeholder):
        client = CopilotClient(settings.COPILOT_USER)
        #TODO nice admin interface with choices
        kwargs = {
            'page.size': instance.event_count,
        }
        if instance.artist_id:
            artist = Artist(instance.artist_id)
            context['artist'] = artist
            context['events'] = artist.events.upcoming(**kwargs)['content']
        else:
            manager = EventManager()
            context['events'] = manager.upcoming(**kwargs)['content']
        return context
plugin_pool.register_plugin(EventListPlugin)
