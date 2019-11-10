#!/bin/python
# coding=utf-8
'''
Created on 2014年5月17日

@author: i
'''


def method(a,b,*c):
    print(a)
    print(b)
    print("length of c is: %d " % len(c))
    for i in c:
        print(i)


if __name__ == "__main__":
    print("__main__")
    method("a","b","c","d","e")
