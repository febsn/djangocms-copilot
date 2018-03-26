# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import *

from . import views
from ..utils import UUID_PATTERN

urlpatterns = [
    url(r'^$', views.RecordListView.as_view(), name='list'),
    url(r'^(?P<id>%s)/' % UUID_PATTERN, views.RecordDetailView.as_view(), name='detail'),
]
