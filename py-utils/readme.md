py-utils
==================

some python utils

requirement and  tested on : puthon3.6 and ubuntu18.04. 

##install:
```bash
python setup.py install --user
```

##deployer
1. use by code 
```python
from py_utils.deployer.deploy import Deploy


def main():
    print "please input the conrect param as : python deploy.py root@xx.xx.xx.xx:/temp /home/user/Downloads/log4py-1.3.zip log4py-1.3_xxxx.zip"
    remote_dir = "/home/pi/"
    local_dir = "/ICESX/workSpacePython/py-remote-deployer"
    deploy = Deploy(local_dir,host="192.168.31.60",remote_dir=remote_dir,user="pi",password="raspberry")
    deploy.zip().scp_file().ssh_unzip()

```
2. use by shell
```python
    python main.py  
    /home/me/test 
    --password= 
    --host=192.168.10.60 
    --user=pi 
    --remote_dir=/home/pi

```
##mapreduce