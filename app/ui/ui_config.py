# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui',
# licensing of 'config.ui' applies.
#
# Created: Sun Sep 29 21:39:46 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName("Config")
        Config.resize(1151, 782)
        font = QtGui.QFont()
        font.setPointSize(13)
        Config.setFont(font)
        self.formLayout_2 = QtWidgets.QFormLayout(Config)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(Config)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Config)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Config)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Config)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(Config)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Config)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(Config)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(Config)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(Config)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.pushButton = QtWidgets.QPushButton(Config)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/icon/上传.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.INSTRUMENT_INDEPEND = QtWidgets.QCheckBox(Config)
        self.INSTRUMENT_INDEPEND.setText("")
        self.INSTRUMENT_INDEPEND.setObjectName("INSTRUMENT_INDEPEND")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.INSTRUMENT_INDEPEND)
        self.SLIPPAGE_SHORT = QtWidgets.QSpinBox(Config)
        self.SLIPPAGE_SHORT.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SLIPPAGE_SHORT.setObjectName("SLIPPAGE_SHORT")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SLIPPAGE_SHORT)
        self.SLIPPAGE_BUY = QtWidgets.QSpinBox(Config)
        self.SLIPPAGE_BUY.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SLIPPAGE_BUY.setObjectName("SLIPPAGE_BUY")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.SLIPPAGE_BUY)
        self.SLIPPAGE_COVER = QtWidgets.QSpinBox(Config)
        self.SLIPPAGE_COVER.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SLIPPAGE_COVER.setObjectName("SLIPPAGE_COVER")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.SLIPPAGE_COVER)
        self.SLIPPAGE_SELL = QtWidgets.QSpinBox(Config)
        self.SLIPPAGE_SELL.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SLIPPAGE_SELL.setObjectName("SLIPPAGE_SELL")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.SLIPPAGE_SELL)
        self.CLOSE_PATTERN = QtWidgets.QComboBox(Config)
        self.CLOSE_PATTERN.setMaximumSize(QtCore.QSize(200, 16777215))
        self.CLOSE_PATTERN.setObjectName("CLOSE_PATTERN")
        self.CLOSE_PATTERN.addItem("")
        self.CLOSE_PATTERN.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.CLOSE_PATTERN)
        self.SHARED_FUNC = QtWidgets.QCheckBox(Config)
        self.SHARED_FUNC.setText("")
        self.SHARED_FUNC.setObjectName("SHARED_FUNC")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.SHARED_FUNC)
        self.REFRESH_INTERVAL = QtWidgets.QDoubleSpinBox(Config)
        self.REFRESH_INTERVAL.setMaximumSize(QtCore.QSize(200, 16777215))
        self.REFRESH_INTERVAL.setObjectName("REFRESH_INTERVAL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.REFRESH_INTERVAL)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.formLayout)

        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        Config.setWindowTitle(QtWidgets.QApplication.translate("Config", "Form", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Config", "配置", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Config", "REFRESH_INTERVAL", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Config", "INSTRUMENT_INDEPEND", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Config", "SLIPPAGE_SHORT", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Config", "SLIPPAGE_BUY", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Config", "SLIPPAGE_COVER", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Config", "SLIPPAGE_SELL", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Config", "CLOSE_PATTERN", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Config", "SHARED_FUNC", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Config", "提交更改", None, -1))
        self.CLOSE_PATTERN.setItemText(0, QtWidgets.QApplication.translate("Config", "today", None, -1))
        self.CLOSE_PATTERN.setItemText(1, QtWidgets.QApplication.translate("Config", "yesterday", None, -1))

import app.resource.mainwindow_rc
