# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import threading

import Queue
import urllib2


# called by each thread
def get_url(q,url):
    q.put(urllib2.urlopen(url).read())


theurls = ["http://baidu.com","http://qq.com"]

q = Queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url,args=(q,u))
    t.daemon = True
    t.start()

s = q.get()
print(s)
