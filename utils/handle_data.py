#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/12/1 23:57 
# email： liang1.li@ximalaya.com

def handle_param_type(value):
    """
    判断param_type的类型
    :param value:
    :return: 
    """
    if isinstance(value,int):
        param_type="int"
    elif isinstance(value,float):
        param_type = "float"
    elif isinstance(value,bool):
        param_type = "boolean"
    else:
        param_type = "string"
    return param_type


def hand_data1(datas):
    """
    处理测试用例的validate
    :param datas:
    :return:
    """
    data_list = []
    if datas is not None:
        for one_dict in datas:
            key = one_dict.get('check')
            value = one_dict.get('expected')
            camparator=one_dict.get("camparator")
            data_list.append({
                'key': key,
                'value': value,
                'comparator': camparator,
                'param_type': handle_param_type(value)
            })
    return data_list



def hand_data2(datas):
    """
    处理配置文件的variables
    :param datas:
    :return:
    """
    data_list = []
    if datas is not None:
        for one_dict in datas:
            key = list(one_dict)[0]
            value=one_dict.get(key)
            data_list.append({
                'key':key,
                'value':value,
                'param_type': handle_param_type(value)
            })
    return data_list

def hand_data3(datas):
    data_list = []
    if datas is not None:
        for one_dict in datas:
            key = list(one_dict)[0]
            value = one_dict.get(key)
            data_list.append({
                'key': key,
                'value': value,
            })
    return data_list

def hand_data4(datas):
    """
    处理配置文件的请求头
    :param datas:
    :return:
    """
    data_list = []
    if datas is not None:
        for key, value in datas.items():
            data_list.append({
                'key': key,
                'value': value
            })
    return data_list
def hand_data5(datas):
    """
    处理配置文件的请求头
    :param datas:
    :return:
    """
    data_list = []
    if datas is not None:
        for item in datas:
            data_list.append({
                'key': item,
            })
    return data_list

def hand_data6(datas):

    data_list = []
    if datas is not None:
        for key, value in datas.items():
            data_list.append({
                'key': key,
                'value': value,
                'param_type': handle_param_type(value),
            })
    return data_list
