#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/18 09:54 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from .models import Projects
from apps.debugtalk.models import DebugTalks
from interfaces.serializer import InterfacesModelSerializer
from utils import validates


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ('update_time', 'is_delete',)
        extra_kwargs = {
            'create_time': {
                'read_only': True
            },

        }

    def create(self, validated_data):
        #发现父类ModelSerializer的序列化器没有需要重写的，我们直接调用父类的create方法就可以
        # project_obj = super().create(**validated_data)
        project_obj = Projects.objects.create(**validated_data)
        DebugTalks.objects.create(project=project_obj)
        return project_obj
class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields = ('id','name',)

class ProjectInterfacesSerializer(serializers.ModelSerializer):
    #单独输出一个项目下所有接口的id
    # interfaces = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    interfaces = InterfacesModelSerializer(read_only=True, many=True)
    class Meta:
        model=Projects
        fields = ('name','interfaces',)

class RunProjectTestCaseSerializer(serializers.ModelSerializer):
    """
    运行整个项目的测试用例的序列化器
    """
    env_id = serializers.IntegerField(write_only=True, validators=[validates.exist_env_id], help_text="环境变量id")

    class Meta:
        model = Projects
        fields = ('id', 'env_id')