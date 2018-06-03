#-*- coding:utf-8 -*-

import sys
#from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QComboBox，QLineEdit)
from PyQt5.QtWidgets import *
from simtopk import *
from DataAnalysis import*
import jindu

from PyQt5.QtCore import *
from PyQt5.QtGui import *
#import similarity



class input_window(QWidget):

     def __init__(self):
           super(input_window,self).__init__()

           self.initUI()

     def initUI(self):

        self.lbl = QLabel("Staubucks",self)

        combo = QComboBox(self)
        combo.addItem("")
        combo.addItem("Brand")
        combo.addItem("Store Number")
        combo.addItem("Store Name")
        combo.addItem("Ownership Type")
        combo.addItem("Street Address")
        combo.addItem("City")
        combo.addItem("State/Province")
        combo.addItem("Country")
        combo.addItem("Postcode")
        combo.addItem("Phone Number")
        combo.addItem("Timezone")

        self.lbl1 = QLabel("经度", self)
        self.lbl2 = QLabel("纬度",self)
        self.lbl3 = QLabel("K", self)

        self.attr_edit = QLineEdit()
        self.lon = QLineEdit()
        self.lab = QLineEdit()
        self.k = QLineEdit()
        self.lbl1.move(50, 20)
        Button = QPushButton(self.tr("确定"))

        grid = QGridLayout()
        grid.addWidget(combo, 1, 0)
        grid.addWidget(self.attr_edit, 1, 1)
        grid.addWidget(self.lbl1, 2, 0)
        grid.addWidget(self.lon, 2, 1)
        grid.addWidget(self.lbl2, 3, 0)
        grid.addWidget(self.lab, 3, 1)
        grid.addWidget(self.lbl3, 4, 0)
        grid.addWidget(self.k, 4, 1)
        grid.addWidget(Button, 5, 0)

        self.setLayout(grid)


        #combo.move(20,20)
        self.lbl.move(50,150)

        self.Text_combo=""
        combo.activated[str].connect(self.keyword_onActivated)
        Button.clicked.connect(self.ok)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QComboBox')
        self.show()


#############################响应函数
     def ok(self):
        input_attr = self.attr_edit.text().encode("utf-8")
        print self.Text_combo
        input_lon = float(self.lon.text())
        input_lat = float(self.lab.text())
        input_k = int(self.k.text())

        starbucks_df = read_data()

        df_find = find_same(starbucks_df, self.Text_combo, input_attr)

        df_find = preprocessing(df_find)
        print("repro")
        df_temp = topk(df_find, input_lon, input_lat, input_k)
        print  df_temp
        simtopk_json="simtopk.json"
        create_geojson(df_temp, simtopk_json)
        starbucks_category_color_stops = [['Starbucks', 'rgb(211,47,47)'], ]
        print "11111"
        draw_map(simtopk_json, starbucks_category_color_stops, 'Brand', r'D:\\file\starbucks\simtopk.html')

        subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '12306'])
        webbrowser.open_new_tab('http://localhost:12306/simtopk.html')
        #webbrowser.open_new_tab('D://file/starbucks/simtopk.html')

     def keyword_onActivated(self, text):
        self.lbl.setText(text)
        self.Text_combo=text.encode("utf-8")

           #self.lbl.adjustSize()"""


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = input_window()

    sys.exit(app.exec_())