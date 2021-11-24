from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.views import APIView
from .serializer import RegisterModelSerializer
from .models import User

#写类视图要继承什么类，看看需求需要那些方法
#注册不要要开启权限
class RegisterView(generics.CreateAPIView):
    #只有继承了GenericAPIView才有serializer_class和queryset
    serializer_class = RegisterModelSerializer
    #查询集没有必要，因为这里没有查询接口
    # queryset = User.objects.all()
    #认证授权都可以在类视图中分别指定
    # permission_classes =
    #类视图中使用jwt token进行认证
    # authentication_classes =('JSONWebTokenAuthentication',)
