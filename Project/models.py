# coding=utf-8
from django.db import models

# Create your models here.
class Project(models.Model):
    project_id = models.BigAutoField("项目ID", auto_created=True, primary_key=True, serialize=False)
    project_name = models.CharField("项目名称", max_length=100, default='')
    project_producer = models.CharField("项目创建者", max_length=100, default='')
    project_description = models.TextField("项目描述", default='')
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)

    # Project.objects.create(project_name='测试1', project_producer='abc', project_description='这是一个测试')
    class Meta:
        db_table = "project"
        verbose_name = "项目管理"
