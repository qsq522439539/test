#!/usr/bin/env python
#coding=utf-8
import sys
from PyQt4 import QtGui, QtCore
import psutil
import atexit

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

class InputDlg(QtGui.QDialog):
	def __init__(self, parent = None):
		super(InputDlg, self).__init__(parent)
		
		self.nameLabel1=QtGui.QLabel(self.tr("进程名"))
		self.nameLabel1.setFrameStyle(QtGui.QFrame.Box|QtGui.QFrame.Box)
		self.nameLabel1.setLineWidth(1)
		self.nameLabel1.setMidLineWidth(0)
		
		self.nameLabel2=QtGui.QLabel("chromedriver")
		self.nameLabel2.setFrameStyle(QtGui.QFrame.Box|QtGui.QFrame.Box)
		self.nameLabel2.setLineWidth(1)
		self.nameLabel2.setMidLineWidth(0)
		
		Button = QtGui.QPushButton(self.tr("运行"))
		
		self.connect(Button, QtCore.SIGNAL("clicked()"), self.killprocess)
		
		layout = QtGui.QGridLayout()
		layout.addWidget(self.nameLabel1, 0, 0)
		layout.addWidget(self.nameLabel2, 0, 1)

		layout.addWidget(Button, 0, 2)
		
		self.setLayout(layout)
		self.resize(250, 150)
		self.setWindowTitle(self.tr("杀进程"))

		
	def killprocess(self, process_name = 'chromedriver.exe'):
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
					print("process_name=%s" % each_pro.name())
					print('process_exe=%s' % each_pro.exe())
					print('process_cwd=%s' % each_pro.cwd())
					print('process_cmdline=%s' % each_pro.cmdline())
					print('process_status=%s' % each_pro.status())
					print('process_username=%s' % each_pro.username())
					print('process_createtime=%s' % each_pro.create_time())
					print('now will kill this process')
					each_pro.terminate()
					each_pro.wait(timeout=3)
					print('psutil.test():\n%s' % psutil.test())
			except psutil.NoSuchProcess, pid:
				print("no process found with pid=%s" % pid)



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = InputDlg()
	main.show()
	sys.exit(app.exec_())