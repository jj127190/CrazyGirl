from __future__ import absolute_import
# from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CrazyGril.settings')
app = Celery('CrazyGril')


app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
