# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import numpy as np

import py_utils.mapreduce.reducebykey as rdk

def test_base():
    all = [("a",1),("a",2),("b",1),("c",2),("a",6),("d",1),("b",3)]
    print(rdk.reducebykey(lambda v1,v2: (v1 + v2),all))
    grouped = rdk.groupbykey(all)
    print(grouped)
    _grouped = rdk.mapdict(np.mean,grouped)
    print(_grouped)


def test_complex():
    all = [("a",[1,2]),("a",[2,4]),("b",[1]),("c",[2]),("a",[6]),("d",[1]),("b",[3])]
    print(rdk.reducebykey(lambda v1,v2: (v1 + v2),all))
    grouped = rdk.groupbykey(all)
    print(grouped)


if __name__ == '__main__':
    test_base()
    # test_complex()
