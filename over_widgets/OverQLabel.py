from PySide6.QtWidgets import QMenu, QLabel
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, Property, QDateTime, QProcess
import os
from data.DataManager import UserData, StyleSheetData


class OverQLabel(QLabel):
    def __init__(self, mainWindow, point: tuple[int, int]):
        super(OverQLabel, self).__init__()
        self.mainWindow = mainWindow 
        self.point = point
        self.selected = False  # 初始化为未选中状态
        self.setStyleSheet(StyleSheetData.themeStyle[UserData.settingsData['theme']]) # 设置初始样式
        self.info = None
        self.addTime= QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")

    def dispalyInfo(self):
        self.mainWindow.FileNameLabel.setText(self.info.baseName())
        self.mainWindow.TargetPathLine.setText(self.info.absoluteFilePath())
        self.mainWindow.AddTimeLabel.setText(self.addTime)
        self.mainWindow.CreateTimeLabel.setText(self.info.birthTime().toString("yyyy-MM-dd hh:mm:ss"))
        self.mainWindow.LastModifiedLabel.setText(self.info.lastModified().toString("yyyy-MM-dd hh:mm:ss"))
        self.mainWindow.FileSizeLabel.setText(f"{self.info.size()/1024.0/1024.0:.2f}"+" MB")
        #self.mainWindow.FileSizeLabel.setText("{:.2f} MB".format(self.info.size() / 1024.0 / 1024.0))
        self.getFolderSize(f'{self.info.canonicalPath()}')
    
    def getFolderSize(self,folderPath):
        self.mainWindow.TotalSizeLabel.setText("玩命计算中...")
        self.mainWindow.folderSizeThread.sizeCalculated.connect(lambda size: self.mainWindow.TotalSizeLabel.setText(f"{size/1024.0/1024.0:.2f}"+" MB"))
        self.mainWindow.folderSizeThread.start(folderPath)


    @Property(bool)
    def isSelected(self):
        return self.selected

    @isSelected.setter
    def isSelected(self, value):
        if self.selected != value:
            self.selected = value
            self.setStyleSheet(StyleSheetData.themeStyle[UserData.settingsData['theme']])  # 更新样式

    def updateIndex(self, index):
        self.index = index

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.mainWindow.pointIsSelected == self.point: return
            # 设置当前标签为选中状态
            self.dispalyInfo()
            self.isSelected = not self.isSelected
            if self.mainWindow.pointIsSelected:
                self.mainWindow.getSelectedLabel().deselect()
                self.mainWindow.pointIsSelected = self.point
                self.mainWindow.selectLabel = self
            else:
                self.mainWindow.pointIsSelected = self.point
                self.mainWindow.selectLabel = self
            print(f"app{self.point} is selected")
              

        elif event.button() == Qt.RightButton:
            if self.selected:
                self.showContextMenu(event) 
        #super(OverQLabel, self).mousePressEvent(event) #让父类方法仍然执行

    # 双击打开
    def mouseDoubleClickEvent(self,event):
        event.button() == Qt.LeftButton
        self.mainWindow.openApp(self.info.absoluteFilePath())
        #super(OverQLabel, self).mouseDoubleClickEvent() #让父类方法仍然执行

    # 右键菜单
    def showContextMenu(self, event):
        contextMenu = QMenu(self)
        
        contextMenu.addAction("运行", lambda:self.mainWindow.openApp(self.info.absoluteFilePath()))
        contextMenu.addAction("在资源管理器中显示", lambda:self.showInExplorer(self.info.canonicalPath()))
        contextMenu.addAction("在PortableBox中删除", lambda:self.mainWindow.delApp())
        
        contextMenu.setStyleSheet(StyleSheetData.themeStyle[UserData.settingsData['theme']])
        contextMenu.exec(event.globalPos())

    # 设置为未选中状态
    def deselect(self):
        self.isSelected = False

    def showInExplorer(self, filePath):
        filePath = os.path.normpath(filePath)
        if os.path.exists(filePath):
            print(f"打开目录: {filePath}")
            QProcess.startDetached("explorer", [filePath])