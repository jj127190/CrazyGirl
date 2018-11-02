#-*- coding:utf-8 -*-
import json
import traceback
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from docker.models import dockerHost,DockerStat,dockerStats
from common.get_mongo import *
import time
import os
from cmdb.models import Host
# Create your views here.
@csrf_exempt
def auto_git(request):
    try:
        print "request body auto git pull"
        # print request.body
        print "============="
        print  type(request.body)
        res = request.body
        data = json.loads(res)
        if data["object_kind"] == "push":
            print "拉取"
            os.popen("cd /crazyGril/server/cg/CrazyGril && git pull")
        else:
            print "什么鬼,应该会自动重启吧！！"
        print "11111111111111"
    except Exception:
        print traceback.format_exc()




@csrf_exempt
def auto_git2(request):
    try:
        print "request body auto git pull"
        # print request.body
        print "============="
        print  type(request.body)
        res = request.body
        data = json.loads(res)
        if data["object_kind"] == "push":
            print "拉取"
            os.popen("cd /cg/cg/CrazyGril && git pull")
        else:
            print "什么鬼,应该会自动重启吧！！"
        print "11111111111111"
    except Exception:
        print traceback.format_exc()

@csrf_exempt
def get_asset_info(request):
    # try:
        if request.method == "POST":

            # print request.body
            data = json.loads(request.body)
            # print data, type(data)
            hostname = data["hostname"]
            ip = data["ip"]
            os = data["osver"]
            vendor = data["vendor"]
            cpu_model = data["cpu_model"]
            cpu_num = data["cpu_num"]
            memory = data["memory"]
            disk = data["disk"]
            disk = disk.replace("B']", "").split(":")[-1].strip()
            sn = data["sn"]
            sta = data["status"]
            # print sta
            print "单个 数据"
            # print hostname, ip, os, vendor, cpu_num, cpu_model, memory, disk, sn
            try:
                asset_info = Host.objects.get(hostname=hostname, ip=ip)
                sys_infos = Host.objects.filter(hostname=hostname, ip=ip).values()
                # print asset_info,type(asset_info)
                print "get_asset_info-----------------------"
                # print sys_infos,type(sys_infos)
            except Exception:
                asset_info = Host()
                print traceback.format_exc()

            asset_info.hostname = hostname
            asset_info.ip = ip
            asset_info.os = os
            asset_info.vendor = vendor
            asset_info.cpu_model = cpu_model
            asset_info.cpu_num = cpu_num
            asset_info.memory = memory
            asset_info.disk = disk
            asset_info.sn = sn
            asset_info.status = "使用中"
            asset_info.save()
            print "数据写进去了。。。。。。。。。。"
            # print traceback.format_exc()
            return HttpResponse("更新数据")
        # print traceback.format_exc()

@csrf_exempt
def get_dockerInfo(request):
    try:
        times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print "=================>>>>>"
        # print request.body
        datas = request.body
        print datas,type(datas)
        da = json.loads(datas)
        hostname = da[0]["hostname"]
        ip = da[0]["hostip"]
        d_ps = da[0]["d_ps"]
        d_im = da[0]["d_im"]
        for i in da:
            del i["hostname"]
            del i["hostip"]
            del i["d_ps"]
            del i["d_im"]
        get_data = json.dumps(da)
        print "get_data================================================ssssssssssssssss"
        print get_data
        print "=================>>>>>"
        # print request.body.split("*")
        # data = request.body.split("*")[0]
        # hostname = json.loads(request.body.split("*")[1])["hostname"]
        # ip = json.loads(request.body.split("*")[1])["ip"]
        # d_ps = json.loads(request.body.split("*")[2])["d_ps"]
        # d_im = json.loads(request.body.split("*")[2])["d_im"]
        # print hostname,type(hostname),ip,type(ip),d_ps,type(d_ps),d_im,type(d_im)
        try:
            ds = dockerHost.objects.get(hostname=hostname, hostip=ip)
        except Exception:
            ds = dockerHost()
        ds.hostname = hostname
        ds.hostip = ip
        ds.d_ps = str(d_ps)
        ds.d_im = str(d_im)
        ds.connect_time = times
        ds.keep = "1"
        ds.save()
        print "hhsss"
        # print data,type(data)
        try:
            res = DockerStat.objects.get(hostip=ip)
        except Exception:
            res = DockerStat()
        res.hostip=ip
        res.txt = get_data
        res.save()
        return redirect("docker/show_con")
    except Exception:
        # ds.keep = "2"
        print traceback.format_exc()
        return HttpResponse(traceback.format_exc())


@csrf_exempt
def test(request):
    conn = MongoClient('127.0.0.1', 27017)
    db = conn["test"]
    all_data = []
    my_set = db[str("10.64.10.65")]
    time_s = int(str(time.time()).split(".")[0]) - 300
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
    # print all_data

    k=[]
    v=[]
    for i in all_data:
        k.append(i["formatime"])
        v.append(i["mem_p"])
    print "k,v==="
    print k,v
    ss={}
    ss["time"] = k
    ss["mem_p"] = v

    print "ssss"
    # print ss
    return HttpResponse(json.dumps(ss))

from pymongo import MongoClient


@csrf_exempt
def get_sysInfo(request):
    try:
        if request.method == "GET":
            conn = MongoClient('127.0.0.1', 27017)
            db = conn["test"]

            all_data=[]

            my_set = db[str("10.64.10.65")]
            # for i in my_set.find({"host"}):
            #     pass
            time_s = int(str(time.time()).split(".")[0]) - 300
            time_e = int(str(time.time()).split(".")[0])
            ss = my_set.find({"time":{ '$gt': time_s, '$lt': time_e }})
            print "ssssssssssssssssssssssss"
            # print ss
            for i in  ss:
                all_dic = {}
                print "           "
                print i,type(i)
                all_dic["formatime"] = i["formatime"]
                all_dic["mem_p"] = i["mem"]["percent"]
                all_data.append(all_dic)
            print "ssssssssssssssssssssssss"
            print all_data
            return HttpResponse(ss)
        if request.method == "POST":
            try:
                print "get_sysInfo=========================="
                print request.body,type(request.body)
                data = json.loads(request.body)
                print "data"
                print data,type(data)
                timeS = int(str(time.time()).split(".")[0])
                hostid = data["hostid"]
                hostname = data["hostname"]
                data["time"] = timeS
                # data["formatime"] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).split(" ")[-1][-3])
                data["formatime"] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())).split(" ")[-1][:-3]
                print "++++++++++++++++++++++++++++++++++"
                print data
                print "开始插入数据"
                mongodb = "test"
                conn = MongoClient('127.0.0.1', 27017)
                db = conn["test"]
                my_set = db[str(data["hostid"])]
                ss = my_set.insert_one(data).inserted_id
                print  "ss",ss
                print "++++++++++++++++++++++++++++++++++"
            except Exception:
                print traceback.format_exc()




            # Host =Host.objects.get()

    except Exception:
        print traceback.format_exc()



@csrf_exempt
def get_dockerStats(request):
    try:
        print "request get dopcker stats"
        print type(request.body)
        print request.body
        hostinfo = request.body.split("*")[-1]
        hostname = json.loads(hostinfo)["hostname"]
        ip = json.loads(hostinfo)["ip"]
        stats = json.loads(request.body.split("*")[0])
        try:
            dockerStats.objects.filter(hostip=ip).delete()
        except Exception:
            print "please ignore!! this is a normal function!!---------------"
        for i in stats:
            stats = dockerStats()
            stats.hostip = ip
            stats.hostname = hostname
            stats.container = i[0]
            stats.cpu = i[1]
            stats.MemUL = i[2]
            stats.Mem = i[3]
            stats.netIO = i[4]
            stats.blockIO = i[5]
            stats.save()
        return HttpResponse("docker stats info show")
    except Exception:
        print traceback.format_exc()