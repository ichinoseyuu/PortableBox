import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QLayout,QMainWindow, QFileIconProvider
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QFileInfo, QProcess

from Ui_PortableBox import Ui_MainWindow
from over_widgets.OverQLabel import OverQLabel
from data.DataManager import UserData, StyleSheetData


class PortableAppManager(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setupUi(self)  # 设置界面
        self.UI_Init()  # 初始化UI
        self.loadData()

    def UI_Init(self):
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果

        self.old_pos = None #移动窗口，上一次鼠标指针位置
        self.styleData = StyleSheetData.loadStyleSheetData("theme\\styleSheet.qss")
        self.appLayouts ={
            0:{0:self.Col_00,1:self.Col_01,2:self.Col_02,3:self.Col_03,4:self.Col_04,5:self.Col_05,6:self.Col_06,7:self.Col_07,8:self.Col_08,9:self.Col_09},
            1:{0:self.Col_10,1:self.Col_11,2:self.Col_12,3:self.Col_13,4:self.Col_14,5:self.Col_15,6:self.Col_16,7:self.Col_17,8:self.Col_18,9:self.Col_19},
            2:{0:self.Col_20,1:self.Col_21,2:self.Col_22,3:self.Col_23,4:self.Col_24,5:self.Col_25,6:self.Col_26,7:self.Col_27,8:self.Col_28,9:self.Col_29},
            3:{0:self.Col_30,1:self.Col_31,2:self.Col_32,3:self.Col_33,4:self.Col_34,5:self.Col_35,6:self.Col_36,7:self.Col_37,8:self.Col_38,9:self.Col_39}
            }
        self.rowCount = self.appLayouts.__len__()
        self.colCount = self.appLayouts[0].__len__()
        print(self.rowCount,self.colCount)
        self.userData = UserData((self.rowCount, self.colCount))
        self.pointIsSelected = ()
        # 连接按钮信号
        self.ButtonMin.clicked.connect(self.showMinimized) #最小化
        self.ButtonExit.clicked.connect(self.exitApplication) # 右上角退出 
        self.ButtonAdd.clicked.connect(self.addApp)
        self.ButtonDel.clicked.connect(self.delApp)
        print("UI_Init done")

    def loadData(self):
        self.userData.loadUserData()
        iconProvider = QFileIconProvider() # 创建 QFileIconProvider 对象，用来获取exe图标
        for row in self.userData.appDocker:
            for col in self.userData.appDocker[row]:
                if self.userData.appDocker[row][col]['path'] != 'none':
                    #self.addAppInData(row, col, f'{self.userData.appDocker[row][col]['path']}')
                    fileInfo = QFileInfo(f'{self.userData.appDocker[row][col]['path']}') # 获取文件路径的信息
                    icon = iconProvider.icon(fileInfo) # 获取exe图标
                    pixmap = QPixmap(icon.pixmap(48, 48))  # 将图标转换为 QPixmap 对象
                    scaledPixmap = pixmap.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    layout = self.getLayout(row, col) # 获取该位置的布局
                    label = OverQLabel(self, (row, col)) # 创建 OverQLabel 对象来存储信息
                    label.setAlignment(Qt.AlignCenter) # 居中显示
                    layout.addWidget(label) #添加到布局中
                    label.setPixmap(scaledPixmap) # 设置图标
                    label.info = fileInfo # 存储文件信息
        print("loadData done")

    
    def saveData(self):
        self.userData.saveUserData()
        print("saveData done")


    #退出程序
    def exitApplication(self):
        self.saveData()
        print("exitApplication")
        QApplication.instance().quit()

    #拖动窗口相关函数 mousePressEvent mouseMoveEvent mouseReleaseEvent
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()  # 记录鼠标按下时的位置

    def mouseMoveEvent(self, event):
        if self.old_pos is not None and event.buttons() == Qt.LeftButton:
            delta = event.globalPosition().toPoint() - self.old_pos  # 计算位置变化
            self.move(self.x() + delta.x(), self.y() + delta.y())  # 移动窗口
            self.old_pos = event.globalPosition().toPoint()  # 更新旧位置

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None  # 释放鼠标时重置旧位置

    # 通过坐标获取组件
    def getLayout(self, row: int, col: int):
        return self.appLayouts[row][col]
    
    def getLayoutByTuple(self, point: tuple[int, int]):
        return self.appLayouts[point[0]][point[1]]
    
    #  获取被选择的label
    def getSelectedLabel(self):
        if not self.pointIsSelected:
            return
        layout = self.getLayoutByTuple(self.pointIsSelected)
        return layout.itemAt(0).widget()
        # 1：return [layout.itemAt(i).widget() for i in range(layout.count())]
        # 2：# 遍历布局中的每个项
        #   for i in range(layout.count()):
        #       item = layout.itemAt(i)  # 获取布局中的第 i 项
        #       if isinstance(widget, OverQLabel):  # 检查部件是否是 OverQLabel
        #           over_labels.append(widget)  # 将 OverQLabel 添加到列表中 
    
    # 判断是否为空
    def isEmpty(self, row: int, col: int) -> bool:
        return self.appLayouts(row, col).count() == 0
    
    # 获取第一个非空组件的坐标
    def getFirstEmptyPoint(self):
        for row in self.appLayouts:
            for col in self.appLayouts[row]:
                if self.appLayouts[row][col].count() == 0:
                    return row, col
        return None, None
    
    # 获取第一个非空组件
    def getFirstEmptyLayout(self):
        for row in self.appLayouts:
            for col in self.appLayouts[row]:
                if self.appLayouts[row][col].count() == 0:
                    return self.appLayouts[row][col]
        return None
    
    
    # 获取所有非空组件
    def getNonEmptyLayouts(self):
        nonEmptyLayouts = []
        for row in self.appLayouts:
            for col in self.appLayouts[row]:
                if self.appLayouts[row][col].count() != 0:
                    nonEmptyLayouts.append(self.appLayouts[row][col])
        return nonEmptyLayouts
    
    # 获取所有非空组件中的labels
    def getAllLabels(self):
        layouts = self.getNonEmptyLayouts()
        return [layouts.itemAt(i).widget() for i in range(layouts.count())]
    
    # 添加app
    def addApp(self):
        selectedFiles, _ = QFileDialog.getOpenFileNames(self, "选择程序", "", "程序 (*.exe)") # 获取选择的文件列表
        if not selectedFiles: return 
        iconProvider = QFileIconProvider() # 创建 QFileIconProvider 对象，用来获取exe图标
        for file in selectedFiles:
            fileInfo = QFileInfo(file) # 获取第一个文件路径的信息
            icon = iconProvider.icon(fileInfo) # 获取exe图标
            pixmap = QPixmap(icon.pixmap(48, 48))  # 将图标转换为 QPixmap 对象
            scaledPixmap = pixmap.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation) # 调整图标大小
            row, col= self.getFirstEmptyPoint() # 获取字典中的第一个空位置
            layout = self.getLayout(row, col) # 获取该位置的布局
            label = OverQLabel(self, (row, col)) # 创建 OverQLabel 对象来存储信息
            label.setAlignment(Qt.AlignCenter) # 居中显示
            layout.addWidget(label) #添加到布局中
            label.setPixmap(scaledPixmap) # 设置图标
            label.info = fileInfo # 存储文件信息
            self.userData.updateAppDockerPath(row, col,f'{fileInfo.absoluteFilePath()}') # 更新数据


    # 打开app
    def openApp(self, path):
        print(path+"is open")
        QProcess.startDetached(f'"{path}"')

    # 删除app
    def delApp(self):
        if not self.pointIsSelected: return
        layout = self.getLayoutByTuple(self.pointIsSelected)
        label = layout.itemAt(0).widget()
        layout.removeWidget(label) # 删除布局中的控件
        self.userData.updateAppDockerPath(self.pointIsSelected[0], self.pointIsSelected[1], 'none')
        label.deleteLater() # 删除控件
        print(f'app{self.pointIsSelected}is deleted')
        self.updateAllLabels(self.pointIsSelected[0],self.pointIsSelected[1])
        self.pointIsSelected = ()
        self.userData.displayData()

    def updateAllLabels(self, row: int, col: int):
        # 当前列是最后一列，在最后一行
        if col == self.colCount - 1 and row + 1 == self.rowCount: 
            self.userData.updateAppDockerPath(row, col, 'none') # 更新数据
            return
        # 当前列是最后一列，但不在最后一行
        if col == self.colCount - 1:
            layoutLast = self.getLayout(row, col)
            layoutNextRow = self.getLayout(row + 1, 0)
            if layoutNextRow.count() == 0: return
            label = layoutNextRow.itemAt(0).widget()
            layoutNextRow.removeWidget(label)
            layoutLast.addWidget(label)
            label.point = (row, col)
            self.userData.updateAppDockerPath(row + 1, col, 'none') # 更新数据
            self.userData.updateAppDockerPath(row, col, f'{label.info.absoluteFilePath()}')
            return self.updateAllLabels(row + 1, 0)
        # 当前列不是最后一列
        layoutLast = self.getLayout(row, col)
        layout = self.getLayout(row, col + 1)
        if layout.count() == 0: return      
        label = layout.itemAt(0).widget()
        layout.removeWidget(label)
        layoutLast.addWidget(label)
        label.point = (row, col)
        self.userData.updateAppDockerPath(row, col + 1, 'none') # 更新数据
        self.userData.updateAppDockerPath(row, col, f'{label.info.absoluteFilePath()}') # 更新数据
        return self.updateAllLabels(row, col + 1)
    
    def moveLabel(self, point: tuple[int,int], targetPoint: tuple[int,int]):
        layoutLast = self.getLayoutByTuple(targetPoint)
        layout = self.getLayout(point)
        if layout.count() == 0:
            return 'Col is Done' 
        else:
            label = [layout.itemAt(i).widget() for i in range(layout.count())][0]
            layout.removeWidget(label)
            layoutLast.addWidget(label)
            label.point = (targetPoint[0], targetPoint[1]) 
           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = PortableAppManager()
    mainWindow.show()
    sys.exit(app.exec())