# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

if __name__ == '__main__':
    from py_utils.file.file import FileOpreation
    fo=FileOpreation()
    fo.recursive("/home/i/Downloads",callback=lambda path:print(path))