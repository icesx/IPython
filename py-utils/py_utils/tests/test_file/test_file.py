# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from py_utils.file.file import FileOpreation
if __name__ == '__main__':
    FileOpreation().list("/ICESX/workSpaceBjrdc/company/assessment/2020/年度",callback=lambda f:print(f))