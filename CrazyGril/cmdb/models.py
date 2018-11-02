# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.



ASSET_STATUS=(
    (str(1), u"使用中"),
    (str(2), u"未使用"),
    (str(3), u"故障"),
    (str(4), u"其他"),
)

ASSET_TYPE = (
    (str(1), u"物理机"),
    (str(2), u"虚拟机"),
    (str(3), u"容器"),
    (str(4), u"网络设备"),
    (str(5), u"安全设备"),
    (str(6), u"其他"),
)



class alert_temp(models.Model):
    alert_name = models.CharField(u"报警模板", max_length=100, blank=True)
    alert_time = models.CharField(u"报警时间", max_length=100, blank=True)
    alert_user =models.CharField(u"报警人", max_length=100, blank=True)
    tag_time = models.DateTimeField(auto_now_add=True, blank=True)
    default = models.CharField(u"默认", max_length=100, blank=True)
    mem = models.CharField(u"内存", max_length=100, blank=True)
    df = models.CharField(u"df", max_length=100, blank=True)
    io = models.CharField(u"io", max_length=100, blank=True)
    upload = models.CharField(u"upload 时间", max_length=100, blank=True)
    traffic_in = models.CharField(u"流量in", max_length=100, blank=True)
    traffic_out = models.CharField(u"流量out", max_length=100, blank=True)
    port = models.CharField(u"端口", max_length=100, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, blank=True)



class Idc(models.Model):
    ids = models.CharField(u"机房标识", max_length=255, unique=True)
    name = models.CharField(u"机房名称", max_length=255, unique=True)
    address = models.CharField(u"机房地址", max_length=100, blank=True)
    tel = models.CharField(u"机房电话", max_length=30, blank=True)
    contact = models.CharField(u"客户经理", max_length=30, blank=True)
    contact_phone = models.CharField(u"移动电话", max_length=30, blank=True)
    jigui = models.CharField(u"机柜信息", max_length=30, blank=True)
    ip_range = models.CharField(u"IP范围", max_length=30, blank=True)
    bandwidth = models.CharField(u"接入带宽", max_length=30, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'数据中心'
        verbose_name_plural = verbose_name



class Host(models.Model):
    hostname = models.CharField(max_length=50, verbose_name=u"主机名", unique=True)
    ip = models.GenericIPAddressField(u"管理IP", max_length=15)
    idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    other_ip = models.CharField(u"其它IP", max_length=100, blank=True)
    asset_no = models.CharField(u"资产编号", max_length=50, blank=True)
    asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
    status = models.CharField(u"设备状态", choices=ASSET_STATUS, max_length=30, null=True, blank=True)
    os = models.CharField(u"操作系统", max_length=100, blank=True)
    vendor = models.CharField(u"设备厂商", max_length=50, blank=True)
    up_time = models.CharField(u"上架时间", max_length=50, blank=True)
    cpu_model = models.CharField(u"CPU型号", max_length=100, blank=True)
    cpu_num = models.CharField(u"CPU数量", max_length=100, blank=True)
    memory = models.CharField(u"内存大小", max_length=30, blank=True)
    disk = models.CharField(u"硬盘信息", max_length=255, blank=True)
    sn = models.CharField(u"SN号 码", max_length=60, blank=True)
    position = models.CharField(u"所在位置", max_length=100, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-upload_time']
        verbose_name = u'asset管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.hostname


class HostGroup(models.Model):
    name = models.CharField(u"服务器组名", max_length=30, unique=True)
    desc = models.CharField(u"描述", max_length=100, blank=True)
    txt = models.TextField(u"txt", max_length=10000, blank=True)




    def __unicode__(self):
        return self.name

















#
#
#
#
#
#
#
#
#
# class dingding(models.Model):
#     account = models.CharField(u"账号", max_length=100, blank=True)
#     passwd = models.CharField(u"密码", max_length=100, blank=True)
#     platform = models.CharField(u"钉钉平台", max_length=100, blank=True)
#     alert_name = models.CharField(u"报警名称", max_length=50, blank=True)
#     msg_on = models.CharField(u"消息推送", max_length=50, blank=True)
#     url = models.CharField(u"url", max_length=100, blank=True)
#     access_token = models.CharField(u"token", max_length=100, blank=True)
#     memo = models.TextField(u"信息", max_length=200, blank=True)
#     msg = models.TextField(u"msg", max_length=200, blank=True)
#     keep_msg = models.TextField(u"msg keep", max_length=300, blank=True)
#
#     upload_time = models.DateTimeField(auto_now_add=True, blank=True)
#
#     class Meta:
#         ordering = ['-upload_time']
#         verbose_name = u'钉钉报警'
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.hostname
