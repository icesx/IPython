# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import numpy as np

x = np.array([[1,2,3],[4,5,6]])
print(np.tile(x,(1,3)))
print(np.tile(x,(3,1)))
print(np.tile(x,(3,3)))
