#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 教程

这个例子显示了一个进度条控件。

作者：我的世界你曾经来过
博客：http://blog.csdn.net/weiaitaowang
最后编辑：2016年8月3日
"""

import sys
#import r
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import *


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('开始', self)
        self.btn.move(40, 80)

        #self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('进度条')
       # self.pbar.setValue(5)
        #QThread.msleep(100)
        #self.pbar.setValue(20)
        self.show()

    def timerEvent(self, e):
        #df=r.r_cal()
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('完成')
            return
        self.step = self.step+10
        self.pbar.setValue(self.step)
        QThread.msleep(15)



    def doAction(self, value):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')

        else:
            #print value
            self.timer.start(100, self)
            self.btn.setText('停止')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())