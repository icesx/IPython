# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from ctypes import *
from ctypes import cdll

so = cdll.LoadLibrary("/ICESX/workSpaceC/IC/PythonWithC/Debug/libPythonWithC.so")


def ivoke_so():
    x = so.ivoke_base(10)
    print("ivoked result is",x)


class Info(Structure):
    #order must same with so
    _fields_ = [
        ("id",c_long),
        ("name",c_char_p),
        ("age",c_int)
    ]
def ivoke_struct():
    info = Info();
    info.age = 1;
    info.name = b"xxx";
    info.id = 1111;
    so.ivoke_2.restype = Info;
    age = so.ivoke_2(info)
    print("ivoke from so age is",age.age)
