import requests
import datetime
import time
import json
import urllib3
urllib3.disable_warnings()
from apscheduler.schedulers.background import BackgroundScheduler


headers={
    "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    "Cookie":"JSESSIONID=a",
    "Connection":"close"
}

def dingtalk(content):
    """
    钉钉通知函数
    :param content: 要通知的内容
    :return: none
    """
    webhook_url = "https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN"
    dd_headers = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    dd_message = {
        "msgtype": "text",
        "text": {
            "content": f'{content}'
        }
    }

    r = requests.post(url=webhook_url, headers=dd_headers, data=json.dumps(dd_message))

def Task():
        url = "YOUR_URL"
        r = requests.get(url,headers=headers,verify=False)
        print(r.status_code)
        if r.status_code != 404:
            dingtalk("YES !!!")
        else:
            dingtalk("NoNoNo !!!")



if __name__ == '__main__':
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()  
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    scheduler.add_job(Task, 'interval', hours=2)
    # 启动调度任务
    scheduler.start()

    while True:
        print(time.time())
        time.sleep(5)
    
