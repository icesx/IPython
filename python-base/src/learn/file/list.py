# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import os


def list(callback,dir):
    _list = os.listdir(dir)
    for file in _list:
        callback(file)


if __name__ == '__main__':
    list(lambda file: print(file),"/home/i")
