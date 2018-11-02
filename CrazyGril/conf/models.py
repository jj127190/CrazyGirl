# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# class conf(models.Model):
#     """
#     CONF INFO LIST
#     """
#     hostip = models.CharField(verbose_name=(u'hostip'), max_length=50, default='')
#     hostport = models.CharField(verbose_name=(u'hostport'), max_length=50, default='')
#     logfiles = models.CharField(verbose_name=(u'logfiles'), max_length=50, default='')
#     dockerfileca = models.CharField(verbose_name=(u'dockerfileca'), max_length=50, default='')
#     mysql_port = models.CharField(verbose_name=(u'mysql_port'), max_length=50, default='')
#     mysql_pass = models.CharField(verbose_name=(u'mysql_pass'), max_length=50, default='')
#     mysqldb = models.CharField(verbose_name=(u'mysqldb'), max_length=50, default='')
#     mysqlip = models.CharField(verbose_name=(u'mysqlip'), max_length=50, default='')
#     upload_time = models.DateTimeField(auto_now_add=True, blank=True)
#
#     # create_time = models.CharField(verbose_name=(u'创建时间'), max_length=50, default='')
#     class Meta:
#         ordering = ['-upload_time']
#         verbose_name = u'dockerfile管理'
#         verbose_name_plural = verbose_name
