from django.http import HttpResponse
from django.shortcuts import render
from pymongo import MongoClient
import time
from cmdb.models import Host
from common.utils import get_mongoinfos,get_trac_inout
# from common.utils import get_mongo_infos
import traceback
import json
# Create your views here.


def info_show(request):
    if request.method == "GET":
        return render(request, "sys_info.html", locals())
    # return HttpResponse("123456")
    if request.method == "POST":
        hostip = request.POST.get("hostip")
        hostname = Host.objects.filter(ip=hostip).values()[0]["hostname"]
        print "hostip name$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        print hostip
        print hostname
        return render(request, "auto_get_type.html", locals())
def info_shows(request):
    try:
        conn = MongoClient('10.64.10.65', 27017)
        db = conn["test"]
        all_data = []
        my_set = db[str("10.64.10.65")]

        time_s = int(str(time.time()).split(".")[0]) - 3000
        time_e = int(str(time.time()).split(".")[0])
        ss = my_set.find({"time": {'$gt': time_s, '$lt': time_e}})

        for i in ss:
            all_dic = {}
            print "           "
            print i, type(i)
            all_dic["formatime"] = i["formatime"]
            all_dic["mem_p"] = i["mem"]["percent"]

            all_data.append(all_dic)
        print "ssssssssssssssssssssssss"

        k=[]
        v=[]
        ss={}
        for i in all_data:
            k.append(i["formatime"])
            v.append(i["mem_p"])


        ss["time"]=k
        ss["mem_p"] =v

        return HttpResponse(json.dumps(ss))
    except Exception:
        print traceback.format_exc()
    # return HttpResponse(ss)
    # return render(request, "sys_info.html", locals())
    # return HttpResponse("123456")

def get_disk(request):
    conn = MongoClient('10.64.10.65', 27017)
    db = conn["test"]
    all_data = []
    my_set = db[str("10.64.10.65")]
    # for i in my_set.find({"host"}):
    #     pass
    time_s = int(str(time.time()).split(".")[0]) - 3000
    time_e = int(str(time.time()).split(".")[0])
    ss = my_set.find({"time": {'$gt': time_s, '$lt': time_e}})
    # ss = my_set.find().limit(7)
    print "ssssssssssssssssssssssss"
    # print ss
    for i in ss:
        all_dic = {}

        all_dic["formatime"] = i["formatime"]
        all_dic["disk"] = i["disk"][0]["percent"]
        all_data.append(all_dic)
    print "ssssssssssssssssssssssss"

    k = []
    v = []
    ss = {}
    for i in all_data:
        k.append(i["formatime"])
        v.append(i["disk"])
    print "kkkkkkkkvvvvvvvv"

    ss["time"] = k
    ss["disk"] = v
    print "sss"

    print '========================================================================================'
    return HttpResponse(json.dumps(ss))



def get_cpu(request):
    conn = MongoClient('10.64.10.65', 27017)
    db = conn["test"]
    all_data = []
    my_set = db[str("10.64.10.65")]
    # for i in my_set.find({"host"}):
    #     pass
    time_s = int(str(time.time()).split(".")[0]) - 3000
    time_e = int(str(time.time()).split(".")[0])
    ss = my_set.find({"time": {'$gt': time_s, '$lt': time_e}})
    # ss = my_set.find().limit(7)
    print "ssssssssssssssssssssssss"
    # print ss
    for i in ss:
        all_dic = {}
        print "           "
        print i, type(i)
        all_dic["formatime"] = i["formatime"]
        all_dic["cpu"] = i["cpu"]["system"]
        all_data.append(all_dic)
    print "ssssssssssssssssssssssss"

    k = []
    v = []
    ss = {}
    for i in all_data:
        k.append(i["formatime"])
        v.append(i["cpu"])
    print "kkkkkkkkvvvvvvvv"

    ss["time"] = k
    ss["cpu"] = v
    print "sss"

    print '========================================================================================'
    return HttpResponse(json.dumps(ss))

def get_eth(request):
    try:
        conn = MongoClient('10.64.10.65', 27017)
        db = conn["test"]
        all_data = []
        my_set = db[str("10.64.10.65")]
        time_s = int(str(time.time()).split(".")[0]) - 3000
        time_e = int(str(time.time()).split(".")[0])
        ss = my_set.find({"time": {'$gt': time_s, '$lt': time_e}})
        for i in ss:
            all_dic = {}
            all_dic["formatime"] = i["formatime"]
            all_dic["ech0_in"] = i["net"][-1]["traffic_in"]
            all_dic["ech0_out"] = i["net"][-1]["traffic_out"]
            all_data.append(all_dic)
        k = []
        v = []
        ins = []
        out = []
        ss = {}
        for i in all_data:
            k.append(i["formatime"])
            ins.append(i["ech0_in"])
            out.append(i["ech0_out"])
        ss["time"] = k
        ss["traffic_in"] = ins
        ss["traffic_out"] = out
        return HttpResponse(json.dumps(ss))
    except Exception:
        print traceback.format_exc()



def mongo_typeinfos(request):
    print request.body
    hostip = request.POST.get("hostip")
    hostname = Host.objects.filter(ip=hostip).values()[0]["hostname"]
    return render(request,"auto_get_type.html",locals())



def info_type_mem(request):
    print "mem"
    print request.body
    print request.GET.get("hostip")
    hostip = request.GET.get("hostip")
    data = get_mongoinfos(hostip,"mem")
    print data
    return HttpResponse(data)

def info_type_disk(request):
    print "info_type_disk"
    print request.body
    print request.GET.get("hostip")
    hostip = request.GET.get("hostip")
    data = get_mongoinfos(hostip, "disk")
    print data
    return HttpResponse(data)


def info_type_cpu(request):
    print "info_type_cpu"
    print request.body
    print request.GET.get("hostip")
    hostip = request.GET.get("hostip")
    data = get_mongoinfos(hostip, "cpu")
    print data
    return HttpResponse(data)

def info_type_eth(request):
    print "info_type_eth"
    print request.body
    print request.GET.get("hostip")
    hostip = request.GET.get("hostip")
    data = get_trac_inout(hostip)
    print data
    return HttpResponse(data)


def info_test(request):

    return render(request,"sys_info1.html",locals())