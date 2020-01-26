# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from model import *
from PIL import Image
import PyQt5


class Ui_MainWindow(object):
    path_Cfg = "/home/mertdgn/Desktop/Hunt-UI/Senior.cfg"
    path_Weights = "/home/mertdgn/Desktop/Hunt-UI/Senior_6.weights"
    path_Meta = "/home/mertdgn/Desktop/Hunt-UI/Senior.data"
    network = darknet(path_Cfg, path_Weights, path_Meta)
    categories = ['category ' + str(i+1) for i in range(7)]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(350, 350))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("upload.png").scaled(
            350, 350, PyQt5.QtCore.Qt.KeepAspectRatio))
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.get_image)
        self.verticalLayout_5.addWidget(self.pushButton)
        self.horizontalLayout_17.addLayout(self.verticalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(
            10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(150, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(150, 30))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_3.addWidget(self.progressBar_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(150, 30))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_4.addWidget(self.textBrowser_3)
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_4.addWidget(self.progressBar_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser_4.sizePolicy().hasHeightForWidth())
        self.textBrowser_4.setSizePolicy(sizePolicy)
        self.textBrowser_4.setMaximumSize(QtCore.QSize(150, 30))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_5.addWidget(self.textBrowser_4)
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.horizontalLayout_5.addWidget(self.progressBar_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser_5.sizePolicy().hasHeightForWidth())
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(150, 30))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_6.addWidget(self.textBrowser_5)
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.horizontalLayout_6.addWidget(self.progressBar_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem13 = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser_6.sizePolicy().hasHeightForWidth())
        self.textBrowser_6.setSizePolicy(sizePolicy)
        self.textBrowser_6.setMaximumSize(QtCore.QSize(150, 30))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout_7.addWidget(self.textBrowser_6)
        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setObjectName("progressBar_6")
        self.horizontalLayout_7.addWidget(self.progressBar_6)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem14 = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem14)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser_7.sizePolicy().hasHeightForWidth())
        self.textBrowser_7.setSizePolicy(sizePolicy)
        self.textBrowser_7.setMaximumSize(QtCore.QSize(150, 30))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.horizontalLayout_8.addWidget(self.textBrowser_7)
        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setProperty("value", 0)
        self.progressBar_7.setObjectName("progressBar_7")
        self.horizontalLayout_8.addWidget(self.progressBar_7)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem15 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            "x.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem17 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_17.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hunt-AI"))
        self.pushButton.setText(_translate("MainWindow", "Upload"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.categories[0] + "</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.categories[1] + "</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.categories[2] + "</p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.categories[3] + "</p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.categories[4] + "</p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.categories[5] + "</p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.categories[6] + "</p></body></html>"))

    def get_image(self):
        name = QtWidgets.QFileDialog.getOpenFileName(
            caption='Open File', filter="Image Files(*.png *.jpg *.jpeg)")
        if name[0] is not None and name[0] != "":
            self.label.setPixmap(QtGui.QPixmap(name[0]).scaled(
                350, 350))
            predicts = self.network.predict(name[0])
            self.progressBar.setProperty("value", predicts[0][1]*100)
            self.progressBar_2.setProperty("value", predicts[1][1]*100)
            self.progressBar_3.setProperty("value", predicts[2][1]*100)
            self.progressBar_4.setProperty("value", predicts[3][1]*100)
            self.progressBar_5.setProperty("value", predicts[4][1]*100)
            self.progressBar_6.setProperty("value", predicts[5][1]*100)
            self.progressBar_7.setProperty("value", predicts[6][1]*100)
            self.categories = [predicts[i][0].decode(
                'utf-8') for i in range(7)]
            self.retranslateUi(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
