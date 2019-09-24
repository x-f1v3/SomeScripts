# 浏览器访问url自动批量截图
from selenium import webdriver
from PIL import ImageGrab
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
with open("222.txt","r") as f:
	urls = f.readlines()

try:
	for i, url in enumerate(urls, start=1):
		try:
			browser.get(url)
			time.sleep(10)
			im = ImageGrab.grab()
			im.save('screenshot_%03d.png' % i)
			
			
		except Exception,e:
			print str(e)
finally:
	browser.quit()
	
