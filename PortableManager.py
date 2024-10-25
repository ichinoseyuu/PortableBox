import sys
from PySide6.QtWidgets import QApplication, QFileDialog, QLayout,QMainWindow, QFileIconProvider
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QFileInfo, QProcess

from Ui_PortableBox import Ui_MainWindow
from over_widgets.OverQLabel import OverQLabel
from data.DataManager import AppData ,StyleSheetData


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
        self.appData = AppData()
        self.appLayouts ={
            0:{0:self.Col_00,1:self.Col_01,2:self.Col_02,3:self.Col_03,4:self.Col_04,5:self.Col_05,6:self.Col_06,7:self.Col_07,8:self.Col_08,9:self.Col_09},
            1:{0:self.Col_10,1:self.Col_11,2:self.Col_12,3:self.Col_13,4:self.Col_14,5:self.Col_15,6:self.Col_16,7:self.Col_17,8:self.Col_18,9:self.Col_19},
            2:{0:self.Col_20,1:self.Col_21,2:self.Col_22,3:self.Col_23,4:self.Col_24,5:self.Col_25,6:self.Col_26,7:self.Col_27,8:self.Col_28,9:self.Col_29},
            3:{0:self.Col_30,1:self.Col_31,2:self.Col_32,3:self.Col_33,4:self.Col_34,5:self.Col_35,6:self.Col_36,7:self.Col_37,8:self.Col_38,9:self.Col_39}
            }

        # 连接按钮信号
        self.ButtonMin.clicked.connect(self.showMinimized) #最小化
        self.ButtonExit.clicked.connect(self.exitApplication) # 右上角退出 
        self.ButtonAdd.clicked.connect(self.addApp)
        self.ButtonDel.clicked.connect(self.delApp)

        print("UI_Init done")

    def loadData(self):
        self.appData.loadAppData()
        for row in self.appData.appDocker:
            for col in self.appData.appDocker[row]:
                if self.appData.appDocker[row][col]['name'] != "none":
                    self.addAppInData(row, col, f'{self.appData.appDocker[row][col]['path']}')
        print("loadData done")

    
    def saveData(self):
        self.appData.saveAppData()
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
    # 获取显示组件
    def getLayout(self, row: int, col: int):
        return self.appLayouts[row][col]
    
    # 添加app
    def addApp(self):
        selectedFiles, _ = QFileDialog.getOpenFileNames(self, "选择程序", "", "程序 (*.exe)") # 获取选择的文件列表
        if not selectedFiles:
            return 
        iconProvider = QFileIconProvider() # 创建 QFileIconProvider 对象，用来获取exe图标
        for file in selectedFiles:
            fileInfo = QFileInfo(file) # 获取第一个文件路径的信息
            icon = iconProvider.icon(fileInfo) # 获取exe图标
            pixmap = QPixmap(icon.pixmap(48, 48))  # 将图标转换为 QPixmap 对象
            scaledPixmap = pixmap.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation) # 调整图标大小
            row, col = self.appData.getFisrtEmpty() # 获取字典中的第一个空位置
            app = OverQLabel(self, [row,col], f"{fileInfo.baseName()}") # 创建 OverQLabel 对象来存储信息
            app.setAlignment(Qt.AlignCenter) # 居中显示
            self.appData.updateElement(row, col,f"{fileInfo.baseName()}",f"{fileInfo.absoluteFilePath()}", app) 
            self.horizontalLayout[row].insertWidget(self.horizontalLayout[row].count() - 1, app) #添加到布局中
            app.setPixmap(scaledPixmap) # 设置图标
            app.info = fileInfo # 存储文件信息

    def addAppInData(self, row: int, col: int, path: str):
        fileInfo = QFileInfo(path) # 获取第一个文件路径的信息
        iconProvider = QFileIconProvider() # 创建 QFileIconProvider 对象，用来获取exe图标
        icon = iconProvider.icon(fileInfo) # 获取exe图标
        pixmap = QPixmap(icon.pixmap(48, 48))  # 将图标转换为 QPixmap 对象
        scaledPixmap = pixmap.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation) # 调整图标大小
        app = OverQLabel(self, [row,col], f"{fileInfo.baseName()}") # 创建 OverQLabel 对象来存储信息
        app.setAlignment(Qt.AlignCenter) # 居中显示  
        self.appData.updateElementValue(row, col,'app', app) 
        self.horizontalLayout[row].insertWidget(self.horizontalLayout[row].count() - 1, app) #添加到布局中
        app.setPixmap(scaledPixmap) # 设置图标
        app.info = fileInfo # 存储文件信息


    # 打开app
    def openApp(self, path):
        print(path+"is open")
        QProcess.startDetached(f'"{path}"')

    # 删除app
    def delApp(self):
        # 获取所有不为空标签
        apps = self.appData.getNonEmptyElements()
        for key in apps:
            if apps[key]['app'].selected:
                apps[key]['app'].setParent(None)  # 从布局中移除标签
                self.appData.removeElementInTuple(apps[key]['app'].index)
                print(f'app{apps[key]['app'].index} is deleted') 
        self.upDateLayout()

    def upDateLayout(self):
        point = self.appData.whatsRowHaveNoneElement(1)
        for i in range(1, point[0]+1):
            self.horizontalLayout[i].update()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = PortableAppManager()
    mainWindow.show()
    sys.exit(app.exec())