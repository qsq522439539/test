#!/usr/bin/env python
#coding=utf-8

import paramiko
import sys,os
import re
import time
from getconfig import getconfig
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

hostname = '192.168.103.59'         #LMT IP
ENB_ADMIN_USERNAME = 'admin'		#username
ENB_ADMIN_KEY = 'admin'				#password
tcname = 'MAX_UE'
MAX_UE_VALUE1 = []                  #get value
MAX_UE_VALUE2 = []
MAX_UE_value1 = [32,38,2,6,8,8,2,12,0]  #expected value
MAX_UE_value2 = [96,100,4,6,8,8,2,4,1]
driver = webdriver.Chrome()

def openBrowser():
	driver.get('http://'+hostname)
	driver.maximize_window()
	WebDriverWait(driver, 30, 0.5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='header_login']")))
	
def login():
	driver.find_element_by_id("username").clear()
	driver.find_element_by_id("username").send_keys("admin")
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys("admin")
	driver.find_element_by_id("log_button").click()
	#wait my_menu element presence
	WebDriverWait(driver, 30, 0.5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='my_menu']")))

#  LTE_96_UE_ENABLE   index=1 ==>close    index=0 ==>open
def MAX_UE(index):
	driver.find_element_by_xpath("//*[@id='my_menu']/div[5]/a[5]").click()
	WebDriverWait(driver, 5, 0.5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='main_internal_container']")))
	driver.find_element_by_xpath("//*[@id='96UE_fieldset']/legend/span").click()
	MAX_UE = driver.find_element_by_xpath("//*[@id='LTE_96_UE_ENABLE']")
	Select(MAX_UE).select_by_index(index)
	driver.find_element_by_xpath("//*[@id='save_button']").click()
	time.sleep(5)
	a = driver.switch_to_alert()
	data = a.text
	if re.match(u'数据未更改',data) :
		print data
		a.accept()
	elif re.match(u'配置成功',data) :
		print data
		a.accept()
		driver.find_element_by_xpath("//*[@id='Loki_reboot']").click()
		driver.find_element_by_xpath("//*[@id='reboot_button']").click()
		WebDriverWait(driver, 300, 0.5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='header_login']")))
		login()
	else:
		print 'no such alert exists'
		
def execute_linuxcmd(command, hostname, username='root', password='root123', port=27149):
	'''
	Set the basic configuration in cli.txt.
	hostname: the conneced host IP address
	username: login host name
	password: login host password
	path: storage path of the configuration script and log
	'''
	port = int(port)
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname, port, username, password)
	stdin, stdout, stderr = client.exec_command("%s" % command)
	message = stdout.read()
	client.close()
	return message

def main():
	
	openBrowser()
	
	login()
	
	MAX_UE(1)
	
	Command = getconfig(tcname)
	
	for command in Command:
		VALUE = int(execute_linuxcmd(command,hostname))
		MAX_UE_VALUE1.append(VALUE)
	print MAX_UE_VALUE1
	if 	MAX_UE_VALUE1 == MAX_UE_value1:
		print '关闭96UE开关时，参数配置正确'
		
		MAX_UE(0)
		
		for command in Command:
			VALUE = int(execute_linuxcmd(command,hostname))
			MAX_UE_VALUE2.append(VALUE)
		print MAX_UE_VALUE2
		if MAX_UE_VALUE2 == MAX_UE_value2:
			print '打开96UE开关时，参数配置正确'
			return True
		else:
			print '打开96UE开关时，参数配置错误'
			return False
	else :
		print '关闭96UE开关时，参数配置错误'
		return False
		
if __name__ == "__main__":
	main()