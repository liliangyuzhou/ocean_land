#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/30 14:24 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from apps.debugtalk.models import DebugTalks

class DebugTalkModelSerializer(serializers.ModelSerializer):
    project=serializers.StringRelatedField(help_text="项目名称")
    class Meta:
        model = DebugTalks
        exclude = ('update_time', 'is_delete','create_time')
        extra_kwargs = {
            'name': {
                'read_only': True
            },
            'debugtalk': {
                'write_only': True
            },
        }
