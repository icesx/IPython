# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import subprocess


class Rsync():
    def __init__(self, target, arg="-av"):
        self.__target = target
        self.__arg = arg

    def do_rsync(self, src):
        try:
            print("rsync from %s to %s" % src % self.__target)
            command = "/usr/bin/rsync " + self.__arg + " " + src + " " + self.__target
            pstat = subprocess.Popen(command, shell=True)
        except Exception as e:
            print(e)
