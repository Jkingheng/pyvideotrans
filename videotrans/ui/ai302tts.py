# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatgpt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from videotrans.configure import config


class Ui_ai302ttsform(object):
    def setupUi(self, ai302ttsform):
        ai302ttsform.setObjectName("ai302ttsform")
        ai302ttsform.setWindowModality(QtCore.Qt.NonModal)
        ai302ttsform.resize(600, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ai302ttsform.sizePolicy().hasHeightForWidth())
        ai302ttsform.setSizePolicy(sizePolicy)
        ai302ttsform.setMaximumSize(QtCore.QSize(600, 450))

        self.label_0 = QtWidgets.QPushButton(ai302ttsform)
        self.label_0.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_0.setGeometry(QtCore.QRect(10, 10, 580, 35))
        self.label_0.setMinimumSize(QtCore.QSize(580, 35))
        self.label_0.setStyleSheet("""text-align:left;background-color:transparent""")
        self.label_0.setText('在此填写 https://302.ai 管理后台-Api超市-Api管理-创建的API KEY,若没有可点此去创建')

        self.label_01 = QtWidgets.QPushButton(ai302ttsform)
        self.label_01.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_01.setGeometry(QtCore.QRect(10, 50, 580, 35))
        self.label_01.setMinimumSize(QtCore.QSize(580, 35))
        self.label_01.setStyleSheet("""text-align:left;background-color:transparent""")
        self.label_01.setText('点此查看使用教程 https://pyvideotrans.com/302ai')

        self.label_2 = QtWidgets.QLabel(ai302ttsform)
        self.label_2.setGeometry(QtCore.QRect(10, 95, 130, 35))
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.ai302tts_key = QtWidgets.QLineEdit(ai302ttsform)
        self.ai302tts_key.setGeometry(QtCore.QRect(150, 95, 431, 35))
        self.ai302tts_key.setMinimumSize(QtCore.QSize(0, 35))
        self.ai302tts_key.setObjectName("ai302tts_key")

        self.label_3 = QtWidgets.QLabel(ai302ttsform)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 121, 16))
        self.label_3.setObjectName("label_3")
        self.ai302tts_model = QtWidgets.QComboBox(ai302ttsform)

        self.ai302tts_model.setGeometry(QtCore.QRect(150, 145, 431, 35))
        self.ai302tts_model.setMinimumSize(QtCore.QSize(0, 35))
        self.ai302tts_model.setObjectName("ai302tts_model")

        self.label_allmodels = QtWidgets.QLabel(ai302ttsform)
        self.label_allmodels.setGeometry(QtCore.QRect(10, 200, 571, 21))
        self.label_allmodels.setObjectName("label_allmodels")

        self.edit_allmodels = QtWidgets.QPlainTextEdit(ai302ttsform)
        self.edit_allmodels.setGeometry(QtCore.QRect(10, 235, 571, 100))
        self.edit_allmodels.setObjectName("edit_allmodels")
        self.edit_allmodels.setReadOnly(True)

        self.set_ai302tts = QtWidgets.QPushButton(ai302ttsform)
        self.set_ai302tts.setGeometry(QtCore.QRect(10, 350, 93, 35))
        self.set_ai302tts.setMinimumSize(QtCore.QSize(0, 35))
        self.set_ai302tts.setObjectName("set_ai302tts")

        self.test_ai302tts = QtWidgets.QPushButton(ai302ttsform)
        self.test_ai302tts.setGeometry(QtCore.QRect(130, 355, 93, 30))
        self.test_ai302tts.setMinimumSize(QtCore.QSize(0, 30))
        self.test_ai302tts.setObjectName("test_ai302tts")

        self.retranslateUi(ai302ttsform)
        QtCore.QMetaObject.connectSlotsByName(ai302ttsform)

    def retranslateUi(self, ai302ttsform):
        ai302ttsform.setWindowTitle("302.ai 接入配音渠道配置")
        self.label_3.setText('选择模型')
        self.label_allmodels.setText('填写所有可用模型，以英文逗号分隔,填写后可在上方选择,目前仅支持tts-1,tts-1-hd')
        self.set_ai302tts.setText('保存')
        self.test_ai302tts.setText('测试..')
        self.ai302tts_key.setPlaceholderText("在api超市-api管理-创建API KEY")
        self.ai302tts_key.setToolTip("如果没有账号，可去 https://302.ai 注册，有7元免费额度")
        self.label_2.setText("API KEY")
