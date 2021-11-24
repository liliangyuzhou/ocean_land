#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/18 09:54 
# email： liang1.li@ximalaya.com
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from utils.tools import get_token
class RegisterModelSerializer(serializers.ModelSerializer):
    # 因为password_confirm和token在用户表中没有，所以我们需要自定义这个字段
    password_confirm = serializers.CharField(label="确认密码", min_length=6, max_length=20,
                                             help_text='确认密码',
                                             write_only=True,
                                             error_messages={
                                                 'min_length': '确认密码的最小长度为6位',
                                                 'max_length': '确认密码的最大长度为20位',
                                             })
    token = serializers.CharField(label='生成token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirm', 'token')

        # 因为用户模型类中对username做限制不符合我们的自己的要求，我们自己覆盖
        #注意model中没有的字段，不能写在extra_kwargs中指定校验
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'min_length': 6,
                'max_length': 20,
                'help_text': '用户名',
                'error_messages': {
                    'min_length': '用户名的最小长度为6位',
                    'max_length': '用户名的最大长度为20位',
                }
            },
            #邮箱字段user中是非必填，我们需求是必填 'required':True
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only':True,
                'required':True,
                #添加邮箱不允许重复
                'validators':[UniqueValidator(queryset=User.objects.all(),message=['此邮箱不能重复使用'])]
            },
            'password': {
                'label': '密码',
                'min_length': 6,
                'max_length': 20,
                'help_text': '密码',
                'write_only': True,
                'error_messages': {
                    'min_length': '确认密码的最小长度为6位',
                    'max_length': '确认密码的最大长度为20位',
                }
            },
        }

    def validate(self,attrs):
        if '@' not in attrs['email']:
            raise serializers.ValidationError('邮箱格式必须正确')
        if attrs['password']!=attrs['password_confirm']:
            raise serializers.ValidationError('密码和确认密码输入不一致')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        # user=User.objects.create(**validated_data)
        #调用此方法密码生成不是明文密码了,应当保存为加密的密码，调用set_password方法
        #方法一
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        #方法二，直接调用create_user()方法，创建的对象数据里面的秘密就是加密过的密码
        # user=User.objects.create_user(**validated_data)

        user.token=get_token(user)
        return user


