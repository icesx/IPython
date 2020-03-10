# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import os

import pyinotify
from pyinotify import WatchManager,Notifier,ProcessEvent



class EventHandler(ProcessEvent):
    """事件处理"""

    def process_IN_CREATE(self,event):
        print("Create file: %s " % os.path.join(event.path,event.name))

    def process_IN_DELETE(self,event):
        print("Delete file: %s " % os.path.join(event.path,event.name))

    def process_IN_MODIFY(self,event):
        print("Modify file: %s " % os.path.join(event.path,event.name))

    def process_IN_ACCESS(self,event):
        print("Access file: %s " % os.path.join(event.path,event.name))

    def process_IN_ATTRIB(self,event):
        print("Access file: %s " % os.path.join(event.path,event.name))


class FileInotify():
    #inotify is implament by c ,this py is not used.
    def __init__(self,folder,event=EventHandler()):
        self.logger.info("create FileSystem...")
        self.path = folder
        self.eventHandler = event
        self.__monitor()

    def __monitor(self):

        wm = WatchManager()
        mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY | pyinotify.IN_ACCESS | pyinotify.IN_ATTRIB
        notifier = Notifier(wm,self.eventHandler)
        wm.add_watch(self.path,mask,rec=True)
        print('now starting monitor %s',self.path)
        while True:
            try:
                notifier.process_events()  # 绑定处理event方法
                if notifier.check_events():  # 检查是否有有可读取的新event
                    notifier.read_events()  # 读取event，交给EventHandler处理
            except KeyboardInterrupt:
                notifier.stop()
                break
