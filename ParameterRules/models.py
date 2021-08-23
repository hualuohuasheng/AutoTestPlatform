# coding=utf-8
from django.db import models

# Create your models here.
class ParameterRules(models.Model):

    rule_name = models.CharField("参数化规则名称", max_length=200, default='')
    rule_method = models.CharField("参数化生成的方式", max_length=500, default='')
    rule_params = models.CharField("参数化生成的参数", max_length=500, default='')
    locations = (("header", "header"), ("body", "body"), ("result", "result"))
    rule_location = models.CharField("参数化生成的位置", choices=locations, max_length=200, default='header', null=True)

