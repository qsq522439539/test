#!/usr/bin/env python
#coding=utf-8

import psutil

def get_process_cmdline(process_name):
	'''
	获取进程的命令行
	:param process_name: 进程名
	:return:返回该进程名（可能有多个）的各进程的参数
	'''
	pid_list = psutil.pids()
	for each_pid in pid_list:
		try:
			each_pro = psutil.Process(each_pid)
			if each_pro.name().lower() == process_name.lower():
				yield each_pro.cmdline()
		except psutil.NoSuchProcess, pid:
			print("no process found with pid=%s"%pid)
			
def kill_process(process_name):
	'''
	杀死进程
	:param process_name: 进程名
	:return:None
	'''
	pid_list = psutil.pids()
	for each_pid in pid_list:
		try:
			each_pro = psutil.Process(each_pid)
			if each_pro.name().lower() == process_name.lower():
				print("found process")
				print("process_name=%s"%each_pro.name())
				print('process_exe=%s'%each_pro.exe())
				print('process_cwd=%s'%each_pro.cwd())
				print('process_cmdline=%s'%each_pro.cmdline())
				print('process_status=%s'%each_pro.status())
				print('process_username=%s'%each_pro.username())
				print('process_createtime=%s'%each_pro.create_time())
				print('now will kill this process')
				each_pro.terminate()
				each_pro.wait(timeout=3)
				print('psutil.test():\n%s'%psutil.test())
		except psutil.NoSuchProcess, pid:
			print("no process found with pid=%s"%pid)

if __name__ == "__main__" :
	pnum = psutil.pids()
	for pnum in psutil.pids():
		p = psutil.Process(pnum)
		print u"进程名 %-20s  内存利用率 %-18s 进程状态 %-10s 创建时间 %-10s " % (
		p.name(), p.memory_percent(), p.status(), p.create_time())
	kill_process('chromedriver.exe')
