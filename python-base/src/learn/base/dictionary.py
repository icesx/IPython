# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

def dict_base():
    dict_ = {'Name': 'Zara','Age': 7,'Class': 'First','Name':"xx"};
    print("dict['Name']: ",dict_.get('Name'))
    print("dict['Age']: ",dict_.get('Age'))
    print("x",dict_.get("x",0))
    dict_.update({"x": "x1"})
    print(dict_)


def dict_fine():
    dic = dict(name="Zara",Age=7,Class="First")
    print(dic["name"])
    print(dic["Age"])


if __name__ == '__main__':
    dict_base()
    print("--------------")
    dict_fine()
