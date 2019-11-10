# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

class With_class:
    def __init__(self):
        print("init")

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        print("exit!")

    def dosome(self):
        print("do something!")


class Sample:
    def __enter__(self):
        print('in enter')
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        print("type: ",exc_type)
        print("val: ",exc_val)
        print("tb: ",exc_tb)

    def do_something(self):
        bar = 1 / 0
        return bar + 10
