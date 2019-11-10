# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

def function(name,time):
    print(name,time)


def function_outter(function,name,time):
    function(name,time)


if __name__ == '__main__':
    function_outter(function,"jinzhenge","2018")
    function_outter(lambda x,y: x + y,"jinzhenge","2018")
