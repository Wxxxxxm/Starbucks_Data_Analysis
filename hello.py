# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import webbrowser
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import *
import xialaliebiao
import range_ui
import growng_k_time
import  jindu
import r
from PyQt5.QtGui import QIcon
import dia


class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1000)
        self.show()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setObjectName("xingbake")





        #self.setLayout(MainWindow)





    def menu(self):



        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        Menu = menubar.addMenu('时区')
        url = "https://www.baidu.com"
        action1=QAction('时区图', self)
        Menu.addAction(action1)
        action1.triggered.connect(self.load1)

        action2 = QAction('时区二级图', self)
        Menu.addAction(action2)
        action2.triggered.connect(self.load2)


        Menu = menubar.addMenu('国家')

        action3 = QAction('柱状图', self)
        Menu.addAction(action3)
        action3.triggered.connect(self.load3)

        action4 = QAction('饼图', self)
        Menu.addAction(action4)
        action4.triggered.connect(self.load4)

        Menu = menubar.addMenu('查询')
        action5=QAction('top-k', self)
        Menu.addAction(action5)
        action5.triggered.connect(self.topk)

        action8 = QAction('range', self)
        Menu.addAction(action8)
        action8.triggered.connect(self.range)

        Menu = menubar.addMenu('分布图')

        action6 = QAction('店铺分布图', self)
        Menu.addAction(action6)
        action6.triggered.connect(self.load5)

        action7 = QAction('时区店铺分布图', self)
        Menu.addAction(action7)
        action7.triggered.connect(self.load6)

        Menu = menubar.addMenu('时间分析')
        action9 = QAction('k-time', self)
        Menu.addAction(action9)
        action9.triggered.connect(self.k_time)



    # menu1.ttriggered.connect(self.load(url))
    def load1(self):
        #时区图
            url = r'file:///D:/file/starbucks/Amout_in_Each_Timezone_Pie.html'
            self.webview = QWebView()
            self.webview.load(QUrl(url))
            self.setCentralWidget(self.webview)
            self.webview.show()

    def load2(self):
        #时区二级图
            url = r'file:///D:/file/starbucks/Amount_of_Country_in_Timezone_Pie.html'
            self.webview = QWebView()
            self.webview.load(QUrl(url))
            self.setCentralWidget(self.webview)
            self.webview.show()

    def load3(self):
        #柱状图
            url = r'file:///D:/file/starbucks/Amount_Each_Country_Bar.html'
            self.webview = QWebView()
            self.webview.load(QUrl(url))
            self.setCentralWidget(self.webview)
            self.webview.show()

            # subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '1236'])
            # webbrowser.open_new_tab('http://localhost:1236/topk.html')
            #self.webview = QWebView()
            #self.webview.load(QUrl(r"D:\file\topk.html"))
            #self.setCentralWidget(self.webview)
            #self.webview.show()

    def load4(self):
        #饼状图
            url = r'file:///D:/file/starbucks/Amount_Each_Country_Pie.html'
            self.webview = QWebView()
            self.webview.load(QUrl(url))
            self.setCentralWidget(self.webview)
            self.webview.show()

    def topk(self):
         self.ui = xialaliebiao.input_window()
         #self.ex = jindu.Example()
         self.ui.show()

    def range(self):
        self.ui=range_ui.input_window()
        self.ui.show()


    def load5(self):
        # 店铺分布图
            subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '1236'])
            webbrowser.open_new_tab('http://localhost:1236/fenbutu.html')

    def load6(self):
        # 店铺时区分布图
            subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '1236'])
            webbrowser.open_new_tab('http://localhost:1236/map_time.html')

    def k_time(self):
        #时区二级图
            self.ui = growng_k_time.input_window()
            self.ui.show()
            print(growng_k_time.a)

            """  url = r'file:///D:/file/starbucks/TOPK_Analysis_with_growing_k.html'
              self.webview = QWebView()
              self.webview.load(QUrl(url))
              self.setCentralWidget(self.webview)
              self.webview.show()"""





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))






# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!








import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    #widget = QtWidgets.QWidget()
    #MainWindow = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow = Ui_MainWindow()
    # url = "https://www.baidu.com"
    # MainWindow.load1()

    MainWindow.show()
    MainWindow.menu()
   # QWebView.load(MainWindow,url)



    sys.exit(app.exec_())