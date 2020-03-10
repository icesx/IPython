# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import  struct
if __name__ == '__main__':
    p=struct.pack('hhl',1,2,3)
    up=struct.unpack('hhl',p)
    print(up)