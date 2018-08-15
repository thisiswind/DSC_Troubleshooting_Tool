# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Input_alarms.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_input_alarms(object):
    def setupUi(self, Dialog_input_alarms):
        Dialog_input_alarms.setObjectName("Dialog_input_alarms")
        Dialog_input_alarms.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_input_alarms.resize(643, 356)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/donkey/dsc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_input_alarms.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog_input_alarms)
        self.label.setGeometry(QtCore.QRect(20, 10, 211, 16))
        self.label.setObjectName("label")
        self.textEdit_alarm_content = QtWidgets.QTextEdit(Dialog_input_alarms)
        self.textEdit_alarm_content.setGeometry(QtCore.QRect(20, 40, 611, 261))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textEdit_alarm_content.setPalette(palette)
        self.textEdit_alarm_content.setObjectName("textEdit_alarm_content")
        self.layoutWidget = QtWidgets.QWidget(Dialog_input_alarms)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 320, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_ok = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.retranslateUi(Dialog_input_alarms)
        QtCore.QMetaObject.connectSlotsByName(Dialog_input_alarms)

    def retranslateUi(self, Dialog_input_alarms):
        _translate = QtCore.QCoreApplication.translate
        Dialog_input_alarms.setWindowTitle(_translate("Dialog_input_alarms", "Input alarms"))
        self.label.setText(_translate("Dialog_input_alarms", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Please paste alarms here:</span></p></body></html>"))
        self.pushButton_ok.setText(_translate("Dialog_input_alarms", "OK"))
        self.pushButton_cancel.setText(_translate("Dialog_input_alarms", "Cancel"))

import donkey_for_input_alarms_window_rc
