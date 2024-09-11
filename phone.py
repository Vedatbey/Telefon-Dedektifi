from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):05310829311
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 10, 441, 561))
        self.label.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 170, 127);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.konumBtn = QtWidgets.QPushButton(self.centralwidget)
        self.konumBtn.setGeometry(QtCore.QRect(160, 420, 131, 51))
        self.konumBtn.setObjectName("konumBtn")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 140, 271, 61))
        self.lineEdit.setStyleSheet("border-radius:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.konumText = QtWidgets.QLabel(self.centralwidget)
        self.konumText.setGeometry(QtCore.QRect(60, 340, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.konumText.setFont(font)
        self.konumText.setObjectName("konumText")
        self.gsmText = QtWidgets.QLabel(self.centralwidget)
        self.gsmText.setGeometry(QtCore.QRect(280, 340, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gsmText.setFont(font)
        self.gsmText.setObjectName("gsmText")
        self.mainText = QtWidgets.QLabel(self.centralwidget)
        self.mainText.setGeometry(QtCore.QRect(110, 30, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.mainText.setFont(font)
        self.mainText.setStyleSheet("color: rgb(255, 255, 255);")
        self.mainText.setObjectName("mainText")
        self.getValue = QtWidgets.QPushButton(self.centralwidget)
        self.getValue.setGeometry(QtCore.QRect(160, 250, 131, 51))
        self.getValue.setObjectName("getValue")
        self.resInfo = QtWidgets.QPushButton(self.centralwidget)
        self.resInfo.setGeometry(QtCore.QRect(160, 500, 131, 51))
        self.resInfo.setObjectName("resInfo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.konumBtn.setText(_translate("MainWindow", "Konumu Bul"))
        self.konumText.setText(_translate("MainWindow", "Konum:Türkiye"))
        self.gsmText.setText(_translate("MainWindow", "GSM:Turkcell"))
        self.mainText.setText(_translate("MainWindow", "TELEFON DEDEKTİFİ"))
        self.getValue.setText(_translate("MainWindow", "Verileri Getir"))
        self.resInfo.setText(_translate("MainWindow", "Bilgileri Sıfırla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
