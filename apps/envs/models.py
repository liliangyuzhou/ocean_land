from django.db import models

from utils.base_model import BaseModel


class Envs(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="环境名称", help_text="环境名称", max_length=200)
    baseurl=models.URLField(verbose_name="请求的base_url",max_length=300,help_text="请求的base_url")
    desc = models.TextField(verbose_name="环境描述", max_length=200, null=True, blank=True, default="")

    class Meta:
        db_table = "tb_envs"
        verbose_name = "项目的全局环境变量配置表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
