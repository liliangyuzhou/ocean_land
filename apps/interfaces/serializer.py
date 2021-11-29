#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/18 09:54 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from .models import Interfaces
from projects.models import Projects

class InterfacesSerializer(serializers.ModelSerializer):
    #StringRelatedField默认是read_only=True,可以查看源码
    project=serializers.StringRelatedField(label="所属项目名称",help_text="所属项目名称")
    #queryset=Projects.objects.all()，对前端输入的project_id进行了一个校验，传入的项目id必须存在
    #PrimaryKeyRelatedField, 前端传的是id，这个字段会自动转换为Projects模型类对象，可以断点发现
    project_id=serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(),help_text="项目id")
    class Meta:
        model=Interfaces
        exclude=('update_time','is_delete')
        extra_kwargs={
            'create_time':{
                'read_only':True,
            }
        }
    def create(self, validated_data):
        project=validated_data.pop('project_id')
        validated_data['project']=project
        interface=Interfaces.objects.create(**validated_data)
        return interface
    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            project = validated_data.pop('project_id')
            validated_data['project'] = project
        return super(InterfacesSerializer, self).update(instance,validated_data)

class InterfacesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interfaces
        fields = ('name',)

class InterfacesModelSerializer(serializers.ModelSerializer):
    class Meta:
        # 1.指定参考哪一个模型类来创建
        model=Interfaces
        fields=('id','name')



