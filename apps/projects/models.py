from django.db import models

# Create your models here.
from utils.base_model import BaseModel


class Projects(BaseModel):
    id = models.AutoField(verbose_name="项目id", primary_key=True, help_text="项目id")
    name = models.CharField(verbose_name="项目名称", help_text="项目名称", unique=True, max_length=200)
    tester = models.CharField(verbose_name="测试人员", help_text="测试人员", max_length=50)
    leader = models.CharField(verbose_name="项目负责人", help_text="项目负责人", max_length=50)
    programmer = models.CharField(verbose_name="开发负责人", help_text="开发负责人", max_length=50)
    publish_app = models.CharField(verbose_name="发布应用", help_text="发布应用", max_length=50)
    desc = models.TextField(verbose_name="项目描述", max_length=500, null=True, blank=True, default="")

    class Meta:
        db_table = "tb_projects"
        verbose_name = "项目表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
