#!/usr/bin/env python
#coding=utf-8

import paramiko
import sys,os
import time
import re
import string

def execute_clicomand(hostname, username, password, port, command):
	'''
	Set the basic configuration in cli.txt.

	hostname: the conneced host IP address

	username: login host name

	password: login host password

	path: storage path of the configuration script and log
	'''
	cmd_ps_oam = "ps -ef | grep oam;"
	cmd_profile = "source /etc/profile;"
	local_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
	
	port = int(port)
	
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname, port, username, password)
	'''
	function:判断oam进程是否存在
	parameter:
		file_cli: cli命令文件
		file_cliout: cli命令执行结果日志
		oam_set_cmdï�?按行读取cli命令文件
	'''
	for i in range(5):
		time.sleep(5)
		stdin_ps_oam, stdout_ps_oam, stderr_ps_oam = client.exec_command(cmd_profile + cmd_ps_oam)
		oamout_ps_oam = stdout_ps_oam.read()
		if "/tmp/sbin/oam" not in oamout_ps_oam:
			# print oamout_ps_oam
			continue
		else:
			stdin, stdout, stderr = client.exec_command("%s" % command)
			message = stdout.read()
			return message
	client.close()
	
def main():
	a = string.letters + string.digits
	a = a*600
	cmd = '''(echo %s >> /mnt/temper/TempLog.txt) '''%a
	b = execute_clicomand(hostname = '192.168.107.220',username='root',password='root123',port=27149,command = cmd)
	print b


if __name__ == "__main__":
	main()