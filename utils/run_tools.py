#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/12/3 16:04 
# email： liang1.li@ximalaya.com
import json
import os
import time

import yaml
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from httprunner.task import HttpRunner
from apps.debugtalk.models import DebugTalks
from configures.models import Configures
from apps.testcases.models import Testcases
from reports.models import Reports

def generate_testcases_file(instance,env,dir_testcase_path):
    """
    生成测试用例yaml文件
    :param instance: 测试用例对象
    :param env: 环境对象
    :param dir_testcase_path: 测试用例的路径
    :return:
    """
    testcases_list=[]
    config={
        'config':{
            "name":instance.name,
            'request':{
                "base_url":env.baseurl if env else "",

            }
        }
    }

    testcases_list.append(config)

    #获取当前测试用例的前置信息
    include=json.loads(instance.include,encoding="utf8")

    #获取当前用例的请求信息
    request=json.loads(instance.request,encoding="utf8")

    interface_name=instance.interface.name
    project_name=instance.interface.project.name

    testcase_projetc_dir_path=os.path.join(dir_testcase_path,project_name)

    if not os.path.exists(testcase_projetc_dir_path):
        os.mkdir(testcase_projetc_dir_path)
        debugtalk_obj=DebugTalks.objects.filter(is_delete=False,id=instance.interface.project_id).first()
        if debugtalk_obj:
            debugtalk=debugtalk_obj.debugtalk
        else:
            debugtalk=""

        #创建debugtalk.py文件
        debugtalk_path=os.path.join(testcase_projetc_dir_path,'debugtalk.py')
        with open(debugtalk_path,mode="w",encoding="utf8") as f:
            f.write(debugtalk)

    #在上方创建的项目目录下创建接口目录
    testcase_dir_interface_path=os.path.join(testcase_projetc_dir_path,interface_name)
    if not os.path.exists(testcase_dir_interface_path):
        os.mkdir(testcase_dir_interface_path)

    #组织构造测试用例
    #拆测试用例的include
    #如果testcases中的字段include中有config
    if 'config' in include:
        config_id=include.get('config')
        config_obj=Configures.objects.filter(is_delete=True,id=config_id).first()
        if config_obj:
            config_request=json.loads(config_obj.request,encoding="utf-8")

            #{"config":{"name":"3","request":{"headers":{"2":"2"}},"variables":[{"1":"1"}]}}
            config_request.get('config').get('request').setdafault('base_url',env.base_url)
            config_request['config']['name']=instance.name
            #把最开始的testcases_list中的config进行覆盖：因为此段config有肯能为空，所以就要使用上方的config
            testcases_list[0]=config_request
    #如果testcases中的字段include中有testcases（前置的测试用例）

    if 'testcases' in include:
        for case_id in include.get('testcases'):
            testcase_obj=Testcases.objects.filter(is_delete=False,id=case_id).first()
            if testcase_obj:
                try:
                    testcase_request=json.loads(testcase_obj.request,encoding="utf-8")
                except Exception as e:
                    raise e
                else:
                    testcases_list.append(testcase_request)
    #将当前用例的request添加到testcases_list
    testcases_list.append(request)

    #将拼接好的结构体testcases_list转换为ymal文件
    with open(os.path.join(testcase_dir_interface_path,instance.name+'.yml'),mode="w",encoding="utf8") as f:
        yaml.dump(testcases_list,f,allow_unicode=True)


def timestamp_to_datetime(summary, type=True):
    """
    根据官方的summary对里面涉及时间的字段进行转换
    :param summary:
    :param type:
    :return:
    """
    if not type:
        time_stamp=int(summary["time"]["start_at"])
        summary['time']["start_datetime"]=datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S")
        for detail in summary['details']:
            try:
                time_stamp = int(detail["time"]["start_at"])
                detail['time']["start_at"]=datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S")
            except Exception as e:
                continue

            for record in detail['records']:
                try:
                    time_stamp = int(record["meta_data"]['request']["start_timestamp"])
                    detail['time']["start_at"] = datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S")
                except Exception as e:
                    continue
    return summary


def create_report(runner, report_name):
    time_stamp=int(runner.summary["time"]["start_at"])
    runner.summary['time']["start_datetime"] = datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S")
    runner.summary['time']["duration"]=round(runner.summary['time']["duration"],2)
    report_name= report_name if report_name else runner.summary['time']["start_datetime"]
    for detail in runner.summary['details']:
        try:
            for record in detail['records']:
                #因为content是bytes类型，要转换为字符串传给前端
                record["meta_data"]['response']["content"]=record["meta_data"]['response']["content"].decode('utf-8')
                record["meta_data"]['response']["cookies"]=dict(record["meta_data"]['response']["cookies"])
                request_body= record["meta_data"]['request']["body"]
                if isinstance(request_body,bytes):
                    record["meta_data"]['request']["body"]=request_body.decode('utf-8')
        except Exception as e:
            continue
    #处理完bytes类型的属性后，然后转换summary为json类型字符串，用来创建reports模型类的summary字段
    summary=json.dumps(runner.summary,ensure_ascii=False)

    report_name=report_name+'_'+datetime.strftime(datetime.now(),'%Y%m%d%H%M%S%f')
    #生成测试报告
    #这里对我们来说生不生成都可以，因为前端根据summary的数值怎么渲染，但是我们创建的时候需要html字段，并且下载报告也用到了html字段
    report_path=runner.gen_html_report(html_report_name=report_name)

    with open(report_path,"r",encoding="utf-8") as f:
        reports=f.read()

    test_report={
        'name':report_name,
        'result':runner.summary.get('success'),
        'success':runner.summary.get('stat').get('successes'),
        'count':runner.summary.get('stat').get('testsRun'),
        'html':reports,
        'summary':summary
    }

    reports_obj=Reports.objects.create(**test_report)
    #这里返回reports模型类的id，后面可以用来打开报告
    return reports_obj.id

def run_testcase(instance,dir_testcase_path):
    """
    运行测试用例
    :param instance: 测试用例对象
    :param dir_testcase_path: 测试用例的目录
    :return:
    """
    runner=HttpRunner()
    try:
        runner.run(dir_testcase_path)
    except Exception:
        return Response({'msg': '用例执行失败'}, status=400)

    runner.summary=timestamp_to_datetime( runner.summary,type=False)

    try:
        report_name=instance.name
    except Exception as e:
        report_name='被遗弃的报告'+'_'+datetime.strftime(datetime.now(),'%Y%m%d%H%M%S%f')

    report_id=create_report(runner,report_name=report_name)
    #运行测试用例后返回报告id，给前端后可以打开测试报告
    data_dict={
        'id':report_id
    }
    return Response(data_dict,status=status.HTTP_201_CREATED)


















