#-*-coding:utf-8-*-

import os
from pymongo import MongoClient
import traceback
from django.shortcuts import render
import configparser as fg
from subprocess import Popen, PIPE
from cmdb.models import ASSET_STATUS,ASSET_TYPE
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def connect_mon(hostid):
    conn = MongoClient('127.0.0.1', 27017)
    db = conn.crazygril
    my_set = db.hostid
    return my_set


def insert_data(my_set,time,data):
    data={"time":time,
          "contact":data
 }





