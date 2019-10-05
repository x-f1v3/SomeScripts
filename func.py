#跑子域名过滤目标
import re

def Get_domain(domain):
    if domain.startswith('http://www.'):
        domain = domain[11:]
    if domain.startswith('https://www.'):
        domain = domain[12:]
    if domain.startswith('http://'):
        domain = domain[7:]
    if domain.startswith('https://'):
        domain = domain[8:]
    if is_ip_address_format(domain):
        return None
    if "/" in domain:
        domain=domain[:domain.index("/")]
    return domain




def is_ip_address_format(value):
    IP_ADDRESS_REGEX = r"\b(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b"
    if value and re.match(IP_ADDRESS_REGEX, value):
        return True
    else:
        return False


a = ["http://www.baidu.com/aaaa/aaa.asp","https://www.baidu.com/aaaa?as=b&b=ass","http://1.1.1.1/aaaa",'https://1.1.1.1/aaaa','http://1.1.1.1:90/aaaa','http://aaa.baidu.com/aaaa','baidu.com','']


for b in a:
    print(init(b))
    
    

# 输入指定字符串，返回随机大小写

import random

def random_list(start,stop,length):
    if length>=0:
        length=int(length)
  	start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  	random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


string = "string"

alphalen = 0

for s in string:
	if s.isalpha():
		alphalen +=1


stringlist = list(string)
randomlist = random_list(0,alphalen,random.randint(int(len(string)/3),int(len(string)/2)))

for x in randomlist:
	if stringlist[x].isalpha():
		stringlist[x] = stringlist[x].upper()

randomstring = ''.join(stringlist)
print(randomstring)
