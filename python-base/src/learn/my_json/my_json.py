# Copyright (C)
# Author: I
# Contact: 12157724@qq.com


import json


def dumps():
    data = [{'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}]
    print(json.dumps(data))


def loads():
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
    text = json.loads(jsonData)
    print(text.get("a"),text.get("b"),text.get("c"))


def create():
    dic = dict(name="i",age="18")
    t = json.dumps(dic)
    print(t)


if __name__ == '__main__':
    dumps()
    loads()
    create()
