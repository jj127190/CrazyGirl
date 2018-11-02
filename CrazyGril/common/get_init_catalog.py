#-*-coding:utf-8-*-
import os
from subprocess import Popen, PIPE
import configparser as fg
dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
init_names="init.conf"
def get_init_names():
    init_conf_catalog= dirs + "/" +init_names
    return init_conf_catalog

def get_mysql_info():
    pass


def get_dockerfile_info():
    config = fg.RawConfigParser()
    init_conf = get_init_names()
    with open(init_conf, "r") as file:
        config.read_file(file)
        file_path = config.get("dockerfile", "dockerfile_catalog")
        return file_path
        # logpath = config.get("log", "log_path")
        # port = config.get("host", "port")


def get_log_info():
    pass
