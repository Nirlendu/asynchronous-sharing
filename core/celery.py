#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

from __future__ import absolute_import
import os

from celery import Celery

# Indicate Celery to use the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')

from django.conf import settings

app = Celery('core',
             backend='amqp',
             broker='amqp://nirlendu:nirlendu@localhost:5672/vhost'
             )
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')

app.config_from_object('core.config.celery')

# This line will tell Celery to autodiscover all your tasks.py that are in your app folders
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

if __name__ == '__main__':
    app.start()
