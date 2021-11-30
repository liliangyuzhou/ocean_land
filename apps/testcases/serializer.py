#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/18 09:54 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from apps.testcases.models import Testcases
from apps.debugtalk.models import DebugTalks
from interfaces.serializer import InterfacesModelSerializer


class TestCaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testcases
        exclude = ('update_time', 'is_delete',)
        extra_kwargs = {
            'create_time': {
                'read_only': True
            },

        }