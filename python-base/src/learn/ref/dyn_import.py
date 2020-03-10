# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
class DynClass:
    def __init__(self,name):
        self.__name=name

    def name(self):
        return "dync..."+self.__name


def show_name():
    return "import name..."


def import_module():
    imp = "learn.ref.dyn_import"
    nc = __import__(imp,fromlist=True)
    print(nc)
    name = nc.show_name()
    print(name)


def import_class():
    imp = "learn.ref.dyn_import"
    nc = __import__(imp,fromlist=True)
    print(nc)
    f=getattr(nc,"DynClass")
    name = f("name").name()
    print(name)


if __name__ == '__main__':
    import_module()
    print("...............")
    import_class()
