

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui2(object):
    def setupUi(self, ui2):
        ui2.setObjectName("ui2")
        ui2.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(ui2)
        self.centralwidget.setObjectName("centralwidget")
        self.dropscreen = QtWidgets.QFrame(self.centralwidget)
        self.dropscreen.setGeometry(QtCore.QRect(10, 10, 1280, 720))
        self.dropscreen.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(29, 88, 82);\n"
"    border-radius:20px;\n"
"\n"
"}")
        self.dropscreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropscreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropscreen.setObjectName("dropscreen")
        self.label_6 = QtWidgets.QLabel(self.dropscreen)
        self.label_6.setGeometry(QtCore.QRect(340, 110, 541, 41))
        self.label_6.setStyleSheet("font: 900 20pt \"Akira Expanded\";\n"
"color: rgb(247, 237, 231);")
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.dropscreen)
        self.label_10.setGeometry(QtCore.QRect(40, 40, 481, 31))
        self.label_10.setStyleSheet("font: 900 24pt \"Akira Expanded\";\n"
"color: rgb(245, 230, 223);")
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.frame = QtWidgets.QFrame(self.dropscreen)
        self.frame.setGeometry(QtCore.QRect(70, 150, 1131, 521))
        self.frame.setStyleSheet("QFrame{\n"
"    \n"
"\n"
"    background-color: rgb(24, 42, 16);\n"
"    border-radius:20px;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        ui2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ui2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        ui2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ui2)
        self.statusbar.setObjectName("statusbar")
        ui2.setStatusBar(self.statusbar)

        self.retranslateUi(ui2)
        QtCore.QMetaObject.connectSlotsByName(ui2)

    def retranslateUi(self, ui2):
        _translate = QtCore.QCoreApplication.translate
        ui2.setWindowTitle(_translate("ui2", "MainWindow"))
        self.label_6.setText(_translate("ui2", "starting camera please stand by"))
        self.label_10.setText(_translate("ui2", "Access Control System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui2 = QtWidgets.QMainWindow()
    ui = Ui_ui2()
    ui.setupUi(ui2)
    ui2.show()
    sys.exit(app.exec_())
