#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/18 09:54 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from .models import TestSuites
from projects.models import Projects
from utils import validates
from interfaces.models import Interfaces

class TestSuitesSerializer(serializers.ModelSerializer):
    #StringRelatedField默认是read_only=True,可以查看源码
    project=serializers.StringRelatedField(label="所属项目名称",help_text="所属项目名称")
    #queryset=Projects.objects.all()，对前端输入的project_id进行了一个校验，传入的项目id必须存在
    #PrimaryKeyRelatedField, 前端传的是id，这个字段会自动转换为Projects模型类对象，可以断点发现
    project_id=serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(),help_text="项目id")

    class Meta:
        model = TestSuites
        exclude = ('is_delete',)
        # fields = ('id', 'name', 'project_id','project' 'author', 'include', 'create_time', 'update_time')
        extra_kwargs = {
            'create_time': {
                'read_only': True,
            },
            'update_time': {
                'read_only': True,
            },
            'author': {
                'read_only': True,
            },
            'author': {
                'read_only': True,
            }
        }
    def create(self, validated_data):
        # project=validated_data.pop('project_id')
        # validated_data['project']=project
        validated_data['project_id']=validated_data['project_id'].id
        testsuites=TestSuites.objects.create(**validated_data)
        return testsuites
    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            # project = validated_data.pop('project_id')
            # validated_data['project'] = project
            validated_data['project_id'] = validated_data['project_id'].id
        return super(TestSuitesSerializer, self).update(instance,validated_data)

class TestSuitesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=TestSuites
        fields = ('name',)

class TestSuitesModelSerializer(serializers.ModelSerializer):
    class Meta:
        # 1.指定参考哪一个模型类来创建
        model=TestSuites
        fields=('id','name')

class RunTestSuitesTestCaseSerializer(serializers.ModelSerializer):
    """
    运行整个项目的测试用例的序列化器
    """
    env_id = serializers.IntegerField(write_only=True, validators=[validates.exist_env_id], help_text="环境变量id")

    class Meta:
        model = TestSuites
        fields = ('id', 'env_id')
