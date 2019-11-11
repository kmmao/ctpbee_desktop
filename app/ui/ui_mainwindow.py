# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Mon Nov 11 16:24:57 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1192, 868)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setBaseSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/images/bee_temp_grey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(28, 28))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 36))
        self.menubar.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.menubar.setFont(font)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.control_menu = QtWidgets.QMenu(self.menubar)
        self.control_menu.setGeometry(QtCore.QRect(270, 163, 159, 96))
        self.control_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.control_menu.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.control_menu.setFont(font)
        self.control_menu.setTabletTracking(False)
        self.control_menu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.control_menu.setWhatsThis("")
        self.control_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.control_menu.setAutoFillBackground(False)
        self.control_menu.setTearOffEnabled(False)
        self.control_menu.setTitle("")
        self.control_menu.setIcon(icon)
        self.control_menu.setSeparatorsCollapsible(False)
        self.control_menu.setToolTipsVisible(False)
        self.control_menu.setObjectName("control_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.account_action = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/icon/account.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_action.setIcon(icon1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.account_action.setFont(font)
        self.account_action.setObjectName("account_action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.market_action = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu/icon/trending-3 行情.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.market_action.setIcon(icon2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.market_action.setFont(font)
        self.market_action.setObjectName("market_action")
        self.looper_action = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu/icon/历史记录.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.looper_action.setIcon(icon3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.looper_action.setFont(font)
        self.looper_action.setObjectName("looper_action")
        self.strategy_action = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/menu/icon/策略.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.strategy_action.setIcon(icon4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.strategy_action.setFont(font)
        self.strategy_action.setObjectName("strategy_action")
        self.order_action = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/menu/icon/下单中心.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.order_action.setIcon(icon5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.order_action.setFont(font)
        self.order_action.setObjectName("order_action")
        self.config_action = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/menu/icon/配置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.config_action.setIcon(icon6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.config_action.setFont(font)
        self.config_action.setObjectName("config_action")
        self.logout_action = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/menu/icon/16-登出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_action.setIcon(icon7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.logout_action.setFont(font)
        self.logout_action.setObjectName("logout_action")
        self.server_logout_action = QtWidgets.QAction(MainWindow)
        self.server_logout_action.setObjectName("server_logout_action")
        self.logout_action_2 = QtWidgets.QAction(MainWindow)
        self.logout_action_2.setIcon(icon7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.logout_action_2.setFont(font)
        self.logout_action_2.setObjectName("logout_action_2")
        self.action = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/menu/icon/关于我们.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action.setIcon(icon8)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.control_menu.addAction(self.action)
        self.menubar.addAction(self.control_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.account_action.setText(QtWidgets.QApplication.translate("MainWindow", "账户", None, -1))
        self.action_2.setText(QtWidgets.QApplication.translate("MainWindow", "行情", None, -1))
        self.market_action.setText(QtWidgets.QApplication.translate("MainWindow", "行情", None, -1))
        self.looper_action.setText(QtWidgets.QApplication.translate("MainWindow", "回测", None, -1))
        self.strategy_action.setText(QtWidgets.QApplication.translate("MainWindow", "策略", None, -1))
        self.order_action.setText(QtWidgets.QApplication.translate("MainWindow", "下单", None, -1))
        self.config_action.setText(QtWidgets.QApplication.translate("MainWindow", "配置", None, -1))
        self.logout_action.setText(QtWidgets.QApplication.translate("MainWindow", "登出", None, -1))
        self.server_logout_action.setText(QtWidgets.QApplication.translate("MainWindow", "服务器登出", None, -1))
        self.logout_action_2.setText(QtWidgets.QApplication.translate("MainWindow", "注销", None, -1))
        self.action.setText(QtWidgets.QApplication.translate("MainWindow", "关于", None, -1))

import app.resource.mainwindow_rc
