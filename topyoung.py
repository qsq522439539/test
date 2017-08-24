#!/usr/bin/env python
#coding=utf-8

import socket
import time
import threading

HOST='192.168.0.254'
PORT=1000
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

def setATTvalue1(channel,channe2,minvalue,maxvalue):
	for i in range(1):
		for j in range(minvalue,maxvalue,1):
			time.sleep(1)
			s.sendall('SET:%s:%s\r\n' % (str(channel), str(j)))
			s.sendall('SET:%s:%s\r\n' % (str(channe2), str(j)))
			data = s.recv(1024)
			print 'Received', repr(data)
		for j in range(maxvalue,minvalue,-1):
			time.sleep(1)
			s.sendall('SET:%s:%s\r\n' % (str(channel), str(j)))
			s.sendall('SET:%s:%s\r\n' % (str(channe2), str(j)))
			data = s.recv(1024)
			print 'Received', repr(data)
	s.close()
		
def setATTvalue2(channel, minvalue, maxvalue):
	value = maxvalue
	while (value > minvalue):
		s.sendall('SET:%s:%s' % (str(channel), str(value)))
		data = s.recv(1024)
		print 'Received', repr(data)
		value -= 1
		time.sleep(1)

	while (value < maxvalue):
		s.sendall('SET:1:value')
		data = s.recv(1024)
		print 'Received', repr(data)
		value += 1
		time.sleep(1)


if __name__ == "__main__":
	threadlist = list()
	threadlist.append(threading.Thread(target=setATTvalue1(1,0,30)))
	threadlist.append(threading.Thread(target=setATTvalue2(2,0,30)))
	for thread in threadlist:
		thread.start()
	for thread in threadlist:
		thread.join()
