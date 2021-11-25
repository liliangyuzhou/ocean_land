from django.db import models

from utils.base_model import BaseModel


class Interfaces(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="接口名称", help_text="接口名称", unique=True, max_length=200)
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, help_text="所属项目",
                                related_name='interfaces')
    tester = models.CharField(verbose_name="测试人员", help_text="测试人员", max_length=50)
    desc = models.TextField(verbose_name="接口描述", max_length=500, null=True, blank=True, default="")

    class Meta:
        db_table = "tb_interfaces"
        verbose_name = "接口表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
