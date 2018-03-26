# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

class News(CMSPlugin):
    pass


class EventList(CMSPlugin):
    artist_id = models.UUIDField(null=True, blank=True, verbose_name=_("artist id"))
    event_count = models.PositiveIntegerField(
        verbose_name=_('number of events'),
        default=5,
        validators=[MinValueValidator(1)],
        help_text=_('The maximum number of events to show.')
)
