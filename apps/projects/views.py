import os
from datetime import datetime
from rest_framework import viewsets,permissions,decorators,status
from rest_framework.response import Response
from . import serializer
from .models import Projects
from utils.tools import get_count_by_project
from ocean_land import settings
from envs.models import Envs
from utils import run_tools
from interfaces.models import Interfaces
from apps.testcases.models import Testcases
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


    @decorators.action(methods=['GET','POST'],detail=False)
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
        elif self.action=='run':
            return serializer.RunProjectTestCaseSerializer
        else:
            return self.serializer_class

    #查询单个项目下面的所有接口
    @decorators.action(detail=True)
    def interfaces(self,request,*args,**kwargs):
        queryset = self.get_object()
        serializer=self.get_serializer(instance=queryset)
        return Response(serializer.data,status=200)

    def list(self, request, *args, **kwargs):
        response=super(ProjectsViewSet, self).list(request, *args, **kwargs)
        response.data['results']=get_count_by_project(response.data['results'])
        return response

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

        interface_objs= Interfaces.objects.filter(is_delete=False,project=instance)
        if not interface_objs.exists():
            data_dict={
                'detail':"项目下没有接口，无法运行项目"
            }
            return Response(data_dict,status=status.HTTP_400_BAD_REQUEST)
        for interface_obj in interface_objs:
            testcase_objs=Testcases.objects.filter(is_delete=False,interface=interface_obj)
            for testcases_obj in testcase_objs:
                # 生成ymal测试用例
                run_tools.generate_testcases_file(testcases_obj, env, dir_testcase_path)

        # 运行测试用例，返回报告id
        return run_tools.run_testcase(instance, dir_testcase_path)