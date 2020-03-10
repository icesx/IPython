# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
class A:
    __sex = 1

    def __init__(self):
        self.__name = "zhangsan"

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self,sex):
        self.__sex = sex

    def echo(self):
        print("i am %s,sex %d" % (self.__name,self.__sex))


if __name__ == '__main__':
    a = A()
    print(getattr(a,"name"))
    print(getattr(a,"sex"))
