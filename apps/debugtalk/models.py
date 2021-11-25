from django.db import models

from utils.base_model import BaseModel


class DebugTalks(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="DebugTalks名称", help_text="测试套件名称", max_length=200,default='debugtalk.py')
    project = models.OneToOneField('projects.Projects', on_delete=models.CASCADE, help_text="所属项目",
                                related_name='debugtalks')
    debugtalk=models.TextField(verbose_name="debugtalk文件内容",default="#debugtalk.py",help_text="debugtalk文件内容",null=True)

    class Meta:
        db_table = "tb_debugtalks"
        verbose_name = "debugtalks.py"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name