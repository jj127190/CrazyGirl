#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import traceback
from django.http import HttpResponse
# from CrazyGril import tasks
from .tasks import run_test_suit,mk,seleid,selegroup,idse,segroup,idsecq,uf
# from celery.five import python_2_unicode_compatible
# from celery import five
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from docker.models import dockerHost,DockerStat,dockerStats
from common.get_mongo import *
import time
import os
from common.utils import curpwd,jujfile
from cmdb.models import Host
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from cmdb.models import HostGroup,Idc

def upf(request):

    return render(request,"upf.html",locals())
def tun_upf(request):
    try:
        uploadf = request.FILES.get("uploadf")
        shell = curpwd() + "/upFileShell"
        res = jujfile(shell)
        if res:
            pass
        else:
            os.mkdir(shell)
        filename = shell + "/" + str(uploadf)
        print "=============="
        print filename
        with open(filename, "wb+") as f:
            for chunk in uploadf.chunks():
                f.write(chunk)
        # return HttpResponse("32")
        return render(request,"shell_add.html",locals())
    except Exception:
        print traceback.format_exc()



@csrf_exempt
def ajax_upload(request):
    try:
        ac_name = request.POST.get("ac_name", "")
        uploadf = request.FILES.get("uploadf")
        shell = curpwd() + "/upFileShell"
        res = jujfile(shell)
        if res:
            pass
        else:
            os.mkdir(shell)
        filename = shell + "/" + ac_name
        print "=============="
        print filename
        with open(filename, "wb+") as f:
            for chunk in uploadf.chunks():
                f.write(chunk)
        return HttpResponse("32")
    except Exception:
        print traceback.format_exc()

@csrf_exempt
def because_accres(request):
    try:
        print "because_accres"
        print request.body
        option = request.POST.get("sele", "")
        selectip = request.POST.get("selectip", "")
        rag = request.POST.get("rag", "")
        shell_command = request.POST.get("shell_command", "")
        uploadf = request.FILES.get("uploadf")
        ac_name = request.POST.get("ac_name","")
        print "名称===="
        print ac_name,option,selectip,rag,shell_command,ac_name,uploadf
        if uploadf:
            shell = curpwd() + "/upFileShell"
            res = jujfile(shell)
            if res:
                pass
            else:
                os.mkdir(shell)
            filename = shell + "/" + str(uploadf)
            print "=============="
            print filename
            with open(filename, "wb+") as f:
                for chunk in uploadf.chunks():
                    f.write(chunk)
        if selectip and uploadf:
            print "在这"
            print "/data/" + str(uploadf)
            # selectip, shell_command, copy_command, q_command, name
            copy_command = "src=/cg/cg/CrazyGril/upFileShell/{0} dest=/data/  mode=0755".format(str(uploadf))
            q_command = "/data/" + str(uploadf)
            print "############################################################"
            print q_command
            print "q_command"
            idsecq.delay(selectip,shell_command,copy_command,q_command,ac_name)
            return redirect("/task/shell_add")


        if uploadf:
            copy_command = "src=/cg/cg/CrazyGril/upFileShell/{0} dest=/data/  mode=0755".format(str(uploadf))
            q_command = "/data/" + str(uploadf)
            uf.delay(selectip,shell_command,copy_command,q_command,ac_name)
            return redirect("/task/shell_add")


        if selectip:
            print "this is selectip=========="
            print selectip, shell_command
            res = idse.delay(selectip, shell_command,ac_name)
            if res.successful():
                print "this task is success"
            return redirect("/task/show_tasks")
            # return render(request, "show_tasks.html", locals())
            # return HttpResponse(res)
        else:
           if option == "机房":
               idss = []
               res = Idc.objects.filter(name=rag).values()[0]["id"]
               hh = Host.objects.filter(idc_id=res).values()
               for i in hh:
                   idss.append(i["ip"].encode('raw_unicode_escape'))
               print idss, type(idss)
               res = segroup.delay(idss, shell_command)
               return HttpResponse("option")
           if option == "组":
               idss = []
               res = Idc.objects.filter(name=rag).values()[0]["id"]
               hh = Host.objects.filter(idc_id=res).values()
               for i in hh:
                   idss.append(i["ip"].encode('raw_unicode_escape'))
               print idss, type(idss)
               res = segroup.delay(idss, shell_command)
               return HttpResponse("option")

    except Exception:
        print traceback.format_exc()





def shell_add(request):
    group = HostGroup.objects.all()
    idc = Idc.objects.all()
    # return render(request, "shell_add.html", locals())
    return render(request, "shell_add1.html",locals())

def shell_exe(request):
    try:
        option =request.POST.get("sele","")
        selectip=request.POST.get("selectip","")
        rag = request.POST.get("rag","")
        shell_command=request.POST.get("shell_command","")
        upload_sh=request.POST.get("upload_sh","")
        msg=request.POST.get("msg","")
        if selectip:
            print selectip,shell_command,upload_sh,msg
            seleid.delay(selectip,shell_command)
            return HttpResponse("selectip cancel!")
        else:
            selegroup.delay(option,rag,shell_command,upload_sh,msg)
            print  option,rag,shell_command,upload_sh,msg
            return HttpResponse("option cancel!")
    except Exception:
        print traceback.format_exc()

def ajax_get_range(request):
    try:
        print "request.body ajax"
        print request.body
        types = request.POST.get("range")
        if types == "1":
            return HttpResponse("1")
        if types == "2":
            idc = Idc.objects.all().values()
            print "idc", idc
            all_gn = []
            for i in idc:
                all_gn.append(i["name"])
            print "all_gn"
            print all_gn, type(all_gn)
            print json.dumps(all_gn)
            return HttpResponse(json.dumps(all_gn))
        if types == "3":
            group = HostGroup.objects.all().values()
            print "group",group
            all_gn = []
            for i in group:
                all_gn.append(i["name"])
            print "all_gn"
            print all_gn,type(all_gn)
            print json.dumps(all_gn)
            return HttpResponse(json.dumps(all_gn))
        if types == "default":
            print "here default!!!"
            return HttpResponse("default")
    except Exception:
        print traceback.format_exc()
    # return HttpResponse("rehi")


def testmk(request):
    print "开始创建文件夹"
    result = mk.delay()
    print result,type(result)
    return HttpResponse("异步五秒")

def tasks(request):
    print('before run_test_suit')
    result = run_test_suit.delay('110')
    print('after run_test_suit')
    return HttpResponse("job is runing background~")



from django_celery_results.models import TaskResult
def show_tasks(request):
    return render(request,"show_tasks.html")




def ajax_show_tasks(request):
    try:
        res = TaskResult.objects.all().values()
        print "sssss"
        print res
        re= []
        for i  in res:
            print i["date_done"]
            print type(i["date_done"])
            result ={}
            result["status"] = i["status"]
            result["date_done"] = "2017"
            result["traceback"] = i["traceback"]
            result["result"] = i["result"]
            result["content_type"] = i["content_type"]
            result["content_encoding"] = i["content_encoding"]
            result["task_id"] = i["task_id"]

            re.append(result)
            print "rrrrrrr"
            print re
        return HttpResponse(json.dumps(re))
    except Exception:
        print traceback.format_exc()
def ansible_show(request):
    return render(request,"ansible_add.html",locals())