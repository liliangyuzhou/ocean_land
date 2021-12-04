import json
import os
from datetime import datetime
from rest_framework import viewsets,permissions,decorators
from rest_framework.response import Response
from . import serializer
from apps.testcases.models import Testcases
from interfaces.models import Interfaces
from utils import handle_data
from ocean_land import settings
from envs.models import Envs
from utils import run_tools
class TestCasesViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.TestCaseModelSerializer
    queryset = Testcases.objects.filter(is_delete=False)

    def perform_destroy(self, instance):
        instance.is_delete=True
        instance.save()

    def retrieve(self, request, *args, **kwargs):
        #获取测试用例对象instance，这里写成testcase_obj更好理解
        testcase_obj=self.get_object()
        #获取测试用例的前置信息

        #数据库存的是json，我们要转成python的字典，少用eval
        testcase_include=json.loads(testcase_obj.include)

        #用例的请求信息
        testcase_request=json.loads(testcase_obj.request)
        testcase_request_datas=testcase_request.get('test').get('request')

        # #用例的名称
        # testcase_name=testcase_request.get('test').get('name')

        #处理测试用例的validate
        testcase_validate=testcase_request.get('test').get('validate')
        testcase_validate_list=handle_data.hand_data1(testcase_validate)

        #处理测试用例的param数据
        testcase_params=testcase_request_datas.get('params')
        testcase_params_list = handle_data.hand_data4(testcase_params)

        # 处理测试用例的header数据
        testcase_headers = testcase_request_datas.get('headers')
        testcase_headers_list = handle_data.hand_data4(testcase_headers)

        #处理测试用例的variables列表
        testcase_variables= testcase_request_datas.get('variables')
        testcase_variables_list = handle_data.hand_data2(testcase_variables)

        #处理测试用例的form表单数据
        testcase_form_datas=testcase_request_datas.get('data')
        testcase_form_datas_list=handle_data.hand_data6(testcase_form_datas)

        #处理测试用例的json数据
        testcase_json_datas=json.dumps(testcase_request_datas.get('json'),ensure_ascii=False)

        #处理测试用例的extract数据
        testcase_extract_datas = testcase_request.get('test').get('extract')
        testcase_extract_datas_list = handle_data.hand_data3(testcase_extract_datas)

        #处理parameter数据
        testcase_parameters_datas = testcase_request.get('test').get('extract')
        testcase_parameters_datas_list = handle_data.hand_data3(testcase_parameters_datas)

        #处理setup_hooks数据
        testcase_setup_hooks_datas = testcase_request.get('test').get('setup_hooks')
        testcase_setup_hooks_datas_list = handle_data.hand_data5(testcase_setup_hooks_datas)

        # 处理teardown_hooks数据
        testcase_teardown_hooks_datas = testcase_request.get('test').get('teardown_hooks')
        testcase_teardown_hooks_datas_list = handle_data.hand_data5(testcase_teardown_hooks_datas)

        selected_configure_id=testcase_include.get('config')
        selected_interface_id=testcase_obj.interface_id
        selected_project_id=Interfaces.objects.get(id=selected_interface_id).project_id
        selected_testcase_id=testcase_include.get('testcases')
        datas={
            "author":testcase_obj.author,
            "testcase_name":testcase_obj.name,
            "selected_configure_id":selected_configure_id,
            "selected_interface_id":selected_interface_id,
            "selected_project_id":selected_project_id,
            "selected_testcase_id":selected_testcase_id,
            "method":testcase_request_datas.get('method'),
            "url":testcase_request_datas.get('url'),
            "param":testcase_parameters_datas_list,
            "header":testcase_headers_list,
            "variable":testcase_form_datas_list,#表单请求
            "jsonVariable":testcase_json_datas,
            "extract":testcase_extract_datas_list,
            "validate":testcase_validate_list,
            "globalVar":testcase_variables_list,
            "parameterized":testcase_parameters_datas_list,
            "setupHooks":testcase_setup_hooks_datas_list,
            "teardownHooks":testcase_teardown_hooks_datas_list,
        }
        return Response(datas)

    @decorators.action(methods=['post'],detail=True)
    def run(self,request,*args,**kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        datas=serializer.validated_data
        env_id=datas.get('env_id')
        dir_testcase_path=os.path.join(settings.SUITES_DIR,datetime.strftime(datetime.now(),'%Y%m%d%H%M%S%f'))
        os.mkdir(dir_testcase_path)

        env=Envs.objects.get(id=env_id)

        #生成ymal测试用例
        run_tools.generate_testcases_file(instance,env,dir_testcase_path)

        #运行测试用例，返回报告id
        return run_tools.run_testcase(instance,dir_testcase_path)






    def  get_serializer_class(self):
        if self.action=="run":
            return serializer.RunTestCaseSerializer
        else:
            return self.serializer_class














