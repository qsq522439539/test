#!/usr/bin/env python
#coding=utf-8

"""
    Mobility container client class

    @precondition: Mobility container hardware box
    @precondition: Mobility container simulator installed on the PC
    @precondition: MobilitySimulator.exe is located under C:\Program Files\MobilitySimulator\

    TEST RESULTS::
        Max speed = 256
        Min speed = ~5
        Negative speed = min speed
        Erroneous xml and erroneous strings are discarded
        Mobility container allows attenuation >100, which can give incorrect
        Only one script per socket.send

"""
import socket
import os
import time  # For sleep(), if required
import random
import win32api, win32pdhutil, win32con
from struct import unpack, pack
import xlrd

currentDir = os.getcwd()

class MobilityContainer:
	def setAttenuator(self,  channel1, value1, channel2, value2):
		"""
			Set a specific attenuator to a specific value.
			attenuatorName: 'WCDMA' or 'GSM'.
			value: Value is an integer between 0 and 100.
		"""
		host = "127.0.0.1"
		port = 2008
		path = r'C:\Program Files\MobilitySimulator\MobilitySimulator.exe'
		os.startfile(path)
		print("Connecting to " + host + ", port " + str(port))
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		count = 0
		while (count < 20):  # trying to connect for 20 seconds
			try:
				s.connect((host, port))
				break
			except socket.error:
				time.sleep(1)
				count = count + 1
			# print '%d' %count
		recv_port = unpack('>I', s.recv(4))[0]
		print 'recv_port = %d' % recv_port
		receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		receiver.connect((host, recv_port))
		version = 1
		bytes = pack('>I', version)
		s.send(bytes)
		print 'Mobility Container -- setup successful'
		
		cmd1 = '<attenuator><name>' + channel1 + '</name><value>' + str(value1) + '</value></attenuator>'
		cmd2 = '<attenuator><name>' + channel2 + '</name><value>' + str(value2) + '</value></attenuator>'
		print'sending \'' + cmd1 + '\''
		bytes = pack('>I', len(cmd1))
		s.send(bytes)
		s.send(cmd1)
		time.sleep(5)
		print'sending \'' + cmd2 + '\''
		bytes = pack('>I', len(cmd2))
		s.send(bytes)
		s.send(cmd2)
		time.sleep(5)
		
if __name__ == "__main__":
	


