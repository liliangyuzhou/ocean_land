#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/25 10:25 
# email： liang1.li@ximalaya.com

from django.db import models

class BaseModel(models.Model):
    create_time=models.DateTimeField(verbose_name="创建时间",help_text="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间",help_text="更新时间" , auto_now=True)
    is_delete=models.BooleanField(verbose_name="逻辑删除",default=False,help_text="逻辑删除",)
    class Meta:
        #该模型为抽象模型，用来给其他模型继承，abstract=True在数据迁移的时候不会创建该BaseModel表
        abstract=True
        verbose_name="公共字段表"
        db_table="BaseModel"

