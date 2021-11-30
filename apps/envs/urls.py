#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/17 11:29 
# email： liang1.li@ximalaya.com

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EnvsViewSet
router=DefaultRouter()
router.register(r"",EnvsViewSet)
urlpatterns = [
]
urlpatterns += router.urls