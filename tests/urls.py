# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

urlpatterns = [
    url(r'bexiopy/', include('bexiopy.urls', namespace='bexiopy', app_name='bexiopy')),
]
