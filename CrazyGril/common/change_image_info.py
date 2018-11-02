#! -*- coding:utf-8 -*-
import os
from subprocess import PIPE,Popen

def image_change_vt(ori_image,ori_version,new_image,new_version):
    ori = ori_image+":"+ori_version
    new = new_image+":"+new_version
    command = "docker tag {0} {1}".format(ori,new)
    p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    out = p.stdout.readlines()
    print "out))))))))))))))"
    print out
    result = "docker images"
    p = Popen(result, shell=True, stdout=PIPE, stderr=PIPE)
    out = p.stdout.readlines()
    for re in out:
        if new_image and new_version in re.split():
            return 1
    # res = []
    # for re in out:
    #     res.append(re.split()[0] + ":" + re.split()[1])

def image_version_change():
    pass