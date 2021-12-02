#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/18 09:54 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from apps.testcases.models import Testcases
from interfaces.models import Interfaces
from utils import validates


class InterfacesAndProjectSerializer(serializers.ModelSerializer):
    # 该序列化化器创建是字段project_id和interface_id，序列化输出是project（项目名称）和name（接口名称）
    project = serializers.StringRelatedField(help_text="项目名称")
    project_id = serializers.IntegerField(write_only=True, validators=[validates.exist_project_id])
    interface_id = serializers.IntegerField(write_only=True, validators=[validates.exist_interface_id])

    class Meta:
        model = Interfaces
        fields = ('interface_id', 'name', 'project_id', 'project')
        extra_kwargs = {
            'name': {
                'read_only': True,
                'help_text': "接口名称"
            }
        }

    def validate(self, attrs):
        if not Interfaces.objects.filter(id=attrs['interface_id'], is_delete=False,
                                         project_id=attrs['project_id']).exists():
            raise serializers.ValidationError("项目和接口信息不对应")
        return attrs


class TestCaseModelSerializer(serializers.ModelSerializer):
    interface = InterfacesAndProjectSerializer(help_text="所属接口和项目信息")

    class Meta:
        model = Testcases
        # exclude = ('update_time', 'is_delete','create_time')
        fields = ('id', 'name', 'interface', 'include', 'request', 'author')
        extra_kwargs = {
            'request': {
                'write_only': True
            },
            'include': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        interface_dict = validated_data.pop('interface')
        validated_data['interface_id'] = interface_dict['interface_id']
        return Testcases.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'interface' in validated_data:
            interface_dict = validated_data.pop('interface')
            validated_data['interface_id'] = interface_dict['interface_id']
        return super().update(instance, validated_data)
