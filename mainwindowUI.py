# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebKitWidgets import QWebView
from DataAnalysis import *
from similarity import *
from r import *
from score import *
from k import *
import time
from urllib import *
from pandas import DataFrame

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        vbox = QGridLayout()

        self.topk = QtWidgets.QWidget(self.centralwidget)
        self.topk.setGeometry(QtCore.QRect(0, 0, 721, 41))
        self.topk.setObjectName("topk")

        self.key = QtWidgets.QComboBox(self.topk)
        self.key.setGeometry(QtCore.QRect(90, 10, 81, 22))
        self.key.setObjectName("key")

        self.key.addItem("")
        self.key.addItem("Brand")
        self.key.addItem("Store Number")
        self.key.addItem("Store Name")
        self.key.addItem("Ownership Type")
        self.key.addItem("Street Address")
        self.key.addItem("City")
        self.key.addItem("State/Province")
        self.key.addItem("Country")
        self.key.addItem("Postcode")
        self.key.addItem("Phone Number")
        self.key.addItem("Timezone")

        self.keyword_text = ""
        self.key.activated[str].connect(self.keyword_onActivated)

        self.keyword = QtWidgets.QLineEdit(self.topk)
        self.keyword.setGeometry(QtCore.QRect(180, 10, 71, 20))
        self.keyword.setObjectName("keyword")

        self.label_3 = QtWidgets.QLabel(self.topk)
        self.label_3.setGeometry(QtCore.QRect(430, 10, 71, 20))
        self.label_3.setObjectName("label_3")

        self.input_k = QtWidgets.QLineEdit(self.topk)
        self.input_k.setGeometry(QtCore.QRect(500, 10, 31, 20))
        self.input_k.setObjectName("input_k")

        self.label = QtWidgets.QLabel(self.topk)
        self.label.setGeometry(QtCore.QRect(260, 10, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.topk)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 31, 16))
        self.label_2.setObjectName("label_2")

        self.search_k = QtWidgets.QPushButton(self.topk)
        self.search_k.setGeometry(QtCore.QRect(540, 10, 75, 23))
        self.search_k.setObjectName("search_k")

        self.input_lat = QtWidgets.QLineEdit(self.topk)
        self.input_lat.setGeometry(QtCore.QRect(380, 10, 41, 20))
        self.input_lat.setObjectName("input_lat")

        self.input_lon = QtWidgets.QLineEdit(self.topk)
        self.input_lon.setGeometry(QtCore.QRect(290, 10, 51, 20))
        self.input_lon.setObjectName("input_lon")

        self.label_9 = QtWidgets.QLabel(self.topk)
        self.label_9.setGeometry(QtCore.QRect(13, 12, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setObjectName("label_9")

        self.time_analysis = QtWidgets.QPushButton(self.topk)
        self.time_analysis.setGeometry(QtCore.QRect(630, 10, 81, 21))
        self.time_analysis.setObjectName("time_analysis")

        self.topr = QtWidgets.QWidget(self.centralwidget)
        self.topr.setGeometry(QtCore.QRect(0, 40, 971, 41))
        self.topr.setObjectName("topr")

        self.webwindow = QWebView(self.centralwidget)
        self.webwindow.setGeometry(QtCore.QRect(-1, 79, 1200, 800))
        self.webwindow.setAutoFillBackground(True)
        self.webwindow.setObjectName("webwindow")

        self.label_11 = QtWidgets.QLabel(self.topr)
        self.label_11.setGeometry(QtCore.QRect(100, 10, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.topr)
        self.label_12.setGeometry(QtCore.QRect(210, 10, 31, 16))
        self.label_12.setObjectName("label_12")

        self.search_r = QtWidgets.QPushButton(self.topr)
        self.search_r.setGeometry(QtCore.QRect(530, 10, 75, 23))
        self.search_r.setObjectName("search_r")

        self.input_lat_r = QtWidgets.QLineEdit(self.topr)
        self.input_lat_r.setGeometry(QtCore.QRect(240, 10, 71, 20))
        self.input_lat_r.setObjectName("input_lat_r")

        self.input_lon_r = QtWidgets.QLineEdit(self.topr)
        self.input_lon_r.setGeometry(QtCore.QRect(130, 10, 71, 20))
        self.input_lon_r.setObjectName("input_lon_r")

        self.label_13 = QtWidgets.QLabel(self.topr)
        self.label_13.setGeometry(QtCore.QRect(320, 10, 101, 20))
        self.label_13.setObjectName("label_13")

        self.input_r = QtWidgets.QLineEdit(self.topr)
        self.input_r.setGeometry(QtCore.QRect(430, 10, 81, 20))
        self.input_r.setObjectName("input_r")

        self.label_14 = QtWidgets.QLabel(self.topr)
        self.label_14.setGeometry(QtCore.QRect(13, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(self.topr)
        self.label_15.setGeometry(QtCore.QRect(630, 10, 84, 20))
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)

        self.input_score = QtWidgets.QLineEdit(self.topr)
        self.input_score.setGeometry(QtCore.QRect(720, 10, 91, 20))
        self.input_score.setObjectName("input_score")
        self.input_score.setEnabled(False)

        self.in_score = QtWidgets.QPushButton(self.topr)
        self.in_score.setGeometry(QtCore.QRect(820, 10, 75, 20))
        self.in_score.setObjectName("in_score")
        self.in_score.setEnabled(False)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)


        # self.setGeometry(300, 300, 250, 150)

        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        # self.msgLabel = QtWidgets.QLabel()
        # self.msgLabel.setMinimumSize(self.msgLabel.sizeHint())

        # self.statusbar.addWidget(self.msgLabel)

        self.shiqu = QtWidgets.QAction(MainWindow)
        self.shiqu.setObjectName("shiqu")

        self.shiquerji = QtWidgets.QAction(MainWindow)
        self.shiquerji.setObjectName("shiquerji")

        self.shiqujianbian = QtWidgets.QAction(MainWindow)
        self.shiqujianbian.setObjectName("shiqujianbian")


        self.zhuzhuang = QtWidgets.QAction(MainWindow)
        self.zhuzhuang.setObjectName("zhuzhuang")

        self.bingtu = QtWidgets.QAction(MainWindow)
        self.bingtu.setObjectName("bingtu")

        self.guojiajianbian = QtWidgets.QAction(MainWindow)
        self.guojiajianbian.setObjectName("guojiajianbian")

        self.fenbu = QtWidgets.QAction(MainWindow)
        self.fenbu.setObjectName("fenbu")

        self.shiqufenbu = QtWidgets.QAction(MainWindow)
        self.shiqufenbu.setObjectName("shiqufenbu")

        self.menu.addAction(self.shiqu)
        self.menu.addAction(self.shiquerji)
        self.menu.addAction(self.shiqujianbian)
        self.menu_2.addAction(self.zhuzhuang)
        self.menu_2.addAction(self.bingtu)
        self.menu_2.addAction(self.guojiajianbian)
        self.menu_3.addAction(self.fenbu)
        self.menu_3.addAction(self.shiqufenbu)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(1200, 80, 301, 501))
        self.listWidget.setObjectName("listView")
        self.listWidget.close()

        self.retranslateUi(MainWindow)
        self.search_k.clicked.connect(self.search_kfun)
        self.shiqu.triggered.connect(self.shiqufun)
        self.shiquerji.triggered.connect(self.shiquerjifun)
        self.shiqujianbian.triggered.connect(self.shiqujianbianfun)
        self.zhuzhuang.triggered.connect(self.zhuzhuangfun)
        self.bingtu.triggered.connect(self.bingtufun)
        self.guojiajianbian.triggered.connect(self.guojiajianbianfun)
        self.fenbu.triggered.connect(self.fenbufun)
        self.shiqufenbu.triggered.connect(self.shiqufenbufun)
        self.time_analysis.clicked.connect(self.time_analysisfun)
        self.search_r.clicked.connect(self.search_rfun)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        vbox.addWidget(self.topk)
        vbox.addWidget(self.topr)
        vbox.addWidget(self.webwindow)

        self.setLayout(vbox)

    def search_kfun(self):
        # input_attr = self.keyword.text().encode("utf-8")
        input_attr = self.keyword.text().decode(encoding="utf-8")
        input_lon = float(self.input_lon.text())
        input_lat = float(self.input_lat.text())
        input_k = int(self.input_k.text())

        starbucks_df = read_data()
        print(starbucks_df)

        start = time.time()
        df_find = find_same(starbucks_df, self.keyword_text, input_attr)
        df_find = preprocessing(df_find)

        df_temp = topk(df_find, input_lon, input_lat, input_k)
        end = time.time()
        run_time = end-start
        self.statusBar().showMessage('查询时间为： '+str(run_time))
        print(df_temp)

        draw_map(df_temp, 'simtopk.html')

        k_analysis = topk_k_analysis(df_find, input_lon, input_lat)
        bar_time = Bar("该经纬度下topk计算时间随k变化")
        bar_pic(bar_time, k_analysis, 'k', 'time', 'k时间顺序')
        bar_time.render(r'time_analysis.html')

        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/simtopk.html'

        self.webwindow.load(QtCore.QUrl(url))
        self.webwindow.show()
        self.listWidget.clear()

        for i in range(df_temp.shape[0]):
             item = QListWidgetItem(df_temp['Store Name'][i])
             self.listWidget.addItem(item)
        self.listWidget.show()
        # self.listWidget.update()

        self.listWidget.itemClicked['QListWidgetItem*'].connect(self.dia)

        # self.msgLabel.setText("run time is: "+ run_time)

    def dia(self):
        self.input_score.setEnabled(True)
        self.in_score.setEnabled(True)
        self.in_score.clicked.connect(self.pingfen)

    def pingfen(self):
        score_var = int(self.input_score.text())

        starbucks_df = read_data()
        print(score_var)
        print(type(self.listWidget.currentItem().text()))
        print(type(self.listWidget.currentItem().text().encode("utf-8")))
        starbucks_df = input_score(starbucks_df,score_var,self.listWidget.currentItem().text().encode("utf-8"))
        starbucks_df.to_csv('temp.csv',encoding="utf_8_sig", index=False)


    def keyword_onActivated(self, text):
        self.keyword_text = text.encode("utf-8")

    def search_rfun(self):
        input_lon_r = float(self.input_lon_r.text())
        input_lat_r = float(self.input_lat_r.text())
        input_r = int(self.input_r.text())

        starbucks_df = read_data()

        df_find = preprocessing(starbucks_df)
        df_temp = r_cal(df_find, input_lon_r, input_lat_r, input_r)

        draw_map(df_temp, 'range.html')
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/range.html'
        self.webwindow.load(QtCore.QUrl(url))
        self.webwindow.show()
        self.listWidget.clear()

        for i in range(df_temp.shape[0]):
            item = QListWidgetItem(df_temp['Store Name'][i])
            self.listWidget.addItem(item)
        self.listWidget.show()

        self.listWidget.itemClicked['QListWidgetItem*'].connect(self.dia)

    def time_analysisfun(self):
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/time_analysis.html'
        self.webwindow.load(QtCore.QUrl(url))
        self.webwindow.show()
        self.listWidget.close()

        # self.statusBar().showMessage('状态栏上显示的消息')


    def shiqufun(self):
        # 时区图
        starbucks_df = read_data()

        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/Amout_in_Each_Timezone_Pie.html'
        self.webwindow.load(QtCore.QUrl(url))
        # self.setCentralWidget(self.webwindow)
        self.webwindow.show()
        self.listWidget.close()

    def shiquerjifun(self):
        # 时区二级图
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/Amount_of_Country_in_Timezone_Pie.html'
        self.webwindow.load(QtCore.QUrl(url))
        # self.setCentralWidget(self.webwindow)
        self.webwindow.show()
        self.listWidget.close()

    def shiqujianbianfun(self):
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:'+url+'/map_time.html'
        self.webwindow.load(QtCore.QUrl(url))
        # self.setCentralWidget(self.webwindow)
        self.webwindow.show()
        self.listWidget.close()

    def zhuzhuangfun(self):
        # 柱状图
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/Amount_Each_Country_Bar.html'
        self.webwindow.load(QtCore.QUrl(url))
        self.webwindow.show()
        self.listWidget.close()

    def bingtufun(self):
        # 饼状图
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/Amount_Each_Country_Pie.html'
        self.webwindow.load(QtCore.QUrl(url))
        self.webwindow.show()
        self.listWidget.close()

    def guojiajianbianfun(self):
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/distribution_map_country.html'
        self.webwindow.load(QtCore.QUrl(url))
        # self.setCentralWidget(self.webwindow)
        self.webwindow.show()
        self.listWidget.close()


    def fenbufun(self):
        # 店铺分布图
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/fenbutu.html'
        self.webwindow.load(QtCore.QUrl(url))
        self.webwindow.show()
        self.listWidget.close()


    def shiqufenbufun(self):
        # 店铺时区分布图
        path = os.getcwd()
        url = pathname2url(path)
        url = 'file:' + url + '/map_time.html'
        self.webwindow.load(QtCore.QUrl(url))
        self.webwindow.show()
        self.listWidget.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "显示结果数："))
        self.label.setText(_translate("MainWindow", "经度："))
        self.label_2.setText(_translate("MainWindow", "纬度："))
        self.search_k.setText(_translate("MainWindow", "查询"))
        self.label_9.setText(_translate("MainWindow", "关键词检索"))
        self.time_analysis.setText(_translate("MainWindow", "查询时间分析"))
        self.label_11.setText(_translate("MainWindow", "经度："))
        self.label_12.setText(_translate("MainWindow", "纬度："))
        self.search_r.setText(_translate("MainWindow", "查询"))
        self.label_13.setText(_translate("MainWindow", "查询距离范围(米)："))
        self.label_14.setText(_translate("MainWindow", "距离范围检索"))
        self.label_15.setText(_translate("MainWindow", "输入分数(1-10):"))
        self.in_score.setText(_translate("MainWindow", "评分"))
        self.menu.setTitle(_translate("MainWindow", "按时区数据统计"))
        self.menu_2.setTitle(_translate("MainWindow", "按国家数据统计"))
        self.menu_3.setTitle(_translate("MainWindow", "分布地图"))
        self.shiqu.setText(_translate("MainWindow", "各时区店铺数量统计饼图"))
        self.shiquerji.setText(_translate("MainWindow", "各时区店铺数量统计饼图（详细）"))
        self.shiqujianbian.setText(_translate("MainWindow", "各时区店铺数量渐变图"))
        self.zhuzhuang.setText(_translate("MainWindow", "柱状图"))
        self.bingtu.setText(_translate("MainWindow", "饼图"))
        self.guojiajianbian.setText(_translate("MainWindow", "各国家店铺数量渐变图"))
        self.fenbu.setText(_translate("MainWindow", "店铺分布图"))
        self.shiqufenbu.setText(_translate("MainWindow", "时区店铺分布图"))

"""
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    #widget = QtWidgets.QWidget()
    #MainWindow = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow = Ui_MainWindow()
    MainWindow.setupUi(MainWindow)
    # url = "https://www.baidu.com"
    # MainWindow.load1()

    MainWindow.show()
   # QWebView.load(MainWindow,url)



    sys.exit(app.exec_())"""