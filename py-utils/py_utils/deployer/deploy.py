#!/bin/python
# coding=utf-8
import zipfile,os
import paramiko


class Deploy(object):

    def __init__(self,local_dir,host,remote_dir,user,password):

        print("init finish")
        self.SEP = "/"
        self.local_dir = local_dir
        self.remote_dir = remote_dir
        self.zip_path = local_dir + ".zip"
        self.folder = local_dir[local_dir.rindex(self.SEP) + len(self.SEP):]
        self.zip_name = self.folder + ".zip"
        self.password = password
        self.user = user
        self.host = host

    def connect_server(self,user_name,host):
        t = paramiko.Transport((host,22))
        t.connect(username=user_name,password=self.password)
        return t

    def scp_file(self):
        sftp = paramiko.SFTPClient.from_transport(self.connect_server(self.user,self.host))
        _remote_zip_path = self.remote_dir + self.SEP + self.zip_name
        print ('to scp file ' + self.zip_path + ' to ' + _remote_zip_path)
        sftp.put(self.zip_path,_remote_zip_path)
        sftp.close()
        return self

    def ssh_unzip(self):
        ssh = self.__ssh_connect()
        cmd = 'unzip -o -d ' + self.remote_dir + ' ' + self.__zip_name()
        print (cmd)
        return self.__exec_cmd(cmd,ssh)

    def __exec_cmd(self,cmd,ssh):
        stdin,stdout,stderr = ssh.exec_command(cmd);
        result = stdout.read()
        print (result)
        error = stderr.read()
        print (error)
        ssh.close()
        return self

    def __zip_name(self):
        return self.remote_dir + self.SEP + self.zip_name

    def __ssh_connect(self):
        paramiko.util.log_to_file("t_ssh.log")
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        paramiko.util.log_to_file("t_ssh.log")
        ssh.connect(self.host,22,self.user,self.password)
        return ssh

    def clean(self):
        ssh = self.__ssh_connect()
        cmd = "rm -rf " + self.__zip_name()
        return self.__exec_cmd(cmd,ssh)

    def zip(self,excludes={}):
        f = zipfile.ZipFile(self.zip_path,'w',zipfile.ZIP_DEFLATED)
        for dirpath,dirnames,filenames in os.walk(self.local_dir):
            for filename in filenames:
                exlude_ = dirpath.replace(self.local_dir + "/",'')
                if self.__include(exlude_,excludes):
                    file_path = os.path.join(dirpath,filename)
                    file_name = file_path.replace(self.local_dir,"")
                    f.write(file_path,self.folder + self.SEP + file_name)
                else:
                    print( "exclude," + exlude_)
        f.close()
        return self

    def __include(self,exclude,excludes):
        x = True
        for folder in excludes:
            if exclude.startswith(folder): x = False
        return x
