# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatgpt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from videotrans.configure import config


class Ui_doubaoform(object):
    def setupUi(self, doubaoform):
        doubaoform.setObjectName("doubaoform")
        doubaoform.setWindowModality(QtCore.Qt.NonModal)
        doubaoform.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(doubaoform.sizePolicy().hasHeightForWidth())
        doubaoform.setSizePolicy(sizePolicy)
        doubaoform.setMaximumSize(QtCore.QSize(600, 500))

        self.label_0 = QtWidgets.QLabel(doubaoform)
        self.label_0.setGeometry(QtCore.QRect(10, 10, 580, 35))
        self.label_0.setText('使用方法见 https://pyvideotrans.com/doubao')

        # line2
        self.label_2 = QtWidgets.QLabel(doubaoform)
        self.label_2.setGeometry(QtCore.QRect(10, 95, 130, 35))
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.doubao_appid = QtWidgets.QLineEdit(doubaoform)
        self.doubao_appid.setGeometry(QtCore.QRect(150, 95, 431, 35))
        self.doubao_appid.setMinimumSize(QtCore.QSize(0, 35))
        self.doubao_appid.setObjectName("doubao_appid")
        # line3

        self.label_3 = QtWidgets.QLabel(doubaoform)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 130, 16))
        self.label_3.setObjectName("label_3")
        self.doubao_access = QtWidgets.QLineEdit(doubaoform)
        self.doubao_access.setGeometry(QtCore.QRect(150, 150, 431, 35))
        self.doubao_access.setMinimumSize(QtCore.QSize(0, 35))
        self.doubao_access.setObjectName("doubao_access")

        self.set_save = QtWidgets.QPushButton(doubaoform)
        self.set_save.setGeometry(QtCore.QRect(10, 200, 93, 35))
        self.set_save.setMinimumSize(QtCore.QSize(0, 35))
        self.set_save.setObjectName("set_save")

        self.retranslateUi(doubaoform)
        QtCore.QMetaObject.connectSlotsByName(doubaoform)

    def retranslateUi(self, doubaoform):
        doubaoform.setWindowTitle("豆包模型音视频识别" if config.defaulelang == 'zh' else 'Doubao')
        self.label_3.setText('填写 Access Token')

        self.set_save.setText('保存')
        self.doubao_appid.setPlaceholderText("填写应用的APP ID")
        self.label_2.setText("APP ID")
