from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name="项目名称", max_length=30, unique=True,
                            help_text="项目名称")

    leader = models.CharField(verbose_name="负责人", max_length=50,
                              help_text="负责人")