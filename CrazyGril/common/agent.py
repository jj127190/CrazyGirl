#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import re
import sys
import json
import time
import traceback
import socket
import platform, threading
import psutil, schedule, requests
from subprocess import Popen, PIPE
import logging

# token = ''
CrazyServerIP = '127.0.0.1'


def log(log_name, path="./"):
    logging.basicConfig(
        # stream=sys.stdout,
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%Y%m%d-%H:%M:%S',
        filename=path + log_name,
        filemode='ab+')
    return logging.basicConfig


log("CrazyGril.log", "./")


def get_ip():
    try:
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
    except Exception as msg:
        print(msg)
        logging.error(traceback.format_exc())
        ipaddr = ''
    return ipaddr


def get_hostname():
    try:
        hostname = socket.getfqdn(socket.gethostname())
        ipaddr = socket.gethostbyname(hostname)
    except Exception as msg:
        print(msg)
        logging.error(traceback.format_exc())
        ipaddr = ''
    return hostname


def get_dmi():
    p = Popen('dmidecode', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout


def parser_dmi(dmidata):
    try:
        pd = {}
        line_in = False
        for line in dmidata.split('\n'):
            if line.startswith('System Information'):
                line_in = True
                continue
            if line.startswith('\t') and line_in:
                k, v = [i.strip() for i in line.split(':')]
                pd[k] = v
            else:
                line_in = False
    except Exception:
        logging.error("parser_dmi" + traceback.format_exc())
    return pd


# 本机 agent  docker 信息

def docker_infos():
    d_ps = os.popen("docker ps -a|wc -l")
    d_ps = d_ps.read().strip()
    d_im = os.popen("docker images|wc -l")
    d_im = d_im.read().strip()
    d_ps = int(d_ps) - 1
    d_im = int(d_im) - 1
    p = Popen('docker ps -a', stdout=PIPE, shell=True)
    out = p.stdout.readlines()
    del out[0]
    all = []
    for i in out:
        res = {}
        res["d_ps"] = d_ps
        res["d_im"] = d_im
        res["hostname"] = get_hostname()
        res["hostip"] = get_ip()
        id = i.split("\"")[0].strip().split()[0]
        res["id"] = id
        image = i.split("\"")[0].strip().split()[1]
        res["image"] = image
        command = i.split("\"")[1]
        res["command"] = command
        res_last = i.split("\"")[2].strip().split("   ")
        tt = []
        for i in res_last:
            if i:
                tt.append(i.strip())
        res["create"] = tt[0]
        res["status"] = tt[1]
        if len(tt) == 4:
            res["port"] = tt[2]
            res["name"] = tt[3]
        else:
            res["name"] = tt[2]
            res["port"] = ""

        all.append(res)
    return all


def docker_statss():
    try:
        """
        docker stats == cadvisor self create dashbord!!!
        """
        dcom_stats = "docker stats $(docker ps -a --format={{.Names}}) --no-stream"
        P = Popen(dcom_stats, stdout=PIPE, shell=True)
        stats = P.stdout.readlines()
        del stats[0]
        all_dic = {}
        all_datas = []
        for i in stats:
            clean_stats = []
            stats_lis = i.split("   ")
            while '' in stats_lis:
                stats_lis.remove('')
            for sta in stats_lis:
                clean_stats.append(sta.strip())
            all_datas.append(clean_stats)
        print "post docker stats"
        print all_datas
        return json.dumps(all_datas)
    except Exception:
        print traceback.format_exc()


def post_docker_stats():
    try:
        ds = docker_statss()
        # ds = json.dumps(sts)
        datas = {}
        datas["hostname"] = get_hostname()
        datas["ip"] = get_ip()
        docker_stats = ds + "*" + json.dumps(datas)
        post_data("http://{0}/api/get_dockerStats/".format(CrazyServerIP), docker_stats)
    except Exception:
        print traceback.format_exc()


def post_docker_info():
    try:

        res = docker_infos()
        print "res============"
        logging.info(json.dumps(res))
        docker_info = json.dumps(res)
        # datas = {}
        # datas["hostname"] = get_hostname()
        # datas["ip"] = get_ip()
        # d_pi = {}
        # d_pi["d_ps"] = d_ps
        # d_pi["d_im"] = d_im
        # docker_info = docker_info
        # docker_info = docker_info + "*" + json.dumps(datas) + "*" + json.dumps(d_pi)
        print "docker info"
        print docker_info
        post_data("http://{0}/api/get_dockerInfo/".format(CrazyServerIP), docker_info)
    except Exception:
        print traceback.format_exc()
        logging.info(traceback.format_exc())


def get_mem_total():
    cmd = "grep MemTotal /proc/meminfo"
    p = Popen(cmd, stdout=PIPE, shell=True)
    data = p.communicate()[0]
    mem_total = data.split()[1]
    memtotal = int(round(int(mem_total) / 1024.0 / 1024.0, 0))
    return memtotal


def get_cpu_model():
    cmd = "cat /proc/cpuinfo"
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout


def get_cpu_cores():
    cpu_cores = {"physical": psutil.cpu_count(logical=False) if psutil.cpu_count(logical=False) else 0,
                 "logical": psutil.cpu_count()}
    return cpu_cores


def parser_cpu(stdout):
    groups = [i for i in stdout.split('\n\n')]
    group = groups[-2]
    cpu_list = [i for i in group.split('\n')]
    cpu_info = {}
    for x in cpu_list:
        k, v = [i.strip() for i in x.split(':')]
        cpu_info[k] = v
    return cpu_info


def get_disk_info():
    ret = []
    cmd = "fdisk -l|egrep '^Disk\s/dev/[a-z]+:\s\w*'"
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = p.communicate()
    for i in stdout.split('\n'):
        disk_info = i.split(",")
        if disk_info[0]:
            ret.append(disk_info[0])
    return ret


def post_data(url, data):
    try:
        r = requests.post(url, data)
        if r.text:
            logging.info(r.text)
        else:
            logging.info("Server return http status code: {0}".format(r.status_code))
    except Exception as msg:
        logging.info(msg)
    return True


def asset_info():
    data_info = dict()
    data_info['memory'] = get_mem_total()
    data_info['disk'] = str(get_disk_info())
    cpuinfo = parser_cpu(get_cpu_model())
    cpucore = get_cpu_cores()
    data_info['cpu_num'] = cpucore['logical']
    data_info['cpu_physical'] = cpucore['physical']
    data_info['cpu_model'] = cpuinfo['model name']
    data_info['ip'] = get_ip()
    data_info['sn'] = parser_dmi(get_dmi())['Serial Number']
    data_info['vendor'] = parser_dmi(get_dmi())['Manufacturer']
    data_info['product'] = parser_dmi(get_dmi())['Version']
    data_info['osver'] = platform.linux_distribution()[0] + " " + platform.linux_distribution()[
        1] + " " + platform.machine()
    data_info['hostname'] = platform.node()
    data_info['status'] = "使用中"
    return json.dumps(data_info)


def asset_info_post():
    try:
        # print "asset info tran CrazyGril ......."
        # print asset_info()
        logging.info('Get the hardwave infos from host:')
        logging.info(asset_info())
        logging.info('----------------------------------------------------------')
        post_data("http://{0}/api/get_asset_info".format(CrazyServerIP), asset_info())
        return True
    except Exception:
        print traceback.format_exc()
        logging.info("asset_info_post error because:" + traceback.format_exc())


def get_sys_cpu():
    sys_cpu = {}
    cpu_time = psutil.cpu_times_percent(interval=1)
    sys_cpu['percent'] = psutil.cpu_percent(interval=1)
    sys_cpu['lcpu_percent'] = psutil.cpu_percent(interval=1, percpu=True)
    sys_cpu['user'] = cpu_time.user
    sys_cpu['nice'] = cpu_time.nice
    sys_cpu['system'] = cpu_time.system
    sys_cpu['idle'] = cpu_time.idle
    sys_cpu['iowait'] = cpu_time.iowait
    sys_cpu['irq'] = cpu_time.irq
    sys_cpu['softirq'] = cpu_time.softirq
    return sys_cpu


def get_sys_mem():
    sys_mem = {}
    mem = psutil.virtual_memory()
    sys_mem["total"] = mem.total / 1024 / 1024
    sys_mem["percent"] = mem.percent
    sys_mem["available"] = mem.available / 1024 / 1024
    sys_mem["used"] = mem.used / 1024 / 1024
    sys_mem["free"] = mem.free / 1024 / 1024
    sys_mem["buffers"] = mem.buffers / 1024 / 1024
    sys_mem["cached"] = mem.cached / 1024 / 1024
    return sys_mem


def parser_sys_disk(mountpoint):
    partitions_list = {}
    d = psutil.disk_usage(mountpoint)
    partitions_list['mountpoint'] = mountpoint
    partitions_list['total'] = round(d.total / 1024 / 1024 / 1024.0, 2)
    partitions_list['free'] = round(d.free / 1024 / 1024 / 1024.0, 2)
    partitions_list['used'] = round(d.used / 1024 / 1024 / 1024.0, 2)
    partitions_list['percent'] = d.percent
    return partitions_list


def get_sys_disk():
    sys_disk = {}
    partition_info = []
    partitions = psutil.disk_partitions()
    for p in partitions:
        partition_info.append(parser_sys_disk(p.mountpoint))
    sys_disk = partition_info
    return sys_disk


# 函数获取各网卡发送、接收字节数
def get_nic():
    key_info = psutil.net_io_counters(pernic=True).keys()  # 获取网卡名称

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)  # 各网卡接收的字节数
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)  # 各网卡发送的字节数

    return key_info, recv, sent


# 函数计算每秒速率
def get_nic_rate(func):
    key_info, old_recv, old_sent = func()  # 上一秒收集的数据
    time.sleep(1)
    key_info, now_recv, now_sent = func()  # 当前所收集的数据

    net_in = {}
    net_out = {}

    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)  # 每秒接收速率
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024)  # 每秒发送速率

    return key_info, net_in, net_out


def get_net_info():
    net_info = []
    key_info, net_in, net_out = get_nic_rate(get_nic)
    for key in key_info:
        in_data = net_in.get(key)
        out_data = net_out.get(key)
        net_info.append({"nic_name": key, "traffic_in": in_data, "traffic_out": out_data})
    return net_info


def agg_sys_info():
    try:
        logging.info('Get the system infos from host:')
        sys_info = {'hostname': platform.node(),
                    'hostid': get_ip(),
                    'cpu': get_sys_cpu(),
                    'mem': get_sys_mem(),
                    'disk': get_sys_disk(),
                    'net': get_net_info()
                    }

        logging.info(sys_info)
        json_data = json.dumps(sys_info)
        # print "json_data tran info to CrazyGril .........."
        # print json_data
        logging.info(json_data)
        post_data("http://{0}/api/get_sysInfo/".format(CrazyServerIP), json_data)
        return True
    except Exception:
        print traceback.format_exc()
        logging.info(traceback.format_exc())


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def write_pid():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    pid = str(os.getpid())
    with open(BASE_DIR + "/CrazyAgent.pid", "wb+") as pid_file:
        pid_file.writelines(pid)


def clean_log():
    CA_log = "CrazyGril.log"
    CA_Clog = CA_log + "_" + str(time.time()).split(".")[0] + ".bak"
    os.system("> {0}".format(CA_log))
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # os.system("cd {0} && mv {1} {2} && touch {1}".format(BASE_DIR,CA_log,CA_Clog))
    logging.info("clean agent log")


if __name__ == "__main__":
    try:
        logging.info("CraztGirl Agent start to connect server successfully...................... ")
        print "              "
        print "CraztGirl Agent start to connect server ......................"
        docker_statss()
        post_docker_stats()
        asset_info_post()
        agg_sys_info()
        post_docker_info()
        write_pid()
        print "                                       "

        time.sleep(1)
        schedule.every(300).seconds.do(run_threaded, asset_info_post)
        schedule.every(300).seconds.do(run_threaded, post_docker_info)
        schedule.every(300).seconds.do(run_threaded, agg_sys_info)
        schedule.every(10).seconds.do(run_threaded, clean_log)
        # 每周早上班的时候检查
        schedule.every().monday.at("09:20").do(run_threaded, clean_log)
        while True:
            schedule.run_pending()
            time.sleep(1)
        print "                                       "
        print "now it is successfully ........................!! "
        print "                            "
        print "please checkout CrazyGirl log file........................."
        time.sleep(1)
    except Exception:
        print "CraztGirl Agent down,becase:{0}......................".format(traceback.format_exc())
        logging.error("CraztGirl Agent down,becase:{0}......................".format(traceback.format_exc()))