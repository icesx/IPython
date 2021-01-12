# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import subprocess
import sys


def run_process(cmd):
    try:
        pstat = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    except Exception as e:
        print("Run script failed:(%s) ,exit run!" % e)
        sys.exit(1)
    else:
        pstat.wait()
        if pstat.returncode == 0:
            print("Run script Successful,exit code is %s" % pstat.returncode)
            lines = pstat.stdout.readlines()
            for line in lines:
                print("%s" % line.decode("utf-8").rstrip('\n'))
        else:
            print("Run script End,exit code is %s,With reason <%s>" % (
                pstat.returncode, pstat.stderr.read().rstrip('\n')))


if __name__ == '__main__':
    run_process("ls /")
