# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(530, 367)
        self.Button_MenuReturn = QtWidgets.QPushButton(OtherWindow)
        self.Button_MenuReturn.setGeometry(QtCore.QRect(0, 0, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Button_MenuReturn.setFont(font)
        self.Button_MenuReturn.setAutoExclusive(False)
        self.Button_MenuReturn.setObjectName("Button_MenuReturn")
        self.label = QtWidgets.QLabel(OtherWindow)
        self.label.setGeometry(QtCore.QRect(130, 30, 261, 51))
        self.label.setObjectName("label")
        self.Input_VK = QtWidgets.QPushButton(OtherWindow)
        self.Input_VK.setGeometry(QtCore.QRect(220, 170, 93, 28))
        self.Input_VK.setObjectName("Input_VK")
        self.Input_TG = QtWidgets.QPushButton(OtherWindow)
        self.Input_TG.setGeometry(QtCore.QRect(220, 330, 93, 28))
        self.Input_TG.setObjectName("Input_TG")
        self.Chanel_id = QtWidgets.QTextEdit(OtherWindow)
        self.Chanel_id.setGeometry(QtCore.QRect(40, 275, 221, 41))
        self.Chanel_id.setObjectName("Chanel_id")
        self.label_2 = QtWidgets.QLabel(OtherWindow)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 261, 51))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(OtherWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 90, 441, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.VK_login = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.VK_login.setObjectName("VK_login")
        self.verticalLayout_2.addWidget(self.VK_login)
        self.VK_password = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.VK_password.setObjectName("VK_password")
        self.verticalLayout_2.addWidget(self.VK_password)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Group_id = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.Group_id.setObjectName("Group_id")
        self.verticalLayout.addWidget(self.Group_id)
        self.Album_id = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.Album_id.setObjectName("Album_id")
        self.verticalLayout.addWidget(self.Album_id)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label_3 = QtWidgets.QLabel(OtherWindow)
        self.label_3.setGeometry(QtCore.QRect(270, 270, 231, 51))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Dialog"))
        self.Button_MenuReturn.setText(_translate("OtherWindow", "Новость"))
        self.label.setText(_translate("OtherWindow", "<html><head/><body><p><img src=\":/Logos/Logos/VK Text Logo.jpg\"/></p></body></html>"))
        self.Input_VK.setText(_translate("OtherWindow", "РЕГИСТРАЦИЯ"))
        self.Input_TG.setText(_translate("OtherWindow", "РЕГИСТРАЦИЯ"))
        self.Chanel_id.setHtml(_translate("OtherWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ВВЕДИТЕ ЛОГИН КАНАЛА (@....)</p></body></html>"))
        self.label_2.setText(_translate("OtherWindow", "<html><head/><body><p><img src=\":/Logos/Logos/tv-lR1sfN7H1jhYj8LTqBG4zqUk-1920.jpg\"/></p></body></html>"))
        self.VK_login.setHtml(_translate("OtherWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ВВЕДИТЕ ЛОГИН</p></body></html>"))
        self.VK_password.setHtml(_translate("OtherWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ВВЕДИТЕ ПАРОЛЬ</p></body></html>"))
        self.Group_id.setHtml(_translate("OtherWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ID СООБЩЕСТВА</p></body></html>"))
        self.Album_id.setHtml(_translate("OtherWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ID АЛЬБОМА</p></body></html>"))
        self.label_3.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Добавьте @thebestofusee_bot </span></p><p align=\"center\"><span style=\" font-weight:600;\">и предоставьте права администратора</span></p></body></html>"))
