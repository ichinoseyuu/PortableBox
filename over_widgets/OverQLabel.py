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
        self.setStyleSheet(StyleSheetData.themeMap[UserData.settingsData['theme']]) # 设置初始样式
        self.info = None
        self.addTime= QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")

    def displayInfo(self):
        self.mainWindow.FileNameLabel.setText(self.info.baseName())
        self.mainWindow.TargetPathLine.setText(self.info.absoluteFilePath())
        self.mainWindow.AddTimeLabel.setText(self.addTime)
        #self.mainWindow.CreateTimeLabel.setText(self.info.birthTime().toString("yyyy-MM-dd hh:mm:ss"))
        #self.mainWindow.LastModifiedLabel.setText(self.info.lastModified().toString("yyyy-MM-dd hh:mm:ss"))
        #self.mainWindow.FileSizeLabel.setText(f"{self.info.size()/1024.0/1024.0:.2f}"+" MB")
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
            self.setStyleSheet(StyleSheetData.themeMap[UserData.settingsData['theme']])  # 更新样式

    def updateIndex(self, index):
        self.index = index

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 单选模式
            if not self.mainWindow.isMultiSelectMode:
                if self.mainWindow.pointIsSelected == self.point: return # 如果当前点已经被选中，直接返回
                self.displayInfo()
                self.isSelected = not self.isSelected # 切换当前点的选择状态
                if self.mainWindow.pointIsSelected:  # 如果已有选中的点
                    self.mainWindow.getSelectedLabel().deselect()  # 取消之前选中的点
                self.mainWindow.pointIsSelected = self.point  # 更新为当前选中的点
                self.mainWindow.selectLabel = self  # 更新当前选中的标签
                print(f"app{self.point} is selected")
            # 多选模式
            elif self.mainWindow.isMultiSelectMode:
                self.isSelected = not self.isSelected # 切换当前点的选择状态
                if self.isSelected:
                    self.displayInfo() # 如果当前点被选中，显示信息
                    self.mainWindow.selectedLabels.append(self)  # 添加当前选中的标签
                else: 
                    self.mainWindow.updateLabelText() # 如果当前点被取消选中，清空信息
                    self.deselect()
                    #self.mainWindow.getSelectedLabel().deselect()  # 取消选中的点
                    self.mainWindow.selectedLabels.remove(self) # 移除最后一个标签

        elif event.button() == Qt.RightButton:
            # 单选模式
            if not self.mainWindow.isMultiSelectMode:
                if self.selected:
                    self.showContextMenu(event)
            # 多选模式
            elif self.mainWindow.isMultiSelectMode:
                if self.selected:
                    self.showContextMenuMultiSelectMode(event)
        #super(OverQLabel, self).mousePressEvent(event) #让父类方法仍然执行

    # 双击打开
    def mouseDoubleClickEvent(self,event):
        if event.button() == Qt.LeftButton:  # 检查是否是左键
            self.mainWindow.openApp(self.info.absoluteFilePath())
        #super(OverQLabel, self).mouseDoubleClickEvent() #让父类方法仍然执行

    # 右键菜单
    def showContextMenu(self, event):
        contextMenu = QMenu(self)
        contextMenu.addAction("运行", lambda:self.mainWindow.openApp(self.info.absoluteFilePath()))
        contextMenu.addAction("在资源管理器中显示", lambda:self.showInExplorer(self.info.canonicalPath()))
        contextMenu.addAction("在PortableBox中删除", lambda:self.mainWindow.delApp()) 
        contextMenu.setStyleSheet(StyleSheetData.themeMap[UserData.settingsData['theme']])
        contextMenu.exec(event.globalPos())

    def showContextMenuMultiSelectMode(self, event):
        contextMenu = QMenu(self)
        action = QAction("在PortableBox中删除", self.mainWindow)
        action.triggered.connect(lambda: self.mainWindow.delApp())
        contextMenu.addAction(action)
        contextMenu.setStyleSheet(StyleSheetData.themeMap[UserData.settingsData['theme']])
        contextMenu.exec(event.globalPos())

    # 设置为未选中状态
    def deselect(self):
        self.isSelected = False

    def select(self):
        self.isSelected = True

    def showInExplorer(self, filePath):
        filePath = os.path.normpath(filePath)
        if os.path.exists(filePath):
            print(f"open: {filePath}")
            QProcess.startDetached("explorer", [filePath])