#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/30 17:52 
# email： liang1.li@ximalaya.com

from django.urls import path

from .views import ReportsViewSet

urlpatterns = [
    path('',ReportsViewSet.as_view)
]

