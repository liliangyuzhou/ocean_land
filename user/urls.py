#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/17 11:29 
# email： liang1.li@ximalaya.com

from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, ObtainJSONWebToken
from . import views
urlpatterns = [
    # path('login/', ObtainJSONWebToken.as_view()),
    # 在子应用中添加jwt认证的login接口，path('login/', ObtainJSONWebToken.as_view())和下面一样
    # path('login/', obtain_jwt_token)
    path('register/',views.RegisterView.as_view())
]
