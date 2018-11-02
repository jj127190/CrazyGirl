#-*-coding:utf-8-*-

import os
import traceback
import socket
import json
import time
from pymongo import MongoClient
from django.http import HttpResponse
from django.shortcuts import render
import configparser as fg
from subprocess import Popen, PIPE
from cmdb.models import ASSET_STATUS,ASSET_TYPE
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_base_image(cata):
    try:
        with open(cata, "r") as f:
            ss = f.readlines()
            res = ss[0].split()[-1]
            maintainer = ss[1].split()[-1]
            base_image = res.split(":")[0]
            version = res.split(":")[-1]
            if maintainer:
                pass
            else:
                maintainer = ""
            if base_image:
                pass
            else:
                base_image = ""
            if version:
                pass
            else:
                version = ""
            dic={"base_image": base_image, "version": version, "maintainer": maintainer}
            return dic
    except Exception:
        print traceback.format_exc()

def page_split(all_datas,pages,nu=5):
    # all_datas = data.objects.all()
    paginator = Paginator(all_datas, nu)
    try:
        page = int(pages)
    except ValueError:
        page = 1
    try:
        all_data = paginator.page(page)
        return all_data,paginator
    except (EmptyPage, InvalidPage):
        all_data = paginator.page(paginator.num_pages)
        return all_data,paginator



def get_host_info():
    myname = socket.getfqdn(socket.gethostname())
    hostid = socket.gethostbyname(myname)
    return myname,hostid



def tran_code(str):
    """

    :param str:
    :return ZH:
    """
    return str.decode('unicode_escape')

def get_asset_tyst():
    asset_type = ASSET_TYPE
    asset_status = ASSET_STATUS
    all_status = []
    all_type = []
    for status in asset_status:
        all_status.append(status[1].encode("utf-8"))
    for type in asset_type:
        all_type.append(type[1].encode("utf-8"))
    return all_status, all_type


def get_for_col(m,mid,fm,fmid):
    pass
    # all_asset = []
    # for asset in m:
    #     print asset[mid]
    #     idc_id = asset[mid]
    #     asset[idc_id] = fm.objects.filter(id=idc_id).values()[0][fmid]
    #     all_asset.append(asset)
    # return all_asset

def page_list_return(total, current=1):

    min_page = current - 4 if current - 6 > 0 else 1
    max_page = min_page + 6 if min_page + 6 < total else total

    return range(min_page, max_page + 1)



def pages(post_objects, request):


    page_len = request.GET.get('page_len', '')
    if not page_len:
        page_len = 3
    paginator = Paginator(post_objects, page_len)
    try:
        current_page = int(request.GET.get('page', '1'))
    except ValueError:
        current_page = 1

    page_range = page_list_return(len(paginator.page_range), current_page)
    end_page = len(paginator.page_range)

    try:
        page_objects = paginator.page(current_page)
    except (EmptyPage, InvalidPage):
        page_objects = paginator.page(paginator.num_pages)

    if current_page >= 5:
        show_first = 1
    else:
        show_first = 0

    if current_page <= (len(paginator.page_range) - 3):
        show_end = 1
    else:
        show_end = 0

    # 所有对象， 分页器， 本页对象， 所有页码， 本页页码，是否显示第一页，是否显示最后一页
    return post_objects, paginator, page_objects, page_range, current_page, show_first, show_end, end_page



def dieAsset_info(request,Host,Idc):
    try:
        asset_id = request.POST.get("asset_id")
        hostname = request.POST.get('hostname', '')
        n_ip = request.POST.get('n_ip', '')
        w_ip = request.POST.get('w_ip', '')
        os = request.POST.get('os', '')
        cpu_type = request.POST.get('cpu_type', '')
        cpu_num = request.POST.get('cpu_num', '')
        mem = request.POST.get("mem", '')
        disk = request.POST.get("disk", '')
        asset_no = request.POST.get("asset_nu", '')
        asset_status = request.POST.get("asset_status", '').strip()
        asset_type = request.POST.get("asset_type", '').strip()
        sn = request.POST.get("sn", '')
        Manufacturer = request.POST.get("Manufacturer", '')
        idc = request.POST.get("idc", '')
        update_time = request.POST.get("update_time", '')
        msg = request.POST.get("msg")
        print "厂商"
        print Manufacturer
        print hostname,n_ip,w_ip,os,cpu_num,cpu_type,mem,disk,asset_no,asset_status,asset_type,sn,Manufacturer,idc,update_time,msg
        host = Host.objects.get(id = asset_id)
        host.hostname = hostname
        host.ip = n_ip
        host.other_ip = w_ip
        idc_ids = Idc.objects.filter(name=idc).values()[0]["id"]
        host.idc_id = idc_ids
        host.asset_no = asset_no
        host.asset_type = asset_type
        host.status = asset_status
        host.vendor = Manufacturer
        host.up_time = update_time
        host.cpu_model = asset_type
        host.cpu_num = cpu_num
        host.memory = mem
        host.disk = disk
        host.sn = sn
        host.memo = msg
        host.save()
        return 1
    except Exception:
        print traceback.format_exc()
        return traceback.format_exc()


def conn_mongo(collection):
    try:
        conn = MongoClient('127.0.0.1', 27017)
        db = conn["test"]
        all_data = []
        my_set = db[str(collection)]
        time_s = int(str(time.time()).split(".")[0]) - 3000
        time_e = int(str(time.time()).split(".")[0])
        ss = my_set.find({"time": {'$gt': time_s, '$lt': time_e}})
        return ss
    except Exception:
        print traceback.format_exc()


def get_mongoinfos(hostip,type):
    try:
        all_data=[]
        res = conn_mongo(hostip)
        for i in res:
            all_dic = {}
            all_dic["formatime"] = i["formatime"]
            if type =="disk":
                all_dic[type] = i[type][0]["percent"]
            else:
                all_dic[type] = i[type]["percent"]
            all_data.append(all_dic)
        k=[]
        v=[]
        ss={}
        for i in all_data:
            k.append(i["formatime"])
            v.append(i[type])
        ss["time"]=k
        ss[type] =v
        return HttpResponse(json.dumps(ss))
    except Exception:
        print traceback.format_exc()


def get_trac_inout(hostip):
    try:
        all_data = []
        res = conn_mongo(hostip)
        for i in res:
            print "123123123131312312312"
            print i
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

def curpwd():
    try:
        return os.getcwd()
    except Exception:
        return traceback.format_exc()

def jujfile(data):
    try:
        res = os.path.exists(data)
        return res
    except Exception:
        print traceback.format_exc()



