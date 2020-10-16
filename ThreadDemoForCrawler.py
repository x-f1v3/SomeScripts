# -*- coding: utf-8 -*-
import Queue  
import threading
import requests 

hosts = []
queue = Queue.Queue()#存放网址的队列  
out_queue = Queue.Queue()#存放网址页面的队列  
      
class ThreadUrl(threading.Thread):  
	def __init__(self,queue,out_queue):  
		threading.Thread.__init__(self)  
		self.queue = queue  
		self.out_queue = out_queue  
      
	def run(self):  
		while True:  
			host = self.queue.get()  
			url = urllib2.urlopen(host)  
			chunk = url.read()  
			self.out_queue.put(chunk)  
			self.queue.task_done()
      
class DatamineThread(threading.Thread):  
	def __init__(self,out_queue):  
		threading.Thread.__init__(self)  
		self.out_queue = out_queue  
      
	def run(self):  
		while True:  
			chunk = self.out_queue.get() 
			self.out_queue.task_done()  
       
def main():  
	for i in range(5):  
		t = ThreadUrl(queue,out_queue)
		t.setDaemon(True)#设置为守护线程  
 		t.start()  
      
        #将网址都存放到queue队列中  
		for host in hosts:  
			queue.put(host)  
      
		for i in range(5):  
			dt = DatamineThread(out_queue)
			dt.setDaemon(True)  
			dt.start()  
      
		queue.join()#线程依次执行，主线程最后执行  
		out_queue.join()  
      
main()  