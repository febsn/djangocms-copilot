# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import *

from . import views
from ..utils import UUID_PATTERN

urlpatterns = [
    url(r'^$', views.ArtistListView.as_view(), name='all'),
    url(r'^(?P<id>%s)/' % UUID_PATTERN, views.ArtistDetailView.as_view(), name='get'),
]
