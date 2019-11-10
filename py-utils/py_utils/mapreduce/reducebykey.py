# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

from functools import reduce


def reducebykey(function,source_list):
    grouped = groupbykey(source_list)
    return list(zip(grouped,map(lambda values: reduce(lambda v1,v2: function(v1,v2),values),grouped.values())))


def mapdict(function,source_list):
    print("source_list is:",source_list.values())
    return list(zip(source_list,map(lambda values: function(values),source_list.values())))


def groupbykey(source_list):
    grouped = {}
    for tu in source_list:
        key = grouped.get(tu[0],0)
        if key == 0:
            grouped.update({tu[0]: [tu[1]]})
        else:
            key.append(tu[1])
    return grouped
