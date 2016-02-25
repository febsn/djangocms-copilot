# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.EventListView.as_view(), name='list')
]
