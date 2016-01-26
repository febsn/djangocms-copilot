# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ArtistsApphook(CMSApp):
    name = _("Copilot Artists")
    urls = ["copilot.artists.urls"]
    app_name = 'artists'
apphook_pool.register(ArtistsApphook)

class EventsApphook(CMSApp):
    name = _("Copilot Events")
    urls = ["copilot.events.urls"]
    app_name = 'events'
apphook_pool.register(EventsApphook)
