# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.random.rand(10)
    print(x)
    y = np.random.rand(10)
    plt.figure()
    p2 = plt.scatter(x,y,marker='+',color='c',label='2',s=50)
    plt.xlabel("time(s)")
    plt.ylabel("value(m)")
    plt.title("line")
    plt.show()
