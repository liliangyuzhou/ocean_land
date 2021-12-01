#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/30 17:53 
# email： liang1.li@ximalaya.com
from rest_framework.serializers import ModelSerializer
from .models import Reports


class ReportsModelSerializer(ModelSerializer):
    class Meta:
        model = Reports
        exclude = ('update_time', 'is_delete',)

        extra_kwargs = {
            'create_time': {
                'read_only': True
            },
            'html': {
                'write_only': True
            }
        }
