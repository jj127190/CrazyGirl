#-*- coding:utf-8 -*-
import json
import logging
import traceback
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
import os
import configparser as fg
import socket

def get_host_info():
    host_name = socket.getfqdn(socket.gethostname())
    host_ip = socket.gethostbyname(host_name)
    res = {"hostip" : host_ip, "hostname": host_name}
    return res
# Create your views here.
def conf_show(request):

    try:
        # host_ip = socket.getfqdn(socket.gethostname())
        # host_name = socket.gethostbyname(host_ip)
        host_ip=get_host_info()["hostip"]
        host_name =get_host_info()["hostname"]
        dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        init_conf = dirs + "/init.conf"
        config = fg.RawConfigParser()
        with open(init_conf, "r") as file:
            config.read_file(file)
            file_path = config.get("dockerfile", "dockerfile_catalog")
            logpath = config.get("log", "log_path")
            port = config.get("host", "port")
            mysqldb = config.get("mysql", "database")
            mysqlip = config.get("mysql", "host")
            mysqlport = config.get("mysql", "port")
            mysqlpass = config.get("mysql", "password")
            mysqluser = config.get("mysql", "user")
            print "sssssssss>>>>>>>>>>"
            print "logoath"+ logpath
            if file_path and logpath and mysqldb and   mysqlip  and mysqlport and mysqlpass:
                return render(request, "conf_file.html",locals())
            else:
                return render(request, "conf_file.html",locals())
    except Exception:
        print traceback.format_exc()
        return HttpResponse(traceback.format_exc())
    # return HttpResponse("conf_show")



def conf_save(request):
    if request.method == "POST":
        try:
            host_ip = get_host_info()["hostip"]
            host_name = get_host_info()["hostname"]
            dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            init_conf = dirs + "/init.conf"
            config = fg.RawConfigParser()
            hostip = request.POST.get("host_ip")
            port = request.POST.get("port")
            file_path = request.POST.get("file_path")
            logpath = request.POST.get("logpath")
            mysqldb = request.POST.get("mysqldb", "crazygril")
            mysqlip = request.POST.get("mysqlip")
            mysqlport = request.POST.get("mysqlport", "3306")
            mysqlpass = request.POST.get("mysqlpass")
            mysqluser = request.POST.get("mysql", "root")
            print "conf_save====================="
            print hostip,file_path,logpath,port,mysqldb,mysqlport,mysqlpass
            print type(port)
            config.add_section('host')
            config.set('host' , 'port', port)
            config.add_section('dockerfile')
            config.set('dockerfile', 'dockerfile_catalog', file_path)
            config.add_section('log')
            config.set('log', 'log_path', logpath)
            config.add_section('mysql')
            config.set('mysql', 'host', mysqlip)
            config.set('mysql', 'port', mysqlport)
            config.set('mysql', 'database', mysqldb)
            config.set('mysql', 'password', mysqlpass)
            config.set('mysql', 'user', mysqluser)
            with open(init_conf, 'wb') as file_con:
                config.write(file_con)
            return render(request, "conf_file.html", locals())
        except Exception:
            print traceback.format_exc()
            return traceback.format_exc()