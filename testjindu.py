# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import range
from simtopk import *
from DataAnalysis import*
import sys

#QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class Progess(QWidget):
    def __init__(self, parent=None):
        super(Progess, self).__init__(parent)
        self.setWindowTitle(self.tr("使用进度条"))
        numLabel = QLabel(self.tr("文件数目"))
        self.numLineEdit = QLineEdit("10")
        typeLabel = QLabel(self.tr("显示类型"))
        self.typeComboBox = QComboBox()
        self.typeComboBox.addItem(self.tr("进度条"))
        self.typeComboBox.addItem(self.tr("进度对话框"))

        self.progressBar = QProgressBar()

        self.btn = QPushButton('开始', self)

        layout = QGridLayout()
        layout.addWidget(numLabel, 0, 0)
        layout.addWidget(self.numLineEdit, 0, 1)
        layout.addWidget(typeLabel, 1, 0)
        layout.addWidget(self.typeComboBox, 1, 1)
        layout.addWidget(self.progressBar, 2, 0, 1, 2)
        layout.addWidget(self.btn, 3, 1)
        #layout.setMargin(15)
        #layout.setSpacing(10)

        self.setLayout(layout)

        #self.connect(startPushButton, SIGNAL("clicked()"), self.slotStart)
        self.btn.clicked.connect(self.slotStart)

    def slotStart(self):
        num = int(self.numLineEdit.text())

        if self.typeComboBox.currentIndex() == 0:
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(num)

            starbucks_df = read_data()
            df_find = find_same(starbucks_df, 'City', '广州')
            df_find = preprocessing(df_find)
            df_temp = topk(df_find, 113.3, 23.40, 5)


            for i in range(num):
                self.progressBar.setValue(i)


        elif self.typeComboBox.currentIndex() == 1:
            progressDialog = QProgressDialog(self)
            progressDialog.setWindowModality(Qt.WindowModal)
            progressDialog.setMinimumDuration(5)
            progressDialog.setWindowTitle(self.tr("请等待"))
            progressDialog.setLabelText(self.tr("拷贝..."))
            progressDialog.setCancelButtonText(self.tr("取消"))
            progressDialog.setRange(0, num)

            for i in range(num):
                progressDialog.setValue(i)

                if progressDialog.wasCanceled():
                    return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    progess = Progess()
    progess.show()
    app.exec_()