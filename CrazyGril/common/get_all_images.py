#-*-coding:utf-8-*-

import os
import time
import traceback
import configparser as fg
from subprocess import Popen, PIPE

dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get_images(command):
    # command = "docker images"
    regirsty="REPOSITORY:TAG"
    res = []
    p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    out = p.stdout.readlines()
    for re in out:
        # if "REPOSITORY"
        res.append(re.split()[0] + ":" + re.split()[1])
    if regirsty in res:
        res.remove(regirsty)
    # print res
    return res


def build_image(name, version, catalog):
    # config = fg.RawConfigParser()
    print "hhhhhhhhhhhhh"
    print name,version,catalog
    names = name.lower()
    command = "cd {0} && docker build -t {1}:{2} .".format(catalog, names, version)
    print command
    p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    out = p.stdout.readlines()
    print out
    if "Successfully built" in ''.join(out):
        return 1
    else:
        return 0


def del_image(pwd):
    try:
        dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        init_conf = dirs + "/init.conf"
        print "init_conf"
        print init_conf
        config = fg.RawConfigParser()
        with open(init_conf, "r") as file:
            config.read_file(file)
            dockerfile_pwd = config.get("dockerfile", "dockerfile_catalog")
        dockerfile_pwd = dockerfile_pwd + "/" + pwd
        print "dockerfile_pwd"
        print dockerfile_pwd
        changef = "dockerfile" + "_" + str(time.time()).split(".")[0] + ".bak"
        command = "cd {0} && mv dockerfile {1}".format(dockerfile_pwd, changef)
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        out = p.stdout.readlines()
    except Exception:
        print traceback.format_exc()
        return traceback.format_exc()
    # for re in out:
