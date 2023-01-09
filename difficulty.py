# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'difficulty.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 310)
        MainWindow.setMinimumSize(QtCore.QSize(310, 310))
        MainWindow.setMaximumSize(QtCore.QSize(310, 310))
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"     background-image: url(:/background/dif_back.png)\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_easy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_easy.setGeometry(QtCore.QRect(20, 80, 71, 71))
        self.pushButton_easy.setStyleSheet("QPushButton {\n"
"    background-image: url(:/background/dif_1.png);\n"
"    background-color: rgb(224, 205, 200);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(224, 205, 200);\n"
"    background-image: url(:/background/dif_1_sec.png);\n"
" }")
        self.pushButton_easy.setText("")
        self.pushButton_easy.setObjectName("pushButton_easy")
        self.pushButton_normal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_normal.setGeometry(QtCore.QRect(120, 80, 71, 71))
        self.pushButton_normal.setStyleSheet("QPushButton {\n"
"    background-color: rgb(224, 205, 200);\n"
"    background-image: url(:/background/dif_2.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(224, 205, 200);\n"
"    background-image: url(:/background/dif_2_sec.png)\n"
" }")
        self.pushButton_normal.setText("")
        self.pushButton_normal.setObjectName("pushButton_normal")
        self.pushButton_hard = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hard.setGeometry(QtCore.QRect(220, 80, 71, 71))
        self.pushButton_hard.setStyleSheet("QPushButton {\n"
"    background-color: rgb(224, 205, 200);\n"
"    background-image: url(:/background/dif_3.png)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(224, 205, 200);\n"
"    background-image: url(:/background/dif_3_sec.png);\n"
" }")
        self.pushButton_hard.setText("")
        self.pushButton_hard.setObjectName("pushButton_hard")
        self.pushButton_jopa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_jopa.setGeometry(QtCore.QRect(70, 170, 170, 60))
        self.pushButton_jopa.setMinimumSize(QtCore.QSize(170, 60))
        self.pushButton_jopa.setStyleSheet("QPushButton {\n"
"    background-image: url(:/background/dif_4.png) stretch;\n"
"    background-color: rgb(224, 205, 200);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(224, 205, 200);\n"
"    background-image: url(:/background/dif_4_sec.png);\n"
" }")
        self.pushButton_jopa.setText("")
        self.pushButton_jopa.setObjectName("pushButton_jopa")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 260, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(66, 46, 41)")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сложность"))
import back_reg


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
