# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [0,1]
    y = [0,1]
    plt.figure()
    plt.plot(x,y)
    plt.xlabel("time(s)")
    plt.ylabel("value(m)")
    plt.title("line")
    plt.show()
