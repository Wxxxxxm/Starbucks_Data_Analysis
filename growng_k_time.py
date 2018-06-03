#-*- coding:utf-8 -*-

import sys
#from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QComboBox，QLineEdit)
from PyQt5.QtWidgets import *
from simtopk import *
from DataAnalysis import*
import r
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#import similarity


a=0
class input_window(QWidget):

     def __init__(self):
           super(input_window,self).__init__()

           self.initUI()

     def initUI(self):



        self.lbl1 = QLabel("经度", self)
        self.lbl2 = QLabel("纬度",self)



        self.lon = QLineEdit()
        self.lab = QLineEdit()

        self.lbl1.move(50, 20)
        Button = QPushButton(self.tr("确定"))

        grid = QGridLayout()

        grid.addWidget(self.lbl1, 2, 0)
        grid.addWidget(self.lon, 2, 1)
        grid.addWidget(self.lbl2, 3, 0)
        grid.addWidget(self.lab, 3, 1)

        grid.addWidget(Button, 5, 0)

        self.setLayout(grid)


        #combo.move(20,20)

        self.Text_combo=""
        Button.clicked.connect(self.ok)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('k_analysis')
        self.show()


#############################响应函数
     def ok(self):

        input_lon = float(self.lon.text())
        input_lat = float(self.lab.text())
        starbucks_df = read_data()
        df_topkk=preprocessing(starbucks_df)
        """df_topkk = topk_k_analysis(starbucks_df, input_lon, input_lat)
        bar2 = Bar("topk time with different k ")
        bar2 = bar_pic(bar2, df_topkk, 'k', 'time', 'Time Analysis Bar')
        bar2.render('TOPK_Analysis_with_growing_k.html')
        subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '12306'])"""
        webbrowser.open_new_tab('http://localhost:12306/TOPK_Analysis_with_growing_k.html')



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = input_window()

    sys.exit(app.exec_())