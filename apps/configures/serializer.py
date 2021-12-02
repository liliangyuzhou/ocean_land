#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/12/1 16:09 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from .models import Configures
from projects.models import Projects
from interfaces.models import Interfaces
from utils import validates


class InterfacesAndProjectSerializer(serializers.ModelSerializer):
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
        if not Interfaces.objects.filter(id=attrs['interface_id'], is_delete=False, project_id=attrs['project_id']):
            raise serializers.ValidationError("项目和接口信息不对应")
        return attrs


class ConfigureSerializer(serializers.ModelSerializer):
    interface = InterfacesAndProjectSerializer(help_text="项目id和接口id")

    class Meta:
        model = Configures
        # exclude = ('update_time', 'is_delete', 'create_time')
        fields=('id','name','interface','author','request')
        extra_kwargs = {
            'request': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        interface_dict=validated_data.pop('interface')
        validated_data['interface_id']=interface_dict['interface_id']
        return Configures.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'interface' in validated_data:
            interface_dict=validated_data.pop('interface')
            validated_data['interface_id']=interface_dict['interface_id']
        return super(ConfigureSerializer, self).update(instance,validated_data)