from django.db import models

from utils.base_model import BaseModel


class Reports(BaseModel):
    id = models.AutoField(verbose_name="项目id", primary_key=True, help_text="项目id")
    name = models.CharField(verbose_name="报告名称", help_text="报告名称", unique=True, max_length=200)
    result=models.BooleanField(verbose_name="执行结果",default=1,help_text="执行结果")#1代表True
    count=models.IntegerField(verbose_name="用例总数",help_text="用例总数")
    success = models.IntegerField(verbose_name="执行成功总数", help_text="执行成功总数")
    html = models.TextField(verbose_name="测试报告html源码", null=True, blank=True, default="",help_text="测试报告html源码")
    summary=models.TextField(verbose_name="报告详情数据", null=True, blank=True, default="",help_text="报告详情数据")


    class Meta:
        db_table = "tb_reports"
        verbose_name = "测试报告表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
