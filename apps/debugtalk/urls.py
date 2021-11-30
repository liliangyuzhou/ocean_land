#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/30 14:24 
# email： liang1.li@ximalaya.com
from rest_framework.routers import DefaultRouter
from .views import EnvsViewSet
router=DefaultRouter()
router.register(r"",EnvsViewSet)
urlpatterns = [
]
urlpatterns += router.urls