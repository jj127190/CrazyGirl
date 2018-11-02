#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import os
import ansible.runner
import ansible.playbook
import ansible.inventory
import traceback
from cmdb.models import Idc,Host
from ansible import callbacks
from ansible import utils
import json
from celery import task,shared_task



@task
def copadcar(selectip,argc,argsh):
    try:
        hosts = selectip
        example_inventory = ansible.inventory.Inventory(hosts)
        cop = ansible.runner.Runner(
            module_name='copy',
            module_args=argc,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        sh = ansible.runner.Runner(
            module_name='shell',
            module_args=argsh,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        out = cop.run()
        out1 = sh.run()
        res = json.dumps(out1, sort_keys=True, indent=4, separators=(',', ': '))
        return res
    except Exception:
        print traceback.format_exc()



@task()
def ttttt():
    print "fuck =.=!!!!!!"
    time.sleep(5)
    os.system("mkdir /fuck")
    return "ma de"



@task()
def add(x, y):
    return x + y
@task
def mk():
    time.sleep(10)
    os.system("mkdir /222222")
    os.system("mkdir /111111")
    print "异步创建完成####"
    return "create 123123 success ok!!!!!@@@@@"

@task
def run_test_suit(ts_id):
    print "++++++++++++++++++++++++++++++++++++"
    print('jobs[ts_id=%s] running....' % ts_id)
    time.sleep(5)

    print('jobs[ts_id=%s] done' % ts_id)
    result = True
    return result









@task
def idse(selectip, shell_command,ac_name):
    try:
        hosts = [selectip]
        example_inventory = ansible.inventory.Inventory(hosts)
        pm = ansible.runner.Runner(
            module_name='command',
            module_args=shell_command,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        out = pm.run()
        res = json.dumps(out, sort_keys=True, indent=4, separators=(',', ': '))
        # return res
        print "#######ansible完成####"
        return "{0} 任务已完成！".format(ac_name)
    except Exception:
        print traceback.format_exc()
        return "异常 -- mk test  success ok!!!!!@@@@@"
############idse 加功能##############

@task
def idsecq(selectip, shell_command,copy_command,q_command,name):
    try:
        time.sleep(10)
        print "################"
        print selectip, shell_command,copy_command,q_command,name
        hosts = [selectip]


        example_inventory = ansible.inventory.Inventory(hosts)
        pm = ansible.runner.Runner(
            module_name='command',
            module_args=shell_command,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        out = pm.run()

        cp = ansible.runner.Runner(
            module_name='copy',
            module_args=copy_command,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        cp1 = cp.run()

        q = ansible.runner.Runner(
            module_name='shell',
            module_args=q_command,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        out2 = q.run()


        res = json.dumps(out2, sort_keys=True, indent=4, separators=(',', ': '))
        # return res
        print "#######ansible完成####"
        return "curring task:{0} successful".format(name)
    except Exception:
        print traceback.format_exc()
        return "this task:{0} is traceback，reason:{1}".format(name, traceback.format_exc())

#############only upfile#########################


@task
def uf(selectip,copy_command,q_command,name):
    try:
        print selectip,copy_command,q_command,name
        hosts = [selectip]
        example_inventory = ansible.inventory.Inventory(hosts)

        cp = ansible.runner.Runner(
            module_name='copy',
            module_args=copy_command,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        cp1 = cp.run()
        q = ansible.runner.Runner(
            module_name='shell',
            module_args=q_command,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        out2 = q.run()
        res = json.dumps(out2, sort_keys=True, indent=4, separators=(',', ': '))
        print "#######ansible完成####"
        return "curring task:{0} successful".format(name)
    except Exception:
        print traceback.format_exc()
        return "this task:{0} is traceback，reason:{1}".format(name,traceback.format_exc())









##############################





@task
def segroup(selectip, shell_command):
    try:
        hosts = selectip
        example_inventory = ansible.inventory.Inventory(hosts)
        pm = ansible.runner.Runner(
            module_name='command',
            module_args=shell_command,
            timeout=5,
            inventory=example_inventory,
            subset='all'
        )
        out = pm.run()
        res = json.dumps(out, sort_keys=True, indent=4, separators=(',', ': '))
        return res
    except Exception:
        print traceback.format_exc()







@task
def seleid(selectip, shell_command):
    pass



@task
def selegroup(idss,shell_command):
    try:
        aip = idss
        command = shell_command
        hosts = aip
        example_inventory = ansible.inventory.Inventory(hosts)

        pm = ansible.runner.Runner(
            module_name='command',
            module_args=command,
            timeout=5,
            inventory=example_inventory,
            subset='all'  # name of the hosts group
        )

        out = pm.run()

        print json.dumps(out, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception:
        print traceback.format_exc()



    # if option == "机房":
    #     res = Idc.objects.filter(name=rag).values()[0]["id"]
    #
    # if option == "组织":
    #     pass




#########################成功
#
# {
#     "contacted": {
#         "10.77.64.122": {
#             "changed": true,
#             "cmd": [
#                 "uptime"
#             ],
#             "delta": "0:00:00.009305",
#             "end": "2018-06-28 15:21:17.452986",
#             "invocation": {
#                 "module_args": "uptime",
#                 "module_complex_args": {},
#                 "module_name": "command"
#             },
#             "rc": 0,
#             "start": "2018-06-28 15:21:17.443681",
#             "stderr": "",
#             "stdout": " 15:21:17 up 71 days, 27 min,  3 users,  load average: 0.01, 0.02, 0.05",
#             "warnings": []
#         }
#     },
#     "dark": {}
# }
# @##################失败
# {
#     "contacted": {
#         "10.77.64.122": {
#             "cmd": "Suptime",
#             "failed": true,
#             "invocation": {
#                 "module_args": "Suptime",
#                 "module_complex_args": {},
#                 "module_name": "command"
#             },
#             "msg": "[Errno 2] No such file or directory",
#             "rc": 2
#         }
#     },
#     "dark": {}
# }
#
# ###############
# {
#     "contacted": {},
#     "dark": {
#         "10.77.64.1223": {
#             "failed": true,
#             "msg": "SSH Error: ssh: Could not resolve hostname 10.77.64.1223: Name or service not known\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue."
#         }
#     }
# }