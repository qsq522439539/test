#!/usr/bin/env python
#coding=utf-8

import re


def getconfig(name):
	fh = open('config2.txt','r')
	if not fh:
		exit(4)
	fc = fh.read()
	fh.close()
	matchObj = re.match(r'(.*?)<TC=%s>(.*?)</TC>(.*)'%name,fc,re.M|re.S|re.I)
	if not matchObj:
		print 'not found paramater'
		exit(6)
	tcconfig = matchObj.group(2)
	if re.search(r'\s+COMMAND\s+.*', tcconfig):
		result, number = re.subn(r'.+COMMAND+\s','',tcconfig)
		result, number = re.subn(r'</PARA>', '', result)
		result = result.splitlines()
		result = result[1:-1]
	return result


def main():

	getconfig('MAX_UE')


if __name__ == "__main__":
	main()