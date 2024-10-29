# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin

from tests import views

import lock_tokens.urls

urlpatterns = [
    re_path(r"^lock-tokens/", include(lock_tokens.urls, namespace="lock-tokens")),
    re_path(r"^test1/$", views.test_view_1, name="view-that-locks-object-1"),
    re_path(
        r"^test2/(?P<object_id>\d+)/$",
        views.test_view_2,
        name="view-that-locks-object-2",
    ),
    re_path(
        r"^test3/(?P<object_id>\d+)/$",
        views.test_view_3,
        name="view-that-unlocks-object",
    ),
    re_path(r"^admin/", admin.site.urls),
]
