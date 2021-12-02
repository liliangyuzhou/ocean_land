#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/12/1 23:57 
# email： liang1.li@ximalaya.com

def handle_param_type(value):
    if isinstance(value,int):
        param_type="int"
    elif isinstance(value,float):
        param_type = "float"
    elif isinstance(value,bool):
        param_type = "boolean"
    else:
        param_type = "string"
    return param_type



def hand_data2(datas):
    """
    列表嵌套字典
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


def hand_data4(datas):
    data_list = []
    if datas is not None:
        for key, value in datas.items():
            data_list.append({
                'key': key,
                'value': value
            })
    return data_list
