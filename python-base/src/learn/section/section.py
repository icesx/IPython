# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

if __name__ == '__main__':
    word = "123456"
    section1 = [word[:i] for i in range(len(word) + 1)]
    print(section1)
    section2 = [R[1:] for R in section1 if R]
    print(section2)
    section3 = [(word[:i],word[i:]) for i in range(len(word) + 1)]
    print(section3)
