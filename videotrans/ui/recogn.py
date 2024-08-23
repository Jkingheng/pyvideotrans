# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolboxen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from videotrans.configure import config
from videotrans.configure.config import box_lang


class Ui_recogn(object):
    def setupUi(self, recogn):
        recogn.setObjectName("recogn")

        self.centralwidget = QtWidgets.QWidget(recogn)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.shibie_out_path = None

        # 语音识别
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(recogn)

        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.shibie_widget = QtWidgets.QVBoxLayout()
        self.shibie_widget.setObjectName("shibie_widget")
        self.verticalLayout_3.addLayout(self.shibie_widget)


        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.shibie_language = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_language.sizePolicy().hasHeightForWidth())
        self.shibie_language.setSizePolicy(sizePolicy)
        self.shibie_language.setMinimumSize(QtCore.QSize(0, 30))
        self.shibie_language.setObjectName("shibie_language")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.shibie_language)
        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.formLayout_2.setObjectName("formLayout_2")

        self.is_cuda = QtWidgets.QCheckBox()
        self.is_cuda.setObjectName("is_cuda")
        self.is_cuda.setText("启用CUDA?" if config.defaulelang == 'zh' else 'Enable CUDA?')

        self.shibie_model_type = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_model_type.sizePolicy().hasHeightForWidth())
        self.shibie_model_type.setSizePolicy(sizePolicy)
        self.shibie_model_type.setMinimumSize(QtCore.QSize(0, 30))
        self.shibie_model_type.setObjectName("shibie_model_type")
        self.shibie_model_type.addItems([
            config.uilanglist['faster model'],
            config.uilanglist['openai model'],
            "GoogleSpeech",
            "zh_recogn中文识别" if config.defaulelang == 'zh' else "zh_recogn only Chinese",
            "豆包模型识别" if config.defaulelang == 'zh' else "Doubao"
        ])

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.shibie_model_type)

        self.shibie_model = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_model.sizePolicy().hasHeightForWidth())
        self.shibie_model.setSizePolicy(sizePolicy)
        self.shibie_model.setMinimumSize(QtCore.QSize(0, 30))
        self.shibie_model.setObjectName("shibie_model")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.shibie_model)

        self.shibie_whisper_type = QtWidgets.QComboBox()
        self.shibie_whisper_type.addItems(
            [config.transobj['whisper_type_all'],
             config.transobj['whisper_type_avg']]
        )
        self.shibie_whisper_type.setToolTip(config.transobj['fenge_tips'])
        self.horizontalLayout.addWidget(self.is_cuda)

        self.horizontalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout.addWidget(self.shibie_whisper_type)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)

        self.shibie_startbtn = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_startbtn.sizePolicy().hasHeightForWidth())
        self.shibie_startbtn.setSizePolicy(sizePolicy)
        self.shibie_startbtn.setMinimumSize(QtCore.QSize(200, 30))
        self.shibie_startbtn.setObjectName("shibie_startbtn")

        self.horizontalLayout_8.addWidget(self.shibie_startbtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.shibie_text = QtWidgets.QPlainTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_text.sizePolicy().hasHeightForWidth())
        self.shibie_text.setSizePolicy(sizePolicy)
        self.shibie_text.setObjectName("shibie_text")
        self.verticalLayout_3.addWidget(self.shibie_text)

        self.shibie_savebtn = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_savebtn.sizePolicy().hasHeightForWidth())
        self.shibie_savebtn.setSizePolicy(sizePolicy)
        self.shibie_savebtn.setObjectName("shibie_savebtn")
        self.shibie_savebtn.hide()

        self.shibie_opendir = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shibie_opendir.sizePolicy().hasHeightForWidth())
        self.shibie_opendir.setSizePolicy(sizePolicy)
        self.shibie_opendir.setFixedHeight(30)
        self.shibie_opendir.setObjectName("shibie_opendir")
        self.shibie_opendir.setText('打开识别结果保存目录' if config.defaulelang == 'zh' else 'Open Output dir')
        self.shibie_opendir.setDisabled(True)

        self.horizontalLayout_shibie8 = QtWidgets.QHBoxLayout()

        self.horizontalLayout_shibie8.addWidget(self.shibie_opendir)
        self.horizontalLayout_shibie8.addWidget(self.shibie_savebtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_shibie8)

        self.label_shibie10 = QtWidgets.QLabel()
        self.verticalLayout_3.addWidget(self.label_shibie10)

        self.horizontalLayout_9.addLayout(self.verticalLayout_3)





        self.retranslateUi(recogn)
        QtCore.QMetaObject.connectSlotsByName(recogn)

    def retranslateUi(self, recogn):
        recogn.setWindowTitle('音视频识别为字幕' if config.defaulelang=='zh'else 'Audio and video recognized as subtitles')
        self.label_3.setText(box_lang.get("Source lang"))
        self.shibie_startbtn.setText(box_lang.get("Start"))
        self.shibie_savebtn.setText(box_lang.get("Save to srt.."))
