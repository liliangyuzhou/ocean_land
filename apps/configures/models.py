from django.db import models

# Create your models here.
from utils.base_model import BaseModel


class Configures(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="配置名称", help_text="配置名称", unique=True, max_length=200)
    interface = models.ForeignKey('interfaces.Interfaces', on_delete=models.CASCADE, help_text="所属接口",
                                  related_name='configures')
    author = models.CharField(verbose_name="创建人", help_text="创建人", max_length=50)
    request = models.TextField(verbose_name="请求详情", help_text="请求详情")

    class Meta:
        db_table = "tb_configures"
        verbose_name = "测试用例配置表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
