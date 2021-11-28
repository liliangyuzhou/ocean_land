#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/19 00:21 
# email： liang1.li@ximalaya.com
import datetime

from rest_framework_jwt.settings import api_settings
import re
from interfaces.models import Interfaces
from testsuites.models import TestSuites
from django.db.models import Count

def UTC2BJS(UTC):
    UTC_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    BJS_format = "%Y-%m-%d %H:%M:%S"
    UTC = datetime.datetime.strptime(UTC,UTC_format)
    #格林威治时间+8小时变为北京时间
    BJS = UTC + datetime.timedelta(hours=8)
    BJS = BJS.strftime(BJS_format)
    return BJS

def get_token(user):
    """
    用于注册获取jwt token
    :param user:
    :return:
    """
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token

def get_count_by_project(datas):

    datas_list=[]
    for item in datas:

        item['create_time'] =UTC2BJS(item['create_time'])
        project_id=item['id']
        interfaces_testcases_objs=Interfaces.objects.values('id').annotate(testcases=Count('testceses')).\
            filter(project_id=project_id,is_delete=False)
        # 统计项目下接口总数
        interfaces_count=interfaces_testcases_objs.count()
        #统计项目下所有未删除接口的用例总数
        testcases_count=0
        for testcases in interfaces_testcases_objs:
            testcases_count+=testcases['testcases']
        #统计项目下的所有未删除接口的配置总数
        interfaces_configures_objs = Interfaces.objects.values('id').annotate(configures=Count('configures')). \
            filter(project_id=project_id, is_delete=False)
        configures_count = 0
        for  configures in interfaces_configures_objs:
            configures_count +=  configures['configures']
        #统计项目下的所有未删除的测试套件的总数
        testsuites_count = TestSuites.objects.filter(project_id=project_id, is_delete=False).count()
        item['interfaces']=interfaces_count
        item['testsuites']=testsuites_count
        item['testcases']=testcases_count
        item['configures']=configures_count
        datas_list.append(item)
    return datas_list