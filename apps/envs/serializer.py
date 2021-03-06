#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/18 09:54 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from .models import Envs

class EnvModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        exclude = ('update_time', 'is_delete',)
        extra_kwargs = {
            'create_time': {
                'read_only': True
            },

        }

class EnvNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Envs
        fields=('id','name')