# -*- coding: utf-8 -*-

import webbrowser
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import DataAnalysis
import miniheap2
#import topk
import sys
import time
import pandas

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

        # 创建两个QlineEdit实例，来显示选择的内容
        #self.colorFrame = QLineEdit()
        #self.colorFrame.setFrameShape(QFrame.Box)
        #self.colorFrame.setAutoFillBackground(True)
        # 创建一个Frame实例用来显示颜色
        self.colorL = QLineEdit()
        #self.fontL = QLineEdit()

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
        #网格类布局

        inputButton.clicked.connect(self.openInput)
        fileButton.clicked.connect(self.openFile)
        colorButton.clicked.connect(self.openColor)
        fontButton.clicked.connect(self.input)
        #把四个按钮控件的clicked（）信号和槽连接

    def openInput(self):
        t, ok = QInputDialog.getText(self, "用户输入对话框",  "请输入任意内容" )
        if ok:
            self.inputL.setText(t)

    def openFile(self):
        s = QFileDialog.getOpenFileName(self, "open file dialog", "d:/", "python file(*py)")
        self.filelL.setText(s[0])

    def openColor(self):
        c = QColorDialog.getColor(Qt.blue)
        if c.isValid():
            self.colorFrame.setPalette(QPalette(c))

    def openFont(self):
        #f, ok=self.input()
        #f, ok = QFontDialog.getFont()
        t, ok = QInputDialog.getText(self, "好的", "请输入任意内容")
        if ok:
            self.inputL.setText(t)


    def input(self):
        lon = float(self.inputL.text())
        lat=float(self.filelL.text())
        k=int(self.colorL.text())
        starbucks_df = DataAnalysis.read_data()
        # df_topk = miniheap2.top_k(starbucks_df, lon, lat, k)
        # DataAnalysis.create_geojson(df_topk, 'topk.geojson')
        # starbucks_category_color_stops = [['Starbucks', 'rgb(211,47,47)'], ]
        # DataAnalysis.draw_map('topk.geojson', starbucks_category_color_stops, 'Brand', r'D:\\file\starbucks\topk.html')
       # df_k = topk.calculate(starbucks_df, lon, lat, k)
        starbucks_category_color_stops = [['Starbucks', 'rgb(211,47,47)'], ]
        dfk_json_file = "df_k.geojson"
        DataAnalysis.create_geojson(df_k, dfk_json_file)
        DataAnalysis.draw_map(dfk_json_file, starbucks_category_color_stops, 'Brand', r'D:\\file\starbucks\dfk.html')
        subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '1236'])
        webbrowser.open_new_tab('http://localhost:1236/dfk.html')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = SDialog()

    sys.exit(app.exec_())
