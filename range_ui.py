#-*- coding:utf-8 -*-

import sys
#from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QComboBox，QLineEdit)
from PyQt5.QtWidgets import *
from simtopk import *
from DataAnalysis import*
import r
import jdt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#import similarity



class input_window(QWidget):

     def __init__(self):
           super(input_window,self).__init__()

           self.initUI()

     def initUI(self):



        self.lbl1 = QLabel("经度", self)
        self.lbl2 = QLabel("纬度",self)
        self.lbl3 = QLabel("半径", self)

        self.attr_edit = QLineEdit()
        self.lon = QLineEdit()
        self.lab = QLineEdit()
        self.k = QLineEdit()
        self.lbl1.move(50, 20)
        Button = QPushButton(self.tr("确定"))

        grid = QGridLayout()


        grid.addWidget(self.lbl1, 2, 0)
        grid.addWidget(self.lon, 2, 1)
        grid.addWidget(self.lbl2, 3, 0)
        grid.addWidget(self.lab, 3, 1)
        grid.addWidget(self.lbl3, 4, 0)
        grid.addWidget(self.k, 4, 1)
        grid.addWidget(Button, 5, 0)

        self.setLayout(grid)


        #combo.move(20,20)

        self.Text_combo=""
        Button.clicked.connect(self.ok)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QComboBox')
        self.show()


#############################响应函数
     def ok(self):
        input_attr = self.attr_edit.text().encode("utf-8")

        input_lon = float(self.lon.text())
        input_lat = float(self.lab.text())
        input_k = int(self.k.text())
        self.ex_1 = jdt.Example()
        self.ex_1.show()
        starbucks_df = read_data()
        df_find = preprocessing(starbucks_df)
        df_temp = r.r_cal(df_find, input_lon, input_lat, input_k)

        range_json="range.json"
        create_geojson(df_temp, range_json)
        starbucks_category_color_stops = [['Starbucks', 'rgb(211,47,47)'], ]
        draw_map(range_json, starbucks_category_color_stops, 'Brand', r'D:\\file\starbucks\range.html')

"""        subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '12306'])
        webbrowser.open_new_tab('http://localhost:12306/range.html')"""


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = input_window()

    sys.exit(app.exec_())