#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import traceback
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from models import ASSET_STATUS,ASSET_TYPE,Host,Idc,HostGroup,alert_temp
from common.utils import tran_code,get_asset_tyst,pages,page_split,dieAsset_info,get_mongoinfos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_mongo_infos(request):
    print "=========="
    print request.body
    hostip = request.POST.get("hostip", "")
    hostname = request.POST.get("hostname","")
    print hostip, hostname
    return HttpResponse("这是走哪了")
    # return render(request, "/charts/auto_get_type.html", locals())
    # if hostip:
    #     mem = get_mongoinfos(hostip,"mem")
    #
    # else:
    #     if hostname:
    #         pass
    #     else:
    #         return HttpResponse("请输入准确值！")


def asset_edit(request):
    if request.method=="GET":
        print "get"
        print request.body
        host_id = request.GET.get("id")
        all_idc = Idc.objects.all()
        print host_id
        res = get_asset_tyst()
        all_status = res[0]
        all_type = res[1]
        host_info = Host.objects.get(id=host_id)
        return render(request, "asset_edit.html", locals())
    if request.method == "POST":
        res = dieAsset_info(request, Host, Idc)
        if res == 1:
            return redirect("/cmdb/asset_info")
        else:
            return HttpResponse(res)



def image_build(request):
    if request.method == "GET":
        print "测试呗，先这么着！！"
        return redirect("/docker/image_build")
        # return render(request,"image_build.html")
    if request.method == "POST":
        print "测试呗，先这么着！！"
        return redirect("/docker/image_build")


def asset_info(request):
    if request.method == "GET":
        try:
            res = get_asset_tyst()
            all_status = res[0]
            all_type = res[1]
            assets_info = Host.objects.all()
            paginator = Paginator(assets_info, 5)
            page = request.GET.get('page', '1')
            currentPage = int(page)
            try:
                print(page)
                assets_infos = paginator.page(page)  # 获取当前页码的记录
            except PageNotAnInteger:
                assets_infos = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
            except EmptyPage:
                assets_infos = paginator.page(paginator.num_pages)
            return render(request, "index.html", locals())
        except Exception:
            print traceback.format_exc()

    if request.method == "POST":
            pass


def asset_add(request):

    if request.method == "GET":
        res = get_asset_tyst()
        all_status = res[0]
        all_type = res[1]
        all_idc = Idc.objects.all()
        print "all_status all_type "
        print all_status,type(all_status)
        print "========"
        print all_type,type(all_type)
        # assets_list, p, assets, page_range, current_page, show_first, show_end, end_page = pages(all_idc, request)
        return render(request,"asset_add_info.html",locals())
    try:
        if request.method == "POST":
            print "=========="
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
            print "Manufacturer"
            print Manufacturer
            print hostname,n_ip,w_ip,os,cpu_num,cpu_type,mem,disk,asset_no,asset_status,asset_type,sn,Manufacturer,idc,update_time,msg
            host = Host()
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
            host.cpu_model = cpu_type
            host.cpu_num = cpu_num
            host.memory = mem
            host.disk = disk
            host.sn = sn
            host.os = os
            host.memo = msg
            host.save()
            return redirect("/cmdb/asset_info")
            # return HttpResponse("ok")
    except Exception:
        print traceback.format_exc()
        return HttpResponse(traceback.format_exc())

        # return redirect("/cmdb/ass_info")


def asset_del(request):
    if request.method == 'POST':
        try:
            del_id = request.POST.get("asset_id")
            print "del_id"
            print del_id
            if del_id:
                Host.objects.filter(id=del_id).delete()
                return redirect("/cmdb/asset_info")
        except Exception:
            print traceback.format_exc()
    if request.method == 'GET':
        del_id = request.GET.get("id")
        return render(request, "asset_del.html", locals())



def asset_show(request):
    host_id = request.GET.get("id")
    all_idc = Idc.objects.all()
    print host_id
    res = get_asset_tyst()
    all_status = res[0]
    all_type = res[1]
    host_info = Host.objects.get(id=host_id)
    return render(request, "asset_show.html", locals())


def idc_info(request):
    if request.method == "GET":
        try:
            idc_infos = Idc.objects.all()
            return render(request, "idc_show.html", locals())
        except Exception:
            print traceback.format_exc()
            return HttpResponse(traceback.format_exc())
    if request.method == "POST":
        pass






def idc_add(request):
    if request.method == "POST":
        try:
            idc_name = request.POST.get("idc_name","")
            idc_tag = request.POST.get("idc_tag", "")
            idc_add = request.POST.get("idc_add", "")
            idc_tel = request.POST.get("idc_tel", "")
            idc_pic = request.POST.get("idc_pic", "")
            idc_mph = request.POST.get("idc_mph", "")
            idc_tan = request.POST.get("idc_tan", "")
            idc_ip_range = request.POST.get("idc_ip_range", "")
            idc_net = request.POST.get("idc_net", "")
            idc_msg = request.POST.get("idc_msg", "")
            idc_info = Idc()
            idc_info.name = idc_name
            idc_info.ids = int(idc_tag)
            idc_info.address = idc_add
            idc_info.tel = idc_tel
            idc_info.contact = idc_pic
            idc_info.contact_phone = idc_mph
            idc_info.jigui = idc_tan
            idc_info.ip_range = idc_ip_range
            idc_info.bandwidth = idc_net
            idc_info.memo = idc_msg
            idc_info.save()
            return redirect("/cmdb/idc_info")
        except Exception:
            print traceback.format_exc()
            return HttpResponse(traceback.format_exc())
        # idc_info.name = idc_name

    if request.method == "GET":
        return render(request, "idc_add.html")




#form 表单的不同提交形式 //  2018/6/4-16:53
def idc_cancel(request):
    return redirect("/cmdb/idc_info")


def group_connect(request):
    groups = HostGroup.objects.all()
    ip_nu = HostGroup.objects.filter().values("txt")
    print "======="
    print ip_nu
    return render(request, "group_connect.html",locals())


def group_add(request):
    if request.method=="GET":
        host_ip = Host.objects.filter().values("ip","hostname")
        print  "host_ip"
        print host_ip,type(host_ip)
        return render(request, "group_add.html", locals())
    if request.method=="POST":
        print "group add infos=========="
        print request.method

def ajax_tran_data(request):
    try:
        print "zaizhe---"
        group_name = request.POST.get("group_name")
        desc = request.POST.get("des")
        selectedValues = request.POST.get("selectedValues")
        # try:
        HG = HostGroup()
        HG.name= group_name
        HG.desc = desc
        HG.txt = selectedValues.replace("-" , "; ")

        HG.save()
        # print "selectedValuesssssssssssssssssssssss"
        # print selectedValues
        # serlist = selectedValues.split("-")
        # print "serlist============================"
        # print serlist
        # for li in serlist:
        #     host = Host.objects.get(ip=li)
        #     HG.serverList.add(host)
        #     HG.save()

        # except Exception:

        print "group_name", group_name

        print "desc", desc
        data = request.body
        print "data----------------------------------"
        print data
        return  HttpResponse("操作成功！")
        # all=[]
        # thel=[]
        # all = data.split("=")
        # print "all----------------------------------"
        # print all
        # del all[0]
        # del all[-1]
        # for i in all:
        #     thel.append(''.join(i.split("&")[0]).split("%2C"))
        # print thel
        # print type(thel)
        # if thel and len(thel)>0:
        #     for i in thel:
        #         if ''.join(i).replace("." ,"").isdigit():
        #             pass
        #         else:
        #             # return HttpResponse("数据:{0}传输不正确,请重新传输或上服务器查看！".format(thel))
        #             return HttpResponse("数据:{0}传输不正确,请重新传输或上服务器查看！".format(thel))
        #     return HttpResponse("1")
        # else:
        #     return HttpResponse("数据:{0}传输不正确,请重新传输或上服务器查看！".format(thel))


    except Exception:
        print traceback.format_exc()
        return HttpResponse("操作失败，数据:{0}传输不正确,请重新传输或上服务器查看！".format(traceback.format_exc()))


def idc_show(request):
    try:
        print "11111111111111111"
        print request.body
        idcn = request.GET.get("idcn")
        print idcn
        print "222222222222222222221"
        idc_info = Idc.objects.get(name=idcn)
        return render(request, "idc_shows.html", locals())
    except Exception:
        print traceback.format_exc()


def idc_edit(request):
    if request.method == "GET":
        try:
            idc_id = request.GET.get("id")
            idc_info = Idc.objects.get(id=idc_id)
            return render(request, "idc_edit.html",locals())
        except Exception:
            print traceback.format_exc()
    if request.method == "POST":
        try:

            id = request.POST.get("id")
            name = request.POST.get("name")
            address = request.POST.get("address")
            tel = request.POST.get("tel")
            contact = request.POST.get("contact")
            contact_phone = request.POST.get("contact_phone")
            jigui = request.POST.get("jigui")
            ip_range = request.POST.get("ip_range")
            bandwidth = request.POST.get("bandwidth")
            memo = request.POST.get("memo")
            print id,name,address,tel,contact_phone,contact,jigui,ip_range,bandwidth,memo
            idc_info = Idc.objects.get(id=id)
            idc_info.name = name
            idc_info.address = address
            idc_info.tel = tel
            idc_info.contact = contact
            idc_info.contact_phone = contact_phone
            idc_info.jigui = jigui
            idc_info.ip_range = ip_range
            idc_info.bandwidth = bandwidth
            idc_info.memo = memo
            idc_info.save()
            return redirect("/cmdb/idc_info")
        except Exception:
            print traceback.format_exc()
            return HttpResponse(traceback.format_exc())

def idc_del(request):
    if request.method == "GET":
        print "==================="
        id = request.GET.get("id")
        print id
        return render(request, "idc_del.html", locals())
    # Idc.objects.get(id=id).delete()
    if request.method == "POST":
        try:
            id = request.POST.get("idc_id")
            # print "idshi1111111111"
            # print id,len(id)
            print "request.body"
            print request.body
            try:
                if len(id) > 0:
                    Idc.objects.filter(id=id).delete()
                    return redirect("/cmdb/idc_info")
                else:
                    return HttpResponse("操作失败，请重新操作！")
            except Exception:
                print traceback.format_exc()
                return HttpResponse("操作失败！原因:{0}".format(traceback.format_exc()))
        except Exception:
            return HttpResponse(traceback.format_exc())
            print traceback.format_exc()
def idc_dels(request):
    print "request body"
    print request.body

def group_edit(request):
    try:
        print "-------------"
        id = request.GET.get("id")
        print "id",id
        txt = HostGroup.objects.filter(id=id).values("txt")[0]["txt"]
        group_name = HostGroup.objects.filter(id=id).values("name")[0]["name"]
        group_desc = HostGroup.objects.filter(id=id).values("desc")[0]["desc"]
        group = txt.split(";")
        all_ips = Host.objects.filter().values("ip")
        allip=[]
        for i in all_ips:
            allip.append(i["ip"])

        print "111"
        print allip, type(allip)
        print "111"
        print "2222"
        print group,type(group)
        print "22"
        print "22"
        print set(allip)
        print set(group)
        print "333"
        ssss = set(allip) - set(group)
        print set(allip)-set(group)
        print ssss,type(ssss)
        print "444"
        print list(ssss)
        print id, group_name, group_desc, txt
        shy = list(ssss)
        return render(request, "group_edit.html", locals())
    except Exception:
        print traceback.format_exc()

    # print "id====="
    # print id
    # # group=[]
    # groupIp = HostGroup.objects.filter(id=id).values("txt")
    # group = groupIp.split(";")

def ajax_change_group(request):
    if request.method == "POST":
        print "request.body"
        print request.body
        try:
            group_name = request.POST.get("group_name","default")
            desc = request.POST.get("desc","default")
            id = request.POST.get("id","default")
            selectedValues = request.POST.get("selectedValues", "null")
            group = HostGroup.objects.get(id=id)
            group.name=group_name
            group.desc = desc
            group.txt = selectedValues.replace("-", ";")
            group.save()
            return HttpResponse("1")
        except Exception:
            print traceback.format_exc()
            return HttpResponse("操作失败，请上服务器查看！失败原因{0}".format(traceback.format_exc()))
            # print traceback.format_exc()

def group_del(request):
    if request.method == "POST":
        id = request.POST.get("group_id")
        print "host id",id
        try:
            HostGroup.objects.filter(id=id).delete()
            return  redirect("/cmdb/group_connect")
        except Exception:
            print traceback.format_exc()
            return HttpResponse(traceback.format_exc())
    if request.method == "GET":
        del_id = request.GET.get("id")
        print "get id",del_id
        return render(request, "group_del.html", locals())
        # id = HostGroup.objects

def wechat(request):
    return render(request, "wechat.html")
def alert_tem(request):
    return render(request, "alert_temp.html")
import time
def create_alertTS(request):
    data=[]
    res={}
    res1 = {}
    res1["alert_temp"] = "测试报警模板111"
    res1["create_time"] = "0101111"
    res1["create_user"] = "王静111"
    res1["des"] = "这是测试123111"
    res1["defaults"] = "默认123111"


    res["alert_temp"]= "测试报警模板"
    res["create_time"] = "0101"
    res["create_user"] = "王静"
    res["des"] = "这是测试123"
    res["defaults"] = "默认123"
    data.append(res)
    data.append(res1)
    print "datassssssss"
    print data
    time.sleep(2)
    return HttpResponse(json.dumps(data))

def create_alertTSs(request):
    if request.method == "GET":
        print "---------"
        print request.body
        print "2-----------"
        mem = request.POST.get("mem")
        df = request.POST.get("df")
        io = request.POST.get("io")
        upload = request.POST.get("upload")
        tins = request.POST.get("in")
        tout = request.POST.get("out")
        port = request.POST.get("port")

        print mem,df,io,upload,tins,tout,port
        # alert_temp.objects.filter().values()
        data={}
        dd =[]
        data["alert_tem"]="test"
        data["alert_create"] = "now"
        data["alert_user"] = "wangjing"
        data["des"] = "测试222"
        data["default"] = "默认222"
        data["alert_tem"] = "test"
        data["alert_tem"] = "test"
        print data
        dd.append(data)
        # dd = json.dumps(dd)
        print dd
        return render(request,"alert_temp.html",locals())
        return HttpResponse(dd)
    if request.method == "POST":
        try:
            print "---------"
            print request.body
            print "2-----------"
            mem = request.POST.get("mem")
            df = request.POST.get("df")
            io = request.POST.get("io")
            upload = request.POST.get("upload")
            tins = request.POST.get("in")
            tout = request.POST.get("out")
            port = request.POST.get("port")

            print mem,df,io,upload,tins,tout,port
            # alert_temp.objects.filter().values()
            data={}
            dd =[]
            data["alert_tem"]="test"
            data["alert_create"] = "now"
            data["alert_user"] = "wangjing"
            data["des"] = "测试222"
            data["default"] = "默认222"
            data["alert_tem"] = "test"
            data["alert_tem"] = "test"
            print data
            dd.append(data)
            # dd = json.dumps(dd)
            print dd
        # return render(request,"alert_tem.html",locals())
            return HttpResponse(json.dumps(dd))
        except Exception:
            print traceback.format_exc()

def dingding_man(request):
    return render(request,"dingding_man.html")

def wac_man(request):
    return render(request,"wechat_manage.html")


def wechat_man(request):
    try:
        return render(request, "wechat_manage.html")
    except Exception:
        print traceback.format_exc()