# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
if __name__ == '__main__':
    a = [1,2,3,4,6,7,3,9,8]
    newList = [x for x in a]
    print(newList)
    newList2 = [x for x in a if x % 2 == 0]
    print(newList2)
