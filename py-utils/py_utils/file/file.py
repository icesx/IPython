# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import os


class FileOpreation():
    def list(self,dir,callback):
        _list = os.listdir(dir)
        for file in _list:
            callback(dir+"/"+file)

    def recursive(self,dir,filter=lambda path:True,callback=lambda path:None):
        for file in os.listdir(dir):
            path = dir + "/" + file
            if os.path.isdir(path):
                self.recursive(path,filter,callback)
            else:
                if filter(path):
                    callback(path)
