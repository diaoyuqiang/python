#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
import paramiko
import time

SELF_HOST = "127.0.0.1"
SSH_HOST = "127.0.0.1"
SSH_PORT = "2223"
SSH_NAME = "quicktron"
SSH_PWD = "quicktron"

OS_TYPE = platform.platform().split('-')[0].lower()

class CMD_Executor:
    def __init__(self):
        if OS_TYPE == "linux":
            try:
                self.sshClient = paramiko.SSHClient()
                self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.sshClient.connect(hostname=SELF_HOST, port=eval(SSH_PORT), username=SSH_NAME, password=SSH_PWD)
                self.ssh = self.sshClient.invoke_shell()
                if SSH_NAME != 'root':
                    time.sleep(0.1)
                    self.ssh.send('sudo su \n')
                    buff = ''
                    if "aarch64" not in platform.platform():
                        while not buff.endswith('/home/quicktron# '):
                            resp = self.ssh.recv(9999).decode()
                            buff += resp
                    else:
                        while not buff.endswith('{0}: '.format(SSH_NAME)):
                            resp = self.ssh.recv(9999).decode()
                            buff += resp
                    self.ssh.send(SSH_PWD)
                    self.ssh.send('\n')
                    print("ssh 连接成功")
            except Exception as e:
                print(e)


    def send(self,cmd):
        """
         执行宿主机 cmd 命令
        :return:
        """
        try:
            if self.ssh:
                buff = ''
                self.ssh.send(cmd + '\n')
                print(cmd)
                while not buff.endswith('quicktron# '):
                    buff += self.ssh.recv(9999).decode()
            else:
                print("ssh 连接失败")
        except Exception as e:
            print(e)

    def close(self):
        self.sshClient.close()
        print("ssh 连接关闭成功")