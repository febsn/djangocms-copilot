# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from copilot.api import CopilotClient
from copilot.conf import settings
from copilot.models import News

class NewsPlugin(CMSPluginBase):
    module = 'Copilot'
    name = _('News plugin')
    model = News
    render_template = "copilot/plugins/news.html"
    endpoint = "news"
    cache = False

    def render(self, context, instance, placeholder):
        client = CopilotClient(settings.COPILOT_USER)
        context['news'] = client.get(self.endpoint).json()['content']
        return context


plugin_pool.register_plugin(NewsPlugin)
