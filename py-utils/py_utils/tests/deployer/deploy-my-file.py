# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from deployer.deploy import Deploy


def main():
    print "please input the conrect param as : python deploy.py root@xx.xx.xx.xx:/temp /home/user/Downloads/log4py-1.3.zip log4py-1.3_xxxx.zip"
    remote_dir = "/home/pi/"
    local_dir = "/ICESX/workSpacePython/py-remote-deployer"
    deploy = Deploy(local_dir,host="192.168.31.60",remote_dir=remote_dir,user="pi",password="raspberry")
    deploy.zip().scp_file().ssh_unzip()


if __name__ == '__main__':
    main()
