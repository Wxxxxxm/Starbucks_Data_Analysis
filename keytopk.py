# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class SDialog(QWidget):

    def __init__(self, parent = None):
        super(SDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dialog")
        self.setGeometry(300,300,450,250)
        #设定窗口标题和窗口的大小和位置。

        inputButton = QPushButton(self.tr("经度"))
        fileButton = QPushButton(self.tr("纬度"))
        colorButton = QPushButton(self.tr("数量"))
        fontButton = QPushButton(self.tr("确定"))

        self.inputL = QLineEdit()
        self.filelL = QLineEdit()


        self.colorL = QLineEdit()


        grid = QGridLayout()
        grid.addWidget(inputButton, 1, 0)
        grid.addWidget(self.inputL, 1, 1)
        grid.addWidget(fileButton, 2, 0)
        grid.addWidget(self.filelL, 2, 1)
        grid.addWidget(colorButton, 3, 0)
        grid.addWidget(self.colorL, 3, 1)
        grid.addWidget(fontButton, 4, 0)
        #grid.addWidget(self.fontL, 4, 1)
        self.setLayout(grid)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = SDialog()

    sys.exit(app.exec_())