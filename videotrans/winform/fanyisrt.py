import os

from PySide6 import QtWidgets
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QMessageBox, QFileDialog, QPlainTextEdit

from videotrans import translator
from videotrans.configure import config
from videotrans.task.fanyiwork import FanyiWorker
from videotrans.util import tools


# 字幕批量翻译
def open():
    def feed(d):
        if d.startswith("error:"):
            QtWidgets.QMessageBox.critical(config.fanyiform, config.transobj['anerror'], d)
            config.fanyiform.fanyi_start.setText('开始执行' if config.defaulelang == 'zh' else 'start operate')
            config.fanyiform.fanyi_start.setDisabled(False)
            config.fanyiform.fanyi_import.setDisabled(False)
        elif d.startswith('replace:'):
            config.fanyiform.fanyi_targettext.clear()
            config.fanyiform.fanyi_targettext.setPlainText(d[8:])
        elif d.startswith('repsour:'):
            config.fanyiform.fanyi_sourcetext.clear()
            config.fanyiform.fanyi_sourcetext.setPlainText(d[8:])
        elif d.startswith('jd:'):
            config.fanyiform.fanyi_start.setText(d[3:])
        else:
            config.fanyiform.fanyi_start.setText('执行完成/开始执行' if config.defaulelang == 'zh' else 'Ended/Start operate')
            config.fanyiform.fanyi_import.setDisabled(False)
            config.fanyiform.daochu.setDisabled(False)
            config.fanyiform.fanyi_start.setDisabled(False)

    def fanyi_import_fun():
        fnames, _ = QFileDialog.getOpenFileNames(config.fanyiform,
                                                 config.transobj['tuodongfanyi'],
                                                 config.params['last_opendir'],
                                                 "Subtitles files(*.srt)")
        if len(fnames) < 1:
            return
        for (i, it) in enumerate(fnames):
            fnames[i] = it.replace('\\', '/').replace('file:///', '')
        if fnames:
            config.fanyiform.files = fnames
            config.params['last_opendir'] = os.path.dirname(fnames[0])
            config.fanyiform.fanyi_sourcetext.setPlainText(f'{config.transobj["yidaorujigewenjian"]}{len(fnames)}')

    def fanyi_save_fun():
        QDesktopServices.openUrl(QUrl.fromLocalFile(config.homedir + "/translate"))

    def fanyi_start_fun():
        config.settings = config.parse_init()
        target_language = config.fanyiform.fanyi_target.currentText()
        translate_type = config.fanyiform.fanyi_translate_type.currentText()
        if target_language == '-':
            return QMessageBox.critical(config.fanyiform, config.transobj['anerror'], config.transobj["fanyimoshi1"])
        proxy = config.fanyiform.fanyi_proxy.text()

        if proxy:
            tools.set_proxy(proxy)
            config.params['proxy'] = proxy

        rs = translator.is_allow_translate(translate_type=translate_type, show_target=target_language)
        if rs is not True:
            QMessageBox.critical(config.fanyiform, config.transobj['anerror'], rs)
            return
        config.fanyiform.fanyi_sourcetext.clear()
        fanyi_task = FanyiWorker(translate_type, target_language, config.fanyiform.files,config.fanyiform)
        fanyi_task.uito.connect(feed)
        fanyi_task.start()

        config.fanyiform.fanyi_start.setDisabled(True)
        config.fanyiform.fanyi_start.setText(config.transobj["running"])
        config.fanyiform.fanyi_targettext.clear()
        config.fanyiform.daochu.setDisabled(True)

    from videotrans.component import Fanyisrt
    try:
        if config.fanyiform is not None:
            config.fanyiform.show()
            config.fanyiform.raise_()
            config.fanyiform.activateWindow()
            return
        config.fanyiform = Fanyisrt()
        config.fanyiform.fanyi_target.addItems(["-"] + config.langnamelist)
        config.fanyiform.fanyi_import.clicked.connect(fanyi_import_fun)
        config.fanyiform.fanyi_start.clicked.connect(fanyi_start_fun)
        config.fanyiform.fanyi_translate_type.addItems(translator.TRANSNAMES)

        config.fanyiform.fanyi_sourcetext = QPlainTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        config.fanyiform.fanyi_sourcetext.setSizePolicy(sizePolicy)
        config.fanyiform.fanyi_sourcetext.setMinimumSize(300, 0)
        config.fanyiform.fanyi_proxy.setText(config.params['proxy'])

        config.fanyiform.fanyi_sourcetext.setPlaceholderText(config.transobj['tuodongfanyi'])
        config.fanyiform.fanyi_sourcetext.setToolTip(config.transobj['tuodongfanyi'])
        config.fanyiform.fanyi_sourcetext.setReadOnly(True)

        config.fanyiform.fanyi_layout.insertWidget(0, config.fanyiform.fanyi_sourcetext)
        config.fanyiform.daochu.clicked.connect(fanyi_save_fun)

        config.fanyiform.show()
    except Exception as e:
        print(e)
