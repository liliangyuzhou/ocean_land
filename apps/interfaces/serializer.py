#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/18 09:54 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from .models import Interfaces

class InterfacesSerializer(serializers.ModelSerializer):
    project=serializers.StringRelatedField(read_only=True,label="所属项目名称")
    class Meta:
        model=Interfaces
        exclude=('update_time','is_delete')
        extra_kwargs={
            'create_time':{
                'read_only':True,
            }
        }

class InterfacesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interfaces
        fields = ('name',)



