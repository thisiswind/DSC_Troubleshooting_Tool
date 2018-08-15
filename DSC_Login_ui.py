# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DSC_Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_login(object):
    def setupUi(self, Dialog_login):
        Dialog_login.setObjectName("Dialog_login")
        Dialog_login.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_login.resize(353, 166)
        Dialog_login.setMinimumSize(QtCore.QSize(353, 166))
        Dialog_login.setMaximumSize(QtCore.QSize(353, 166))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/donkey_login/dsc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_login.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog_login)
        self.label.setGeometry(QtCore.QRect(70, 20, 101, 16))
        self.label.setObjectName("label")
        self.pushButton_login = QtWidgets.QPushButton(Dialog_login)
        self.pushButton_login.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.layoutWidget = QtWidgets.QWidget(Dialog_login)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 50, 195, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_gib = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_gib.setPlaceholderText("")
        self.lineEdit_gib.setClearButtonEnabled(False)
        self.lineEdit_gib.setObjectName("lineEdit_gib")
        self.verticalLayout_2.addWidget(self.lineEdit_gib)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_2.addWidget(self.lineEdit_password)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog_login)
        QtCore.QMetaObject.connectSlotsByName(Dialog_login)

    def retranslateUi(self, Dialog_login):
        _translate = QtCore.QCoreApplication.translate
        Dialog_login.setWindowTitle(_translate("Dialog_login", "Login"))
        self.label.setText(_translate("Dialog_login", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Please login</span></p></body></html>"))
        self.pushButton_login.setText(_translate("Dialog_login", "Login"))
        self.pushButton_login.setShortcut(_translate("Dialog_login", "Return"))
        self.label_2.setText(_translate("Dialog_login", "    GID:"))
        self.label_3.setText(_translate("Dialog_login", "Password:"))

import donkey_for_login_window_rc
