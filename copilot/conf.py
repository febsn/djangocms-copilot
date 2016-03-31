# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from appconf import AppConf

class CopilotConf(AppConf):
    PAGE_SIZE = 30
    ASSET_TAGS = ['ARTIST_MAINIMAGE', 'ARTIST_PRESSIMAGE', ]

    class Meta:
        prefix = 'copilot'
