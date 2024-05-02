from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()

# 防止睡眠
def DoNotSleep():
    url = "https://police-robot.onrender.com/callback"
    r = requests.get(url)

# 防止自動休眠
sched.add_job(DoNotSleep, trigger='interval', id='doNotSleeps_job', day_of_week='mon-fri', minute='*/15')
