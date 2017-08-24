#!/usr/bin/env python
#coding=utf-8
# gridlayout.py
import sys
from PyQt4 import QtGui, QtCore

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))
# #滑块改变LCD显示数字
# class SigSlot(QtGui.QWidget):
#     def __init__(self, parent = None):
#         QtGui.QWidget.__init__(self, parent)
#         self.setWindowTitle('signal & slot')
#         lcd = QtGui.QLCDNumber(self)
#         slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
#         vbox = QtGui.QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(slider)
#         self.setLayout(vbox)
#         self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), lcd,QtCore.SLOT('display(int)')) #滑块的valueChanged信号连接到lcd的display上
#         self.resize(250, 150)
#
# #网格布局
# class GridLayout(QtGui.QWidget):
#     def __init__(self, parent = None):
#         QtGui.QWidget.__init__(self)
#         self.setWindowTitle('grid layout')
#         names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
#         '4', '5', '6', '*', '1', '2', '3',
#         '-', '0', '.', '=', '+']
#         grid = QtGui.QGridLayout()
#         j = 0
#         pos = [(0, 0), (0, 1), (0, 2), (0, 3),
#         (1, 0), (1, 1), (1, 2), (1, 3),
#         (2, 0), (2, 1), (2, 2), (2, 3),
#         (3, 0), (3, 1), (3, 2), (3, 3),
#         (4, 0), (4, 1), (4, 2), (4, 3)]
#         for i in names:
#             button = QtGui.QPushButton(i)
#             if j == 2:
#                 grid.addWidget(QtGui.QLabel(''), 0, 2)
#             else:
#                 grid.addWidget(button, pos[j][0], pos[j][1])
#             j = j + 1
#         self.setLayout(grid)
# #重写事件，按ESC退出
# class Escape(QtGui.QWidget):
#     def __init__(self, parent = None):
#         QtGui.QWidget.__init__(self)
#         self.setWindowTitle('escape')
#         self.resize(250, 150)
#         self.connect(self, QtCore.SIGNAL('closeEmitApp()'),
#         QtCore.SLOT('close()'))
#     def keyPressEvent(self, event):
#         if event.key() == QtCore.Qt.Key_Escape:
#             self.close()
# #发射信号
# class Emit(QtGui.QWidget):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self)
# 		self.setWindowTitle('emit')
# 		self.resize(250, 150)
# 		self.connect(self, QtCore.SIGNAL('closeEmitApp()'),QtCore.SLOT('close()'))
#
# 	def mousePressEvent(self, event):
# 		self.emit(QtCore.SIGNAL('closeEmitApp()'))
# #预定义对话框
# class InputDialog(QtGui.QWidget):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self)
# 		self.setGeometry(300, 300, 350, 80)
# 		self.setWindowTitle('InputDialog')
# 		self.button = QtGui.QPushButton('Dialog', self)
# 		self.button.setFocusPolicy(QtCore.Qt.NoFocus) #焦点 Qt::TabFocus 接受Tab键焦点 Qt::ClickFocus 接受鼠标单击做焦点 Qt::StrongFocus	TabFocus | ClickFocus |接受Tab键和鼠标单击做焦点
# 		self.button.move(20, 20)                      #Qt::WheelFocus	StrongFocus | 滑轮作为焦点选中事件 Qt::NoFocus 不接受焦点
# 		self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
# 		self.setFocus()
# 		self.label = QtGui.QLineEdit(self)
# 		self.label.move(130, 22)
# 	def showDialog(self):
# 		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog','Enter your name:')
# 		if ok:
# 			self.label.setText(unicode(text))
#
# #颜色对话框
# class ColorDialog(QtGui.QWidget):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self)
# 		color = QtGui.QColor(0, 0, 0)
# 		self.setGeometry(300, 300, 250, 180)
# 		self.setWindowTitle('ColorDialog')
# 		self.button = QtGui.QPushButton('Dialog', self)
# 		self.button.setFocusPolicy(QtCore.Qt.NoFocus)
# 		self.button.move(20, 20)
# 		self.connect(self.button, QtCore.SIGNAL('clicked()'), self.showDialog)
# 		self.setFocus()
# 		self.widget = QtGui.QWidget(self)
# 		self.widget.setStyleSheet('QWidget {background-color: %s}' %
# 		color.name())
# 		self.widget.setGeometry(130, 22, 100, 100)
# 	def showDialog(self):
# 		col = QtGui.QColorDialog.getColor()
# 		if col.isValid():
# 			self.widget.setStyleSheet('QWidget {background-color: %s}' %col.name())
#
# #字体对话框
# class FontDialog(QtGui.QWidget):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self)
# 		hbox = QtGui.QHBoxLayout()
# 		self.setGeometry(300, 300, 250, 110)
# 		self.setWindowTitle('FontDialog')
# 		button = QtGui.QPushButton(self.tr('选择字体'), self)
# 		button.setFocusPolicy(QtCore.Qt.NoFocus)
# 		button.move(20, 20)
# 		hbox.addWidget(button)
# 		self.connect(button, QtCore.SIGNAL('clicked()'), self.showDialog)
# 		self.label = QtGui.QLabel('Knowledge only matters', self)
# 		self.label.move(130, 20)
# 		hbox.addWidget(self.label, 1) #该语句将 labe 标签加入到 hbox 布局中，并通过第二个参数 1 设置 label 的大小是可变
# 		self.setLayout(hbox)          #的。该设置是必须的，因为在用户选择不同的字体时，label 标签中的字体可能会变大，若
# 	def showDialog(self):             #不进行该设置，标签中的内容就可能不会被全部显示。
# 		font, ok = QtGui.QFontDialog.getFont()
# 		if ok:
# 			self.label.setFont(font)
#
# #文件对话框
# class OpenFile(QtGui.QMainWindow):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self, parent)
# 		self.setGeometry(300, 300, 350, 300)
# 		self.setWindowTitle('OpenFile')
# 		self.textEdit = QtGui.QTextEdit()
# 		self.setCentralWidget(self.textEdit)
# 		self.statusBar()
# 		self.setFocus()
# 		exit = QtGui.QAction(QtGui.QIcon('icons/open.png'), 'Open', self)
# 		exit.setShortcut('Ctrl+O')
# 		exit.setStatusTip('Open new file')
# 		self.connect(exit, QtCore.SIGNAL('triggered()'), self.showDialog)
# 		menubar = self.menuBar()
# 		file = menubar.addMenu('&File')
# 		file.addAction(exit)
# 	def showDialog(self):
# 		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './') #弹出对话框标题栏、目录
# 		file = open(filename)       #显示文件内容
# 		data = file.read()
# 		self.textEdit.setText(data)
#
# #单选框
# class CheckBox(QtGui.QWidget):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self, parent)
# 		self.setGeometry(300, 300, 250, 150)
# 		self.setWindowTitle('Checkbox')
# 		self.cb = QtGui.QCheckBox('Show title', self)
# 		self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
# 		self.cb.move(10, 10)
# 		self.cb.toggle() #选上单选框
# 		self.connect(self.cb,QtCore.SIGNAL('stateChanged(int)'),self.changeTitle)
# 	def changeTitle(self, value):
# 		if self.cb.isChecked():
# 			self.setWindowTitle('Checkbox')
# 		else:
# 			self.setWindowTitle('Unchecked')
#
# #开关按钮
# class ToggleButton(QtGui.QWidget):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self, parent)
# 		self.color = QtGui.QColor(0, 0, 0) #设置初始颜色 红绿蓝
# 		self.setGeometry(300, 300, 280, 170)
# 		self.setWindowTitle('ToggleButton')
# 		self.red = QtGui.QPushButton('Red', self)
# 		self.red.setCheckable(True)
# 		self.red.move(10, 10)
# 		self.connect(self.red, QtCore.SIGNAL('clicked()'),self.setRed)
# 		self.green = QtGui.QPushButton('Green', self)
# 		self.green.setCheckable(True)       #创建个button并且可选择
# 		self.green.move(10, 60)
# 		self.connect(self.green, QtCore.SIGNAL('clicked()'),self.setGreen)
# 		self.blue = QtGui.QPushButton('Blue', self)
# 		self.blue.setCheckable(True)
# 		self.blue.move(10, 110)
# 		self.connect(self.blue, QtCore.SIGNAL('clicked()'),self.setBlue)
# 		self.square = QtGui.QWidget(self)
# 		self.square.setGeometry(150, 20, 100, 100)
# 		self.square.setStyleSheet('Qwidget {background-color: %s}' %self.color.name())
# 		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('cleanlooks'))
# 	def setRed(self):
# 		if self.red.isChecked():
# 			self.color.setRed(255)
# 		else:
# 			self.color.setRed(0)
# 		self.square.setStyleSheet('QWidget {background-color: %s}' %self.color.name())
# 	def setGreen(self):
# 		if self.green.isChecked():
# 			self.color.setGreen(255)
# 		else:
# 			self.color.setGreen(0)
# 		self.square.setStyleSheet('QWidget {background-color: %s}' %self.color.name())
# 	def setBlue(self):
# 		if self.blue.isChecked():
# 			self.color.setBlue(255)
# 		else:
# 			self.color.setBlue(0)
# 		self.square.setStyleSheet('QWidget {background-color: %s}' %self.color.name())
#
# #滑块、标签
# class SliderLabel(QtGui.QWidget):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self, parent)
# 		self.setGeometry(300, 300, 250, 150)
# 		self.setWindowTitle('SliderLabel')
# 		self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
# 		self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
# 		self.slider.setGeometry(30, 40, 100, 30)
# 		self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'),self.changeValue)
# 		self.label = QtGui.QLabel(self)
# 		self.label.setPixmap(QtGui.QPixmap('icons/mute.png')) #创建标签部件并把mute.png加入到标签中显示
# 		self.label.setGeometry(160, 40, 80, 80)
# 	def changeValue(self, value):
# 		pos = self.slider.value()
# 		if pos == 0:
# 			self.label.setPixmap(QtGui.QPixmap('icons/mute.jpg'))
# 		elif 0 < pos <= 30:
# 			self.label.setPixmap(QtGui.QPixmap('icons/mute.jpg'))
# 		elif 30 < pos < 80:
# 			self.label.setPixmap(QtGui.QPixmap('icons/mute.jpg'))
# 		else:
# 			self.label.setPixmap(QtGui.QPixmap('icons/max.jpg'))
#
# #进度条
# class ProgressBar(QtGui.QWidget):
# 	def __init__(self, parent = None):
# 		QtGui.QWidget.__init__(self)
# 		self.setGeometry(300, 300, 250, 150)
# 		self.setWindowTitle('ProgressBar')
# 		self.pbar = QtGui.QProgressBar(self)    #创建一个进度条
# 		self.pbar.setGeometry(30, 40, 200, 25)
# 		self.button = QtGui.QPushButton('Start', self)
# 		self.button.setFocusPolicy(QtCore.Qt.NoFocus)
# 		self.button.move(40, 80)
# 		self.connect(self.button, QtCore.SIGNAL('clicked()'), self.onStart)
# 		self.timer = QtCore.QBasicTimer()      #创建定时器对象
# 		self.step = 0
# 	def timerEvent(self, event):
# 		if self.step >= 100:
# 			self.timer.stop()
# 			return
# 		self.step = self.step +1
# 		self.pbar.setValue(self.step)
# 	def onStart(self):
# 		if self.timer.isActive():
# 			self.timer.stop()
# 			self.button.setText('Start')
# 		else:
# 			self.timer.start(100, self)
# 			self.button.setText('Stop')

#日历
class Calendar(QtGui.QWidget):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self)
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Calendar')
		self.cal = QtGui.QCalendarWidget(self) #创建一个日历对象
		self.cal.setGridVisible(True)
		self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'),self.showDate)
		self.label = QtGui.QLabel(self)
		date = self.cal.selectedDate()
		self.label.setText(str(date.toPyDate()))
		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(self.cal)
		vbox.addWidget(self.label)
		self.setLayout(vbox)
	def showDate(self):
		date = self.cal.selectedDate()
		self.label.setText(str(date.toPyDate()))
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	qb = Calendar()
	qb.show()
	sys.exit(app.exec_())

