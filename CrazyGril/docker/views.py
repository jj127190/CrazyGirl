#-*- coding:utf-8 -*-
import json
import logging
import traceback
import datetime
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.shortcuts import render
from docker.models import dockerfiles,dockerHost,DockerStat,dockerStats
from common.get_all_images import get_images,build_image,del_image
from common.get_init_catalog import get_init_names,get_dockerfile_info
from common.utils import get_base_image,page_split,get_host_info
from common.change_image_info import image_change_vt
# from models import dockerStats
import configparser as fg
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
import time
import os

# Create your views here.

def image_delete(request):
    if request.method == "POST":
        try:
            print request.body
            imagede = request.POST.get("imagede")
            delidimage = imagede.encode("utf-8")
            imageid = delidimage.split(" ")[0].strip()
            image_na = dockerfiles.objects.filter(id=imageid).values()
            name = image_na[0]["newimage"]
            print "image_na,name"
            print image_na,name
            dockerfiles.objects.filter(id=imageid).delete()
            del_image(name)
            return redirect('/docker/image_build')
        except Exception:
            print traceback.format_exc()
            return traceback.format_exc()
    if request.method == "GET":
        try:
            imagede = request.GET.get("imagede")
            delidimage = imagede.encode("utf-8")
            imageid = delidimage.split(" ")[0].strip()
            return render(request, "confirm_del.html",locals())
        except Exception:
            print traceback.format_exc()
            return HttpResponse(traceback.format_exc())

def search_build_image(request):

    if request.method == "POST":
        print request.body
        maintainer = request.POST.get("maintainer").strip()
        version = request.POST.get("version").strip()
        newimage = request.POST.get("newimage").strip()
        # print maintainer,version,newimage
        print "maintainer:" + maintainer
        print "version:" + version
        print "newimage:" + newimage
        import socket
        # myname = socket.getfqdn(socket.gethostname())
        # myaddr = socket.gethostbyname(myname)
        # print myname
        # print myaddr
        if maintainer and not version and not newimage:
            maintainer = maintainer
            all_data = dockerfiles.objects.filter(maintainer__icontains=maintainer).values()
            print all_data

            ########
            pages = '1'
            data = page_split(all_data, pages, nu=4)
            all_data = data[0]
            paginator = data[1]
            ########
            res = get_host_info()
            hostip = res[1]
            return render(request,"image_build.html",locals())
            # return HttpResponse()
        if not maintainer and  version and not newimage:
            version=version
            all_data = dockerfiles.objects.filter(version__icontains=version).values()
            print all_data

            ########
            pages = '1'
            data = page_split(all_data, pages, nu=4)
            all_data = data[0]
            paginator = data[1]
            ########
            res = get_host_info()
            hostip = res[1]
            return render(request, "image_build.html", locals())
        if not maintainer and  not version and  newimage:
            newimage=newimage
            all_data = dockerfiles.objects.filter(newimage__icontains=newimage).values()
            print all_data

            ########
            pages = '1'
            data = page_split(all_data, pages, nu=4)
            all_data = data[0]
            paginator = data[1]
            ########
            res = get_host_info()
            hostip = res[1]
            return render(request, "image_build.html", locals())
        if  maintainer and  version and not newimage:
            maintainer=maintainer
            version=version
            all_data = dockerfiles.objects.filter(newimage__icontains=newimage,version__icontains=version).values()
            print all_data
            ########
            pages = '1'
            data = page_split(all_data, pages, nu=4)
            all_data = data[0]
            paginator = data[1]
            ########
            res = get_host_info()
            hostip = res[1]
            return render(request, "image_build.html", locals())
        if not  maintainer and  version and  newimage:
            version = version
            newimage=newimage
            all_data = dockerfiles.objects.filter(maintainer__icontains=maintainer,version__icontains=version).values()
            print all_data
            ########
            pages = '1'
            data = page_split(all_data, pages, nu=4)
            all_data = data[0]
            paginator = data[1]
            ########
            res = get_host_info()
            hostip = res[1]
            return render(request, "image_build.html", locals())
        if maintainer and version and newimage:
            all_data = dockerfiles.objects.filter(version__icontains=version, maintainer__icontains=maintainer, newimage__icontains=newimage).values()
            version = version
            newimage = newimage
            maintainer =maintainer
            ########
            pages = '1'
            data = page_split(all_data, pages, nu=4)
            all_data = data[0]
            paginator = data[1]
            ########
            res = get_host_info()
            hostip = res[1]
            return render(request, "image_build.html", locals())
        if  not maintainer and not version and not newimage:
            print "在这吗？"
            all_data = dockerfiles.objects.all().values()
            print "all_data"
            print all_data
            ########
            pages = '1'
            data = page_split(all_data, pages, nu=4)
            all_data = data[0]
            paginator = data[1]
            ########
            res = get_host_info()
            hostip = res[1]
            return render(request, "image_build.html", locals())

    if request.method == "GET":
        print "GET------------------"
        dockerfile = dockerfiles.objects.all().values()
        res = get_host_info()
        hostip = res[1]
        return render(request, "image_build.html", locals())



def build_add(request):
    try:
        if request.method == "GET":
            command = "docker images"
            dic={}
            lis=[]
            images = get_images(command)
            nu = 0
            for i in images:
                dic[nu]= i
                nu = nu + 1
            print "========="
            print dic

            requestuser = request.user.username

            return render(request, "image_build_add.html",locals())
        if request.method == "POST":

            return render(request, "image_build_add.html")
    except Exception:
        print traceback.format_exc()




def image_create_add(request):
    if request.method == "GET":
        return  HttpResponse("get 形式！")
    if request.method == "POST":
        try:
            print "====================="
            print request.body
            # images = request.POST.get("images")
            requestUser = request.user.username
            base_image = request.POST.get("images")
            maintainer = request.POST.get("user", requestUser)
            version = request.POST.get("version", "latest")
            command = request.POST.get("command")
            newimage = request.POST.get("newimage")
            msg = request.POST.get("msg", "msg")

            catalog_name = base_image.split(":")[0].split("/")[-1]

            #####################################
            # 获取初始化dockerfile 目录
            ######################################
            init_conf = get_init_names()
            config = fg.RawConfigParser()
            with open(init_conf, "r") as file:
                config.read_file(file)
                dockerfile_catalog = config.get("dockerfile", "dockerfile_catalog")
                df = dockerfile_catalog +"/" + newimage
            if os.path.exists(df):
                pass
            else:
                os.makedirs(df)
            dfs = df + "/" + "dockerfile"
            print "dfs"
            print dfs
            print "format"
            print "FROM {0}\nMAINTAINER {1}\n{2}".format(base_image, maintainer, command)
            with open(dfs, "w") as f:
                f.write("FROM {0}\nMAINTAINER {1}\n{2}".format(base_image, maintainer, command))
            status = 1
            res = build_image(newimage, version, df)
            print "res"
            print res
            if res == 1:
                try:
                    dockerfile = dockerfiles()
                    dockerfile.newimage = newimage
                    dockerfile.base_image = base_image
                    dockerfile.maintainer = maintainer
                    dockerfile.version = version
                    dockerfile.msg = msg
                    dockerfile.status = status
                    # dockerfile.newimage = newimage
                    dockerfile.save()
                    return redirect("/docker/image_build")
                    # return render(request, "image_build.html")
                except Exception:
                    print traceback.format_exc()
                    return HttpResponse(traceback.format_exc())
            else:
                return  HttpResponse("创建失败，请查看服务器！")
        except Exception:
            print traceback.format_exc()




def upload_dockerfile(request):
    if request.method == "GET":
        return render(request, "upload_dockerfile.html")
            
    if request.method == "POST":
        try:
            print "哎，我要做一个开源的crazygril,2018-5-23打卡,从头开始，加油！"
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            newimage = request.POST.get("newimage")
            # version = request.POST.get("version")
            # maintainer = request.POST.get("maintainer")
            msg = request.POST.get("msg")
            upload_dockerfile = request.FILES.get('upload_dockerfile')
            pwd = get_dockerfile_info()
            print "pwd"
            print pwd
            if not os.path.exists(pwd):
                os.mkdir(pwd)

            all_catalog = os.listdir(pwd)
            if newimage in all_catalog:
                return HttpResponse("目录重复，请重命名！")
            else:

                print  newimage,msg,upload_dockerfile,pwd
                nimp = pwd +"/"+ newimage
                os.mkdir(nimp)
                cata_df = nimp + "/" + "dockerfile"
                with open(cata_df,"wb") as f:
                    for chunk in upload_dockerfile.chunks():
                        f.write(chunk)
            b_v = get_base_image(cata_df)
            version = b_v["version"]
            base_image = b_v["base_image"]
            maintainer = b_v["maintainer"]
            print "cata_df,nimp",cata_df,nimp,maintainer,version
            if os.path.exists(cata_df) and os.path.exists(nimp):
                print "=======ssss"
                res = build_image(newimage, version, nimp)
                if res:
                    print "vvvvvvvvvvvv"
                    print msg, version, base_image, maintainer, newimage
                    res = dockerfiles()
                    res.newimage = newimage
                    res.msg = msg
                    res.version = version
                    res.base_image = base_image
                    res.maintainer = maintainer
                    res.save()
                    return redirect("/docker/image_build")
                else:
                    return HttpResponse("创建镜像不成功，请上服务器查看具体原因！")
            else:
                return HttpResponse("路径不存在或者文件不存在，请上服务器查看！")
        except Exception:
            print traceback.format_exc()
            return HttpResponse(traceback.format_exc())


def image_edit(request):
    if request.method == "POST":
        try:
            print "post"
            print "-----"
            print request.body
            newimage = request.POST.get("newimage")
            version = request.POST.get("version")
            maintainer = request.POST.get("maintainer")
            msg = request.POST.get("msg")
            Idc = request.POST.get("Idc","1")
            current_id = request.POST.get("current_id")
            print "Idc:"
            idcnu = Idc
            if idcnu == "1":
                idc_name="石景山"
            if idcnu == "2":
                idc_name = "三元桥"
            if idcnu == "3":
                idc_name = "苏州桥"
            obj = dockerfiles.objects.get(id=current_id)
            objs = dockerfiles.objects.filter(id=current_id).values()
            ori_image_name = objs[0]["newimage"]
            ori_image_version = objs[0]["version"]
            ori_image_maintainer = objs[0]["maintainer"]
            ori_image_msg = objs[0]["msg"]
            ori_image_idc = objs[0]["default"]
            if msg and msg == ori_image_msg:
                pass
            else:
                obj.msg = msg
            if maintainer and  maintainer == ori_image_maintainer:
                pass
            else:
                obj.maintainer = maintainer
            if idc_name == ori_image_idc:
                pass
            else:
                obj.default = idc_name
            if newimage and newimage == ori_image_name:
                pass
            else:
                obj.newimage = newimage
                ###更改docker tag
                res_name = image_change_vt(ori_image_name, ori_image_version, newimage, version)
                if res_name == 1:
                    pass
                else:
                    return HttpResponse("更改不成功，请上服务器上查看！")
            if version and newimage == ori_image_version:
                pass
            else:
                obj.version = version
                res_version = image_change_vt(ori_image_name, ori_image_version, newimage, version)
                if res_version == 1:
                    pass
                else:
                    return HttpResponse("更改不成功，请上服务器上查看！")
                ###更改docker tag

            obj.save()

            return redirect("/docker/image_build")
        except Exception:
            print traceback.format_exc()
            return HttpResponse(traceback.format_exc())




            # if newimage == ori_image_name and version == ori_image_version:
            #     pass
            #
            # if newimage != ori_image_name and version != ori_image_version:
            #
            #     #os.system("docker tag harbor.cntv.cn/rancher/{0}:{1} harbor.cntv.cn/rancher/{2}:{3} ".format(ori_image_name,ori_image_version,newimage,version))
            #     #os.system("mv /liu/dockerfiles/{0} /liu/dockerfiles/{1}".format(ori_image_name,newimage))
            #     #os.system("docker rmi -f harbor.cntv.cn/rancher/{0}:{1}".format(ori_image_name, ori_image_version))
            #     obj.dfilename = newimage
            #     obj.version = version
            #
            # if newimage != ori_image_name and version == ori_image_version:
            #     #os.system(
            #         # "docker tag harbor.cntv.cn/rancher/{0}:{1} harbor.cntv.cn/rancher/{2}:{3} ".format(ori_image_name,
            #         #                                                                                    ori_image_version,
            #         #                                                                                    newimage,
            #         #                                                                                    version))
            #     #os.system("mv /liu/dockerfiles/{0} /liu/dockerfiles/{1}".format(ori_image_name, newimage))
            #     #os.system("docker rmi -f harbor.cntv.cn/rancher/{0}:{1}".format(ori_image_name, ori_image_version))
            #     obj.dfilename = newimage
            # if newimage == ori_image_name and version != ori_image_version:
            #     #os.system("docker tag harbor.cntv.cn/rancher/{0}:{1} harbor.cntv.cn/rancher/{2}:{3} ".format(ori_image_name,
                                                                                                       # ori_image_version,
                                                                                                       # newimage,
                                                                                                       # version))
            #     #os.system("docker rmi -f harbor.cntv.cn/rancher/{0}:{1}".format(newimage, ori_image_version))
            #     obj.version = version
            # if maintainer:
            #     obj.maintainer = maintainer
            # if msg:
            #     obj.msg = msg
            # if Idc:
            #     obj.newimage = idc_name
            # obj.save()



    if request.method == "GET":
        print request.body
        image_edit_id = request.GET.get("image_edit_id")
        image_edit_res = dockerfiles.objects.filter(id=image_edit_id).values()
        print image_edit_res,type(image_edit_res)
        print "GET>>>>>>>>>>>>>>>>>>>>>>"
        newimage = image_edit_res[0]["newimage"]
        version = image_edit_res[0]["version"]
        base_image = image_edit_res[0]["base_image"]
        maintainer = image_edit_res[0]["maintainer"]
        times = image_edit_res[0]["times"]
        msg = image_edit_res[0]["msg"]
        ids = image_edit_res[0]["id"]
        upload_time=image_edit_res[0]["upload_time"]
        return render(request,"image_edit.html",locals())



def image_build(request):
    if request.method == "GET":
        print "request.user"
        print request.user
        pages = int(request.GET.get('page', '1'))
        all_datas = dockerfiles.objects.all()
        data = page_split(all_datas, pages, nu=4)
        all_data=data[0]
        paginator =data[1]
        res = get_host_info()
        hostip = res[1]
        print "all_data"
        print all_data
        return render(request, "image_build.html", locals())


        # paginator = Paginator(all_datas, 5)
        # try:
        #     page = int(request.GET.get('page', '1'))
        # except ValueError:
        #     page = 1
        # try:
        #     all_data = paginator.page(page)
        # except (EmptyPage, InvalidPage):
        #     all_data = paginator.page(paginator.num_pages)


    if request.method == "POST":
        all_datas = dockerfiles.objects.all()
        paginator = Paginator(all_datas, 5)
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        try:
            all_data = paginator.page(page)
        except (EmptyPage, InvalidPage):
            all_data = paginator.page(paginator.num_pages)
        res = get_host_info()
        hostip = res[1]
        return render(request, "image_build.html", locals())




def update_images(request):
    pass

        # page = request.GET.get('page', "1")
        # try:
        #     contacts = Paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     contacts = Paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of results.
        #     contacts = Paginator.page(paginator.num_pages)

        # return render(request, 'list.html', {'contacts': contacts})

        # paginator = Paginator(all_datas, 5)  # Show 25 contacts per page

        # Make sure page request is an int. If not, deliver first page.
        # try:
        #     page = int(request.GET.get('page', '1'))
        # except ValueError:
        #     page = 1
        #
        #     # If page request (9999) is out of range, deliver last page of results.
        # try:
        #     all_data = paginator.page(page)
        # except (EmptyPage, InvalidPage):
        #     all_data = paginator.page(paginator.num_pages)

        # return render_to_response('list.html', {"contacts": contacts})


        # return render(request, "image_build.html", locals())
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def show_con(request):
    if request.method == "POST":
        pass

    if request.method == "GET":
        try:
            all_datass = dockerHost.objects.all()
            paginator = Paginator(all_datass, 2)
            page = request.GET.get('page',"1")
            datas = dockerHost.objects.filter().values()
            hostnu = len(datas)
            try:
                all_data = paginator.page(page)
            except PageNotAnInteger:

                all_data = paginator.page(1)
            except EmptyPage:

                all_data = paginator.page(paginator.num_pages)
            return render(request, "docker_info.html", locals())
        except Exception:
            print traceback.format_exc()



def container_show(request):
    if request.method=="GET":
        try:
            hostip = request.GET.get("hostip")
            datas = DockerStat.objects.filter(hostip=hostip).values()
            datass =  datas[0]["txt"]

            print type(datass)
            data = json.loads(datass)
            print type(data)
            return render(request, "container_show.html", locals())
        except Exception:
            print traceback.format_exc()
            return HttpResponse("返回")



def t_get_conec(request):
    try:
        hostip = request.GET.get("hostip")
        c_name = request.GET.get("c_name")
        print hostip
        print c_name
        res = dockerStats.objects.filter(hostip=hostip,container=c_name).values()
        print "res"
        print res
        cpu = res[0]["cpu"].split("%")[0]
        mem = res[0]["Mem"].split("%")[0]
        if mem.split(".")[0]:
            pass
            # mem = str(int(float(mem)))
        else:
            mem = "0"
        if cpu.split(".")[0]:
            pass
            # cpu = str(int(float(cpu)))
        else:
            cpu = "0"
        print cpu, mem
        return render(request, "docker_stats_show2.html", locals())
    except Exception:
        print traceback.format_exc()




def show_stats(request):
    return render(request,"show_stats.html")
    # return HttpResponse("show stats")

def query_stat(request):
    try:
        query = request.body
        hostip = request.GET.get("hostip")
        print "fffffffff"
        print hostip
        all_data = dockerStats.objects.filter(hostip=hostip).values()
        print "ffffffffffff"
        print all_data
        return render(request, "query_stats.html", locals())
    except Exception:
        print traceback.format_exc()


def ajax_query_stats(request,hostip):
    print "hostip"
    print hostip
    print "=============="
    query = request.body
    hostip = request.GET.get("hostip")
    print hostip
    print query, type(query)
    stats = dockerStats.objects.filter(hostip=hostip).values()
    da = json.dumps(stats)
    print "da"
    print da
    return HttpResponse(da)


def ajax_docker_stats(request):
    print "reques method  i guss get"
    print request.method
    stats = dockerStats.objects.all().values()
    all_data = []
    for i in stats:
        di = {}
        di["hostname"] = i["hostname"]
        di["container"] = i["container"]
        di["cpu"] = i["cpu"]
        di["mem_ul"] = i["MemUL"]
        di["mem"] = i["Mem"]
        di["net_io"] = i["netIO"]
        di["block_io"] = i["blockIO"]
        di["ids"] = i["id"]
        all_data.append(di)
        # di["mem"] = i["Mem"]
    print "ssssssssssssssssssssssssssssss"
    print all_data,type(all_data)
    return HttpResponse(json.dumps(all_data))
    # query = {"hostname":"testslave1",
    #          "hostip": "10.64.10.65",
    #          "container": ""
    #          }
    # security_group = dockerStats.objects.values("id", "hostname", "hostip", "container", "cpu", "MemUL", "Mem", "netIO", "blockIO", "msg").filter(**query).order_by("-create_time")
    # print "ajax stats"
    # print stats,type(stats)
    # return HttpResponse(stats)
    # return HttpResponse(json.dumps(tuple(pingdetectlist)))

def docker_echarts(request):
    hostip = "10.64.10.65"
    hostname = "Server"
    ss = dockerStats.objects.filter(hostip=hostip).values()
    res = []
    for i in ss:
        res.append(i["container"])
    return render(request,"docker_stats_show.html",locals())
    # pass
def Ajax_getInfo(request):
    try:
        # print "1111111111"
        print request.body
        container = request.GET.get("container")
        print container
        # print "22222222222222"
        ss = dockerStats.objects.filter(container=container).values()
        print "ssssssssssssssssssssssssssssssss"
        dic = {}
        dic["mem"] = ss["Mem"]
        dic["cpu"] = ss["cpu"]
        return HttpResponse(json.dumps(dic))
    except Exception:
        print traceback.format_exc()

def container_e(request):
    try:
        container_id = request.GET.get("container_id")
        mem = dockerStats.objects.filter(id=container_id).values()[0]["Mem"].split("%")[0]
        cpu = dockerStats.objects.filter(id=container_id).values()[0]["cpu"].split("%")[0]
        print "123123123132132"
        print  mem,type(mem)
        print  cpu, type(cpu)
        if mem.split(".")[0]:
            pass
            # mem = str(int(float(mem)))
        else:
            mem = "0"
        if cpu.split(".")[0]:
            pass
            # cpu = str(int(float(cpu)))
        else:
            cpu = "0"
        print cpu,mem
        return render(request,"docker_stats_show2.html",locals())
    except Exception:
        print traceback.format_exc()

def Ajax_tt(request):
    return HttpResponse("123")

def search_c(request):
    print request.body
    c_name = request.POST.get("c_name")
    hostip = request.POST.get("hostip")
    print c_name,hostip
    res =dockerStats.objects.filter(hostip=hostip,container=c_name).values()
    print res
    mem = res[0]["Mem"].split("%")[0]
    cpu = res[0]["cpu"].split("%")[0]
    print mem,cpu
    return render(request,"docker_stats_show.html",locals())