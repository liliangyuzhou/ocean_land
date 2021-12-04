#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/12/1 16:45 
# email： liang1.li@ximalaya.com

from projects.models import Projects
from interfaces.models import Interfaces
from envs.models import Envs
from rest_framework import serializers
def exist_project_id(value):
    if not isinstance(value,int):
        raise serializers.ValidationError("所选项目不合法")
    elif not Projects.objects.filter(id=value,is_delete=False).exists():
        raise serializers.ValidationError("所选项目不存在")

def exist_interface_id(value):
    if not isinstance(value,int):
        raise serializers.ValidationError("所选接口不合法")
    elif not Interfaces.objects.filter(id=value,is_delete=False).exists():
        raise serializers.ValidationError("所选接口不存在")

def exist_env_id(value):
    if value !=0:
        if not Envs.objects.filter(id=value,is_delete=False).exists():
            raise serializers.ValidationError("所选环境配置不存在")