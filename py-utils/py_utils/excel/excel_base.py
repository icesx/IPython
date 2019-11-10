# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import os


class ExcelBase():
    def __init__(self,file):
        self.file = file
        print("try open file",file)

    def __check_file(self):
        if os.path.exists(self.file):
            pass
        else:
            print("file not exists,to create it")
            os.open(self.file,"w")
            os.close(self.file)
