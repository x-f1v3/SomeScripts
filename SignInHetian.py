# -*- coding: utf-8 -*-

#www.hetianlab.com 签到
import requests
import json

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer':'http://www.hetianlab.com/pages/profile.jsp?w=dyns&u=REG-79b8-844e-437a-ad37-a4f23e575450',

        }
login_url='http://www.hetianlab.com/Login.action'
sign_url='http://www.hetianlab.com/userInfo!isFirLogin.action'
query_coin_url='http://www.hetianlab.com/outUserInfo!getUserInfo.action'
query_payload={'userId':''} # 你的userId

payload={'username':'',#username
         'password':'',#password
         'validateCode':'',
         'rtnJson':'true',
} # passwd在本地是加密的，要抓包获得

s=requests.session()
r=s.post(login_url,headers=header,data=payload) #登录
sign_html=s.get(sign_url) # 签到
sign_data =json.loads(sign_html.content)
total_money_html=s.post(query_coin_url,data=query_payload) #查询
totalMoney=json.loads(total_money_html.content)  # 查询总的coin
if str(sign_data['result']) =='success' and str(sign_data['coin']) !='0.0':
    print  'Sign in successfully'
    total_money_html=s.post(query_coin_url,data=query_payload) #查询
    totalMoney=json.loads(total_money_html.content)  # 查询总的coin
    print 'totalCoin is '+str(totalMoney['c'])
else:
    print "Sign in already"
    print 'totalCoin is '+str(totalMoney['c'])




