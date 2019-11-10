# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import matplotlib.pyplot as plt


def f(x):
    return x ** 3 - x ** 2 + 9


if __name__ == '__main__':
    X = list((x) for x in range(1,100))
    Y = map(lambda x: f(x),X)
    plt.figure(figsize=(20,15))  # 创建绘图对象
    plt.plot(X,Y,"bx",linewidth=1)  # 在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
    plt.xlabel("Time(s)")  # X轴标签
    plt.ylabel("Volt")  # Y轴标签
    plt.title("Line plot")  # 图标题
    plt.show()  # 显示图
