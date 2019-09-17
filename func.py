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
    
    
