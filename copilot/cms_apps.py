# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

@apphook_pool.register
class ArtistsApphook(CMSApp):
    name = _("Copilot Artists")
    app_name = 'artists'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["copilot.artists.urls"]

@apphook_pool.register
class EventsApphook(CMSApp):
    name = _("Copilot Events")
    app_name = 'events'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["copilot.events.urls"]

@apphook_pool.register
class RecordsApphook(CMSApp):
    name = _("Copilot Records")
    app_name = 'records'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["copilot.records.urls"]
