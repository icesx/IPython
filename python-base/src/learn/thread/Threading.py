# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import threading
import time

if __name__ == '__main__':
    def print_time(threadName,delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s: %s" % (threadName,time.ctime(time.time())))


    try:
        threading.start_new_thread(print_time,("Thread-1",2,))
        threading.start_new_thread(print_time,("Thread-2",4,))
    except:
        print("Error: unable to start thread")

    while 1:
        pass
