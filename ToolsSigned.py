#coding=utf8
__author__ = 'jacky'
from wxpy import *

bot = Bot(cache_path=True)  #微信扫码登录，开启缓存

for tools in bot.mps().search("TOOls"): # 获得所有公众号并搜索tools公众号
    tools.send('3')
    for text in bot.messages:
        if text.text != "3":
            if u"签过到" in text.text:
                print "今天已签过到了..."
            if u"恭喜" in text.text:
                print  "今天签到了..."










