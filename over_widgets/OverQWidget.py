from PySide6.QtWidgets import QMenu, QWidget
from PySide6.QtGui import  QFont, QAction
from PySide6.QtCore import Qt,Property

class OverQWidget(QWidget):
    def __init__(self, mainWindow, parent=None):
        super().__init__(parent)
        self.mainWindow = mainWindow
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        
    def showContextMenu(self):
        contextMenu = QMenu(self)
        contextMenu.addAction("添加程序", self.mainWindow.addApp())
        contextMenu.setFont(QFont('微软雅黑', 10))
        contextMenu.setStyleSheet("QMenu { font-family: '微软雅黑'; font-size: 10pt; color: #333333; }")
        contextMenu.exec_()