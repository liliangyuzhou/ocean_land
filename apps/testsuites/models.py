from django.db import models
from utils.base_model import BaseModel


class TestSuites(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="测试套件名称", help_text="测试套件名称", unique=True, max_length=200)
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, help_text="所属项目",
                                related_name='testsuites')
    author = models.CharField(verbose_name="创建人", help_text="创建人", max_length=50)
    include = models.TextField(verbose_name="包含的接口列表", null=True, help_text="包含的接口列表")

    class Meta:
        db_table = "tb_testsuites"
        verbose_name = "测试套件表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
