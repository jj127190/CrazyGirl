# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class dockerfiles(models.Model):
    """
    DOCKERFILE INFO LIST
    """
    status = models.CharField(verbose_name=(u'status'), max_length=50, default='')
    newimage = models.CharField(verbose_name=(u'newimage'), max_length=50, default='')
    dfilename = models.CharField(verbose_name=(u'dockerfilename'), max_length=50, default='')
    base_image = models.CharField(verbose_name=(u'ID'), max_length=50, default='')
    maintainer = models.CharField(verbose_name=(u'维护者'), max_length=50, default='')
    msg = models.CharField(verbose_name=(u'信息'), max_length=50, default='')
    times = models.CharField(verbose_name=(u'时间创建'), max_length=50, default='')
    version = models.CharField(verbose_name=(u'版本号'),max_length=50, default='')
    default = models.CharField(verbose_name=(u'默认'), max_length=50, default='')
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)
    # create_time = models.CharField(verbose_name=(u'创建时间'), max_length=50, default='')
    class Meta:
        ordering = ['-upload_time']
        verbose_name = u'dockerfile管理'
        verbose_name_plural = verbose_name



class dockerHost(models.Model):
    """
       dockerhost INFO LIST
    """
    names = models.CharField(u"nams", max_length=100, default='')
    hostname = models.CharField(u"主机名", max_length=100, default='')
    hostip = models.CharField(u"主机ip", max_length=100, default='')
    d_ps = models.CharField(u"容器数量", max_length=50, default='')
    d_im = models.CharField(u"镜像数量", max_length=50, default='')
    port = models.CharField(u"容器端口", max_length=50, default='')
    keep = models.CharField(u"连接状态", max_length=50, default='')
    connect_time = models.CharField(u"更新时间", max_length=50, default='')
    msg = models.TextField(u"备注信息", max_length=200, default='')
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.names
    class Meta:
        ordering = ['-upload_time']
        verbose_name = u'dockerhost'
        verbose_name_plural = verbose_name





class DockerStat(models.Model):
    """
       DockerStat INFO LIST

    """
    # host_info = models.ForeignKey(dockerHost, verbose_name=u"所有容器信息", on_delete=models.SET_NULL, null=True,
    #                                     blank=True)
    hostname = models.CharField(u"主机名", max_length=100, default='')
    hostip = models.CharField(u"主机ip", max_length=100, default='')
    name = models.CharField(verbose_name=(u'name'), max_length=100, default='')
    con_id = models.CharField(verbose_name=(u'con_id'), max_length=100, default='')
    image = models.CharField(verbose_name=(u'image'), max_length=100, default='')
    command = models.CharField(verbose_name=(u'command'), max_length=100, default='')
    create = models.CharField(verbose_name=(u'create'), max_length=100, default='')
    status = models.CharField(verbose_name=(u'status'), max_length=100, default='')
    port = models.CharField(verbose_name=(u'status'), max_length=100, default='')
    dname = models.CharField(verbose_name=(u'dname'), max_length=100, default='')
    default = models.CharField(verbose_name=(u'default'), max_length=100, default='')
    msg = models.CharField(verbose_name=(u'msg'), max_length=200, default='')
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)
    txt = models.TextField(u"txt", max_length=10000, blank=True)

    class Meta:
        ordering = ['-upload_time']
        verbose_name = u'DockerStat'
        verbose_name_plural = verbose_name





class dockerStats(models.Model):
    """
       docker stats info
    """
    hostname = models.CharField(u"主机名", max_length=100, default='')
    hostip = models.CharField(u"主机ip", max_length=100, default='')
    container = models.CharField(u"container", max_length=100, default='')
    cpu = models.CharField(u"cpu", max_length=100, default='')
    MemUL = models.CharField(u"内存使用", max_length=100, default='')
    Mem = models.CharField(u"内存百分比", max_length=50, default='')
    netIO = models.CharField(u"网络IO", max_length=50, default='')
    blockIO = models.CharField(u"块IO", max_length=50, default='')
    keep = models.CharField(u"连接状态", max_length=50, default='')
    connect_time = models.CharField(u"更新时间", max_length=50, default='')
    msg = models.TextField(u"备注信息", max_length=200, default='')
    default = models.TextField(u"default", max_length=200, default='')
    upload_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.names
    class Meta:
        ordering = ['-upload_time']
        verbose_name = u'dockerStats'
        verbose_name_plural = verbose_name




# def post_docker_stats():
#     try:
#         """
#         docker stats == cadvisor self create dashbord!!!
#         """
#         dcom_stats = "docker stats $(docker ps -a --format={{.Names}}) --no-stream"
#         P = Popen(dcom_stats, stdout=PIPE, shell=True)
#         stats = P.stdout.readlines()
#         del stats[0]
#         all_dic={}
#         all_datas=[]
#         for i in stats:
#             clean_stats=[]
#             stats_lis = i.split("   ")
#             while '' in stats_lis:
#                 stats_lis.remove('')
#             for sta in stats_lis:
#                 clean_stats.append(sta.strip())
#             all_datas.append(clean_stats)
#         print "post docker stats"
#         print json.dumps(all_datas)
#         return json.dumps(all_datas)
#     except Exception:
#         print traceback.format_exc()
    # post_data = json.dumps(all_datas)



