#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/30 17:52 
# email： liang1.li@ximalaya.com
from rest_framework.routers import DefaultRouter
from .views import ReportsViewSet
router=DefaultRouter()
router.register(r"",ReportsViewSet)
urlpatterns = [
]
urlpatterns += router.urls
