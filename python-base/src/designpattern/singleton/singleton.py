# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls,*args,**kwargs):
        if not isinstance(cls.__instance,cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance


class SingletonMeta(object):
    def __init__(self):
        self.instance = None

    def __call__(cls,*args,**kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args,**kwargs)
        else:
            print("instance already existed!")
        return cls.instance

class NotSingleton(object):
    pass


if __name__ == '__main__':
    for i in range(1,10):
        print("singleton:%s" % Singleton())
        print("not singleton%s" % NotSingleton())
