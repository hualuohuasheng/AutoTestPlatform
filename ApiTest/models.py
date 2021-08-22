# coding=utf8
from django.db import models


# Create your models here.
class Project(models.Model):

    project_id = models.BigIntegerField("项目ID", primary_key=True, null=False, db_index=True)
    project_name = models.CharField("项目名称", max_length=100, default='')
    project_producer = models.CharField("项目创建者", max_length=100, default='')
    project_description = models.TextField("项目描述", default='')
    create_time = models.DateTimeField("创建时间", auto_now=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        db_table = "project"
        verbose_name = "项目管理"


class GlobalParameters(models.Model):

    name = models.CharField("参数名称", max_length=50, default='')

