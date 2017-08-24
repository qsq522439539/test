#!/usr/bin/env python
#coding=utf-8

import sys
from PyQt4 import QtGui,QtCore


class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		
		self.initUI()
	
	def initUI(self):
		
		textEdit = QtGui.QTextEdit()
		self.setCentralWidget(textEdit)
		
		exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)
		
		self.statusBar()
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)
		
		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAction)
		
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Main window')
		self.show()

		
	def center(self): #居中
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		
	# def closeEvent(self, event):
	#
	# 	reply = QtGui.QMessageBox.question(self, 'Message',
	# 	                                   "Are you sure to quit?", QtGui.QMessageBox.Yes |
	# 	                                   QtGui.QMessageBox.No, QtGui.QMessageBox.No)
	#
	# 	if reply == QtGui.QMessageBox.Yes:
	# 		event.accept()
	# 	else:
	# 		event.ignore()
def main():
# 	app = QtGui.QApplication(sys.argv)
# 	'''每个PyQt4应用程序必须创建一个应用程序对象。
# 	应用程序对象位于QtGui模块中。该sys.argv参数是命令行中的参数列表。
# 	Python脚本可以从shell运行。这是我们如何控制我们的脚本启动的一种方式。'''
# 	w = QtGui.QWidget()
# 	w.resize(550, 150) #宽、高
# 	w.move(300, 300)   #坐标x = 300, y = 300
# 	w.setWindowTitle('Simple') #标题
# 	w.show()
#
# 	sys.exit(app.exec_())
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
	