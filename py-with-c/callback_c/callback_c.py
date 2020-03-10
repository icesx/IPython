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
    # order must same with so
    _fields_ = [
        ("id",c_long),
        ("name",c_char_p),
        ("age",c_int)
    ]


def callback(age):
    print("callback age:",age)


def ivoke_struct():
    info = Info()
    info.age = 1
    info.name = b"xxx"
    info.id = 1111
    so.ivoke_2.restype = Info
    CALLBACK=CFUNCTYPE(None,c_int)
    age = so.ivoke_2(info,CALLBACK(callback))
    so.ivoke.restype = Info
    print("ivoke_2 from so age is",age.age)
    name="zhangsan"
    info2=so.ivoke(c_int(1),bytes(name, encoding = "utf8"))
    print("ivoke from so name is",str(info2.name,encoding = "utf8"))


