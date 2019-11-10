# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
def map_fun(x):
    return x * 2


if __name__ == '__main__':
    for i in map(str,[1,2,3,4,5,6,7,8,9]):
        print(i)
    print(map(map_fun,range(6)))
