# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
#
#
# yield retrun value ,next continue
def foo(num):
    print("starting...")
    num = 4
    print("numxx")
    while num < 10:
        print("num:", num)
        num = num + 1
        yield num
        num = num + 1
        print("after yield", num)


for n in foo(0):
    print("outter", n)

gennerator = (x * x for x in range(3))
print("gennerator", next(gennerator))
print("gennerator", next(gennerator))


def sample():
    yield 1
    yield 2
    yield [3, 4, 5]
    yield from [6, 7, 8]
    yield 9


for i in sample():
    print("sample", i)


def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i * i


cg = create_generator()
print(cg)
for i in cg:
    print("cg", i)


###yeild from
def b():
    r = yield from c()


def c():
    yield from [1, 2, 3]


for i in b():
    print("yield from ", i)
