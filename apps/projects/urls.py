#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/17 11:29 
# email： liang1.li@ximalaya.com

from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, ObtainJSONWebToken
from .views import ProjectsViewSet
router=DefaultRouter()
router.register(r"",ProjectsViewSet)
urlpatterns = [
    # path('projects/',ProjectsViewSet.as_view())
]
urlpatterns += router.urls