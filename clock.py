from apscheduler.schedulers.blocking import BlockingScheduler
import urllib

sched = BlockingScheduler()

'''
# 防止睡眠
def DoNotSleep():
    url = "https://github.com/yazzzhu/police_robot" #https://police-robot.onrender.com
    r = requests.get(url)

# 防止自動休眠
sched.add_job(conn, trigger='interval', id='doNotSleeps_job', day_of_week='mon-fri', minute='*/15')
'''

@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/15')
def scheduled_job():
    url = "https://github.com/yazzzhu/police_robot"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

sched.start()
