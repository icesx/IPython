# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import numpy as np


def normalize(data):
    m = np.mean(data)
    mx = max(data)
    mn = min(data)
    return [(float(i) - m) / (mx - mn) for i in data]


def max_normalize(data,key):
    mx = max(data,key=key)
    return map(lambda item: (item,float(key(item)) / key(mx)),data)
