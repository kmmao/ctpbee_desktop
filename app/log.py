from PySide2.QtCore import Qt, QTimer, Slot
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QDialog
from app.ui.ui_log import Ui_Log


class LogDialog(QDialog, Ui_Log):
    def __init__(self, mainwindow):
        super(LogDialog, self).__init__()
        self.setupUi(self)
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)#窗口置顶
        self.mainwindow = mainwindow
        self.mainwindow.job.order_log_signal.connect(self.set_log_slot)

    @Slot(str)
    def set_log_slot(self, record: str):
        self.log_list.insertItem(0, record)
        if self.log_list.count() > 500:
            self.log_list.clear()

    def closeEvent(self, arg__1: QCloseEvent):
        self.mainwindow.log_dialog = None
        arg__1.accept()
