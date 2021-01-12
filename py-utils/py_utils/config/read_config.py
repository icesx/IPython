# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import configparser


class ConfigIni():
    def __init__(self, file):
        self.__config = configparser.ConfigParser()
        self.__config.read(file)

    def get(self, section, key):
        return self.__config.get(section, key)

    def getEval(self, section, key):
        return eval(self.get(section, key))

    def sections(self):
        return self.__config.sections()


if __name__ == '__main__':
    ci = ConfigIni("config.ini")
    print(ci.sections())
    array = ci.getEval("array", "array_a")
    for i in array:
        print(i)
    base = ci.get("base", "base_a")
    print(eval(base))
    dict = ci.getEval("dict", "dict_a")
    print(dict.get("key"))
