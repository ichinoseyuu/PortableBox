import webbrowser
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from Ui_Settings import Ui_Form
from data.DataManager import UserData, StyleSheetData

class SettingsForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self) #建立窗口布局
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        self.old_pos = None #移动窗口，上一次鼠标指针位置

        # 设置主题选项
        self.ThemeSelects.addItem("浅色模式")
        self.ThemeSelects.addItem("深色模式")
        self.ThemeSelects.addItem("马卡龙配色")
        # 连接 QComboBox 的信号（用户选择项时触发）
        self.ThemeSelects.currentIndexChanged.connect(self.changeTheme)

        # 关于窗口绑定按钮的点击事件
        self.ButtonMin.clicked.connect(self.showMinimized) #最小化
        self.ButtonExit.clicked.connect(self.close)#关闭窗口
        self.ButtonBlog.clicked.connect(self.openMyBlog)# 跳转的我的主页
        #self.ButtonSave.clicked.connect(self.saveSettings)#保存设置

    def openMyBlog(self):
        webbrowser.open('https://ichinoseyuu.github.io/')

    def changeTheme(self):
        if self.ThemeSelects.currentText() == "浅色模式":
            UserData.settingsData['theme'] = 'light'
            self.parent.setStyleSheet(StyleSheetData.themeStyle['light'])
            self.setStyleSheet(StyleSheetData.themeStyle['light'])
            self.parent.update()
            self.update()
        elif self.ThemeSelects.currentText() == "深色模式":
            UserData.settingsData['theme'] = 'dark'
            self.parent.setStyleSheet(StyleSheetData.themeStyle['dark'])
            self.setStyleSheet(StyleSheetData.themeStyle['dark'])
            self.parent.update()
            self.update()
        elif self.ThemeSelects.currentText() == "马卡龙配色":
            UserData.settingsData['theme'] = 'macaron'
            self.parent.setStyleSheet(StyleSheetData.themeStyle['macaron'])
            self.setStyleSheet(StyleSheetData.themeStyle['macaron'])
            self.parent.update()
            self.update()


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
