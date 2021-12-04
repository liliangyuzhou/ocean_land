from django.shortcuts import render
import os
from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import decorators,status
from .serializer import TestSuitesModelSerializer,TestSuitesNameSerializer,RunTestSuitesTestCaseSerializer,TestSuitesSerializer
from .models import TestSuites
from utils.tools import get_count_by_interface,get_count_by_testsuites
from apps.testcases.models import Testcases
from interfaces.models import Interfaces
from ocean_land import settings
from utils import run_tools
from envs.models import Envs
# Create your views here.

class TestSuitesViewSet(ModelViewSet):
    serializer_class = TestSuitesSerializer
    queryset = TestSuites.objects.filter(is_delete=False)


    def perform_destroy(self, instance):
        instance.is_delete=True
        instance.save()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas=serializer.data
            datas=get_count_by_testsuites(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_testsuites(datas)
        return Response(datas)

    def get_serializer_class(self):
        if self.action=='run':
            return RunTestSuitesTestCaseSerializer
        else:
            return self.serializer_class


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

        include = eval(instance.include)
        if len(include) == 0:
            data_dict = {
                'detail': "此套件下没有测试用例，无法执行"
            }
            return Response(data_dict, status=status.HTTP_400_BAD_REQUEST)
        for interface_id in include:
            testcase_objs = Testcases.objects.filter(is_delete=False, interface=interface_id)
            if testcase_objs:
                for testcases_obj in testcase_objs:
                    # 生成ymal测试用例
                    run_tools.generate_testcases_file(testcases_obj, env, dir_testcase_path)

        # 运行测试用例，返回报告id
        return run_tools.run_testcase(instance, dir_testcase_path)