import requests
import urllib3
urllib3.disable_warnings()
import re

'''
python3 爬虫demo
'''
url="https://127.0.0.1/?id={}"
s = requests.session()
s.keep_alive = False
proxies = {
  "http": "http://127.0.0.1:1080",
  "https": "http://127.0.0.1:1080",
}
headers={
    "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    "Cookie":"JSESSIONID=a",
    "Connection":"close"
}


r = s.get(url.format(12000),headers=headers,proxies=proxies,verify=False)
print(r.text)



# findall model
key_pattern=re.compile(r'<label class="col" >(.*?)</label>')
keys = key_pattern.findall(r.text)
print(keys)
# match model
match_value_pattern = re.compile(r'.*?<label>(.*?)</label>.*?<label>(.*?)</label>.*?',re.M|re.S)
value = match_value_pattern.match(r.text)
print(value.groups())

