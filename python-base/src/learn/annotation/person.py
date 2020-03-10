# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
class Person(object):
    def __init__(self):
        self.__name = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name
        return self


if __name__ == '__main__':
    p = Person()
    p.name = "namexx"
    print(p.name)
