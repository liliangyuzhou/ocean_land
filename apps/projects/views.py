from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions,decorators
from rest_framework.response import Response
from . import serializer
from .models import Projects
from utils.tools import get_count_by_project
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.filter(is_delete=False)
    serializer_class = serializer.ProjectModelSerializer
    #这里在全局指定IsAuthenticated权限，在注册和登陆接口放开所有权限即可
    # permission_classes = (permissions.IsAuthenticated)
    ordering_fields=('id','name')

    def perform_destroy(self, instance):
        """
        重写action中的perform_destroy方法，做逻辑删除
        :param instance:
        :return:
        """
        instance.is_delete=True
        instance.save()


    @decorators.action(methods=['GET','POST'],detail=False,url_path='pm',url_name='url_name')
    def names(self,request,*args,**kwargs):
        queryset=self.get_queryset()
        serializer=self.get_serializer(instance=queryset,many=True)
        return Response(serializer.data,status=200)

    def get_serializer_class(self):
        #如果一个类中，使用了多个不同序列化器类，那么我们可以将get_serializer_class重写
        #继承视图集类后，会提供action属性，指定当前请求的action方法名称
        #可以根据action去选择不同的序列化器类
        if self.action=='names':
            return serializer.ProjectNameSerializer
        elif self.action=='interfaces':
            return serializer.ProjectInterfacesSerializer
        else:
            return self.serializer_class

    #查询单个项目下面的所有接口
    @decorators.action(detail=True)
    def interfaces(self,request,*args,**kwargs):
        queryset = self.get_object()
        serializer=self.get_serializer(instance=queryset)
        return Response(serializer.data,status=200)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas=serializer.data
            datas=get_count_by_project(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_project(datas)
        return Response(datas)
