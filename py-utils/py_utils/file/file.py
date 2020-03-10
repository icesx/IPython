# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import os


class FileOpreation():
    def list(self,callback,dir):
        _list = os.listdir(dir)
        for file in _list:
            callback(file)

    def recursive(self,filter,callback,dir):
        for file in os.listdir(dir):
            path = dir + "/" + file
            if os.path.isdir(path):
                self.recursive(callback,path)
            else:
                if filter(path):
                    callback(path)
