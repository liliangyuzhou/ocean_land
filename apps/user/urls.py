#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/17 11:29 
# email： liang1.li@ximalaya.com

from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token, ObtainJSONWebToken
from apps.user import views
urlpatterns = [
    # path('login/', ObtainJSONWebToken.as_view()),
    # 在子应用中添加jwt认证的login接口，path('login/', ObtainJSONWebToken.as_view())和下面一样
    path('login/', obtain_jwt_token),
    path('register/',views.RegisterView.as_view()),
    #验证用户名是否存在
    re_path(r'^(?P<username>\w{6,20})/count/$', views.UsernameIsExistedView.as_view()),
    #验证邮件是否存在
    re_path(r'^(?P<email>[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+)/count/$',
            views.EmailIsExistedView.as_view()),
]
