# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

from py_utils.math.normal import normalize,max_normalize

if __name__ == '__main__':
    l = [("a",1),("b",2),("c",3),("d",4),("e",5)]
    print(max(l,key=lambda x:x[1]))
    # print(normalize(l))
    for x in max_normalize(l,key=lambda x: x[1]):
        print(x)
