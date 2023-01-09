# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 620)
        MainWindow.setMinimumSize(QtCore.QSize(620, 620))
        MainWindow.setMaximumSize(QtCore.QSize(620, 620))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"     background-image: url(:/background/back_reg.png)\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 370, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(192, 165, 157);\n"
"    background-image: url(:/background/sing_in.png);\n"
" }\n"
"QPushButton:hover {\n"
"     background-color:rgb(255, 237, 221);\n"
" }")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(150, 210, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("background-color:rgb(255, 239, 234);")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setMaxLength(64)
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name.setPlaceholderText("Нажмите для ввода")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(150, 290, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_pass.setFont(font)
        self.lineEdit_pass.setStyleSheet("background-color:rgb(255, 239, 234);")
        self.lineEdit_pass.setText("")
        self.lineEdit_pass.setMaxLength(16)
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(160, 330, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setText("Показать пароль")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_reg = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reg.setGeometry(QtCore.QRect(230, 470, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.pushButton_reg.setFont(font)
        self.pushButton_reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_reg.setStyleSheet("QPushButton {\n"
"    background-color: rgb(192, 165, 157);\n"
"    \n"
"    background-image: url(:/background/sing_up.png);\n"
" }\n"
"QPushButton:hover {\n"
"     background-color:rgb(255, 237, 221);\n"
" }")
        self.pushButton_reg.setText("")
        self.pushButton_reg.setObjectName("pushButton_reg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.lineEdit_pass.setPlaceholderText(_translate("MainWindow", "Нажмите для ввода"))
import back_reg


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
