import os
from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework import decorators
from .serializer import InterfacesSerializer,InterfacesNameSerializer,RunInterfaceTestCaseSerializer
from .models import Interfaces
from apps.testcases.models import Testcases
from configures.models import Configures
from utils.tools import get_count_by_interface
from utils import run_tools
from ocean_land import settings
from envs.models import Envs
# Create your views here.

class InterfacesViewSet(viewsets.ModelViewSet):
    serializer_class = InterfacesSerializer
    queryset = Interfaces.objects.filter(is_delete=False)


    def perform_destroy(self, instance):
        instance.is_delete=True
        instance.save()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas=serializer.data
            datas=get_count_by_interface(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_interface(datas)
        return Response(datas)

    @decorators.action(detail=False)
    def names(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data, status=200)

    def get_serializer_class(self):
        if self.action=='names':
            return InterfacesNameSerializer
        elif self.action=='run':
            return RunInterfaceTestCaseSerializer
        else:
            return self.serializer_class

    @decorators.action(detail=True)
    def testcases(self,request,pk=None):
        testcases=Testcases.objects.filter(interface_id=pk,is_delete=False)
        one_list=[]
        for item in testcases:
            one_list.append(
                {'id':item.id,
                 'name':item.name
                 }
            )
        return Response(data=one_list)

    @decorators.action(detail=True,url_path='configs')
    def configures(self,request,pk=None):
        configures=Configures.objects.filter(interface_id=pk,is_delete=False)
        one_list=[]
        for item in configures:
            one_list.append(
                {'id': item.id,
                 'name': item.name
                 }
            )
        return Response(data=one_list)

    @decorators.action(methods=['post'], detail=True)
    def run(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        datas = serializer.validated_data
        env_id = datas.get('env_id')
        #创建测试用例所在的目录名
        dir_testcase_path = os.path.join(settings.SUITES_DIR, datetime.strftime(datetime.now(), '%Y%m%d%H%M%S%f'))
        if not os.path.exists(dir_testcase_path):
            os.mkdir(dir_testcase_path)

        env = Envs.objects.filter(id=env_id,is_delete=False).first()

        testcase_objs= Testcases.objects.filter(is_delete=False,interface_id=instance.id)
        if not testcase_objs.exists():
            data_dict={
                'detail':"接口下没有测试用例，无法运行接口"
            }
            return Response(data_dict,status=status.HTTP_400_BAD_REQUEST)
        for testcases_obj in testcase_objs:
            # 生成ymal测试用例
            run_tools.generate_testcases_file(testcases_obj, env, dir_testcase_path)
        # 运行测试用例，返回报告id
        return run_tools.run_testcase(instance, dir_testcase_path)



