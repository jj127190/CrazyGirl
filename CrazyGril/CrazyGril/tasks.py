#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import traceback
import os
from celery import Celery

import time

from celery import shared_task
from django.conf import settings

@shared_task
def sayhello():
    try:
        print('hello ...')
        # time.sleep(2)
        os.mkdir("./123123123")
        print('world ...')
        return "heihei"
    except Exception:
        print traceback.format_exc()