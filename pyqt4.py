#!/usr/bin/env python
#coding=utf-8

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore





if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	b = QtGui.QPushButton("HELLO")
	b.show()
	app.connect(b,QtCore.SIGNAL('clicked()'),app,QtCore.SLOT('quit()')) #信号和槽机制，SIGNAL是b的信号，SLOT是app的槽
	app.exec_()
	
	
	
	'''
	1.一个信号可以连接另一个信号。(object1,QtCore.SIGNAL(),object2,QtCore.SIGNAL()) object1发射的信号触发object2发射信号
	2.一个信号连接多个槽。(object1,QtCore.SIGNAL(),object2,QtCore.SIGNAL())  (object1,QtCore.SIGNAL(),object3,QtCore.SIGNAL())
	3.一个槽响应多个信号。(object1,QtCore.SIGNAL(),object2,QtCore.SIGNAL()) (object3,QtCore.SIGNAL(),object2,QtCore.SIGNAL())
	
	'''