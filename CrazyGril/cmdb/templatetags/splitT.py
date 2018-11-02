#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from cmdb.models import HostGroup, Host
from django import template
import json

register = template.Library()
@register.filter
def split(data):
    print data,type(data)
    print len(data.split(";"))
    return len(data.split(";"))

@register.filter
def get_res(id):
    ip = Host.objects.filter(id=id).values()[0]["ip"]
    print "11111111111111111111"
    print ip
    groups = []
    res = HostGroup.objects.filter().values()
    for i in res:
        if ip in i["txt"]:
            groups.append(i["name"])
    print "groups"
    print str(groups).decode('unicode_escape')
    return str(groups).decode('unicode_escape').replace("[u", "").replace("]", "").replace("u", "").replace("\'","")


@register.filter
def rejson(data):
    data = json.dumps(data)
    return data
