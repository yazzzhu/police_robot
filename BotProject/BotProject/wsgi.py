"""
WSGI config for BotProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BotProject.settings')

application = get_wsgi_application()


from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()

# 防止睡眠
def DoNotSleep():
    url = "https://police-robot.onrender.com/callback"
    r = requests.get(url)

# 防止自動休眠
sched.add_job(DoNotSleep, trigger='interval', id='doNotSleeps_job', day_of_week='mon-fri', minute='*/15')