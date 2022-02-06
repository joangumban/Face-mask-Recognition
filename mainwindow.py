


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.dropscreen = QtWidgets.QFrame(self.centralwidget)
        self.dropscreen.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(29, 88, 82);\n"
"    border-radius:20px;\n"
"\n"
"}")
        self.dropscreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropscreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropscreen.setObjectName("dropscreen")
        self.label = QtWidgets.QLabel(self.dropscreen)
        self.label.setGeometry(QtCore.QRect(450, 200, 431, 41))
        self.label.setStyleSheet("font: 900 36pt \"Akira Expanded\";\n"
"color: rgb(247, 237, 231);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dropscreen)
        self.label_2.setGeometry(QtCore.QRect(320, 240, 291, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/Open Peeps - Avatar (1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.dropscreen)
        self.label_3.setGeometry(QtCore.QRect(590, 240, 361, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/Open Peeps - Avatar.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.dropscreen)
        self.label_4.setGeometry(QtCore.QRect(220, 460, 981, 21))
        self.label_4.setStyleSheet("font: 900 22pt \"Akira Expanded\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.dropscreen)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 481, 31))
        self.label_5.setStyleSheet("font: 900 24pt \"Akira Expanded\";\n"
"color: rgb(245, 230, 223);")
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.dropscreen)
        self.progressBar.setGeometry(QtCore.QRect(250, 510, 811, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"    background-color: rgb(22, 20, 7);\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: rgb(75, 183, 83);\n"
"    border-radius: 10px;\n"
"     min-width: 10em;\n"
"        padding: 6px;\n"
"\n"
"}")
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.dropscreen, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.setBuddy(self.label_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Instruction"))
        self.label_4.setText(_translate("MainWindow", "please stand within 1m distance from the camera"))
        self.label_5.setText(_translate("MainWindow", "Access Control System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
