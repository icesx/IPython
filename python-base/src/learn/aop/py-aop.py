#!/bin/python
# coding=utf-8
'''
Created on 2014年5月17日

@author: i
'''


class py_aop:
    def __method(self,param):
        print("method with " + param)

    def method(self,param):
        self.__proxy(self.__method,param)

    def __proxy(self,method,param):
        print("proxy begin")
        method(param)
        print("proxy end")


if __name__ == "__main__":
    print("__main__")
    py_aop().method("parm")
