# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baidu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets

from videotrans.configure import config


class Ui_baiduform(object):
    def setupUi(self, baiduform):
        baiduform.setObjectName("baiduform")
        baiduform.setWindowModality(QtCore.Qt.NonModal)
        baiduform.resize(400, 223)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(baiduform.sizePolicy().hasHeightForWidth())
        baiduform.setSizePolicy(sizePolicy)
        baiduform.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(baiduform)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(baiduform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.baidu_appid = QtWidgets.QLineEdit(baiduform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baidu_appid.sizePolicy().hasHeightForWidth())
        self.baidu_appid.setSizePolicy(sizePolicy)
        self.baidu_appid.setMinimumSize(QtCore.QSize(210, 35))
        self.baidu_appid.setObjectName("baidu_appid")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.baidu_appid)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(baiduform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.baidu_miyue = QtWidgets.QLineEdit(baiduform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baidu_miyue.sizePolicy().hasHeightForWidth())
        self.baidu_miyue.setSizePolicy(sizePolicy)
        self.baidu_miyue.setMinimumSize(QtCore.QSize(210, 35))
        self.baidu_miyue.setObjectName("baidu_miyue")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.baidu_miyue)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.set_badiu = QtWidgets.QPushButton(baiduform)
        self.set_badiu.setMinimumSize(QtCore.QSize(0, 35))
        self.set_badiu.setObjectName("set_badiu")
        self.verticalLayout_2.addWidget(self.set_badiu)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(baiduform)
        QtCore.QMetaObject.connectSlotsByName(baiduform)

    def retranslateUi(self, baiduform):
        baiduform.setWindowTitle("百度")
        self.label.setText("Baidu Appid")
        self.label_2.setText("Baidu Secret")
        self.set_badiu.setText('保存' if config.defaulelang == 'zh' else "Save")
