import webbrowser
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit
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
        self.ThemeSelect.addItems(['浅色模式','深色模式','马卡龙'])
        # 连接 QComboBox 的信号（用户选择项时触发）
        self.ThemeSelect.currentIndexChanged.connect(self.changeTheme)
        self.FontSelect.addItems(["微软雅黑","幼圆","宋体","楷体","黑体"])
        # 连接 QComboBox 的信号（用户选择项时触发）
        self.FontSelect.currentIndexChanged.connect(self.changeFont)

        # 关于窗口绑定按钮的点击事件
        self.ButtonMin.clicked.connect(self.showMinimized) #最小化
        self.ButtonExit.clicked.connect(self.close)#关闭窗口
        self.ButtonBlog.clicked.connect(lambda:self.openWeb('https://ichinoseyuu.github.io/'))# 跳转的我的主页
        self.ButtonGithub.clicked.connect(lambda:self.openWeb('https://github.com/ichinoseyuu'))# 跳转的我的github
        #self.ButtonSave.clicked.connect(self.saveSettings)#保存设置


    def openWeb(self, url):
        webbrowser.open(url)

    def changeTheme(self):
        # 获取当前选择的主题
        selectedTheme = StyleSheetData.getThemeNameEN(self.ThemeSelect.currentText())
        # 更新 UserData 设置
        UserData.settingsData['theme'] = selectedTheme
        # 设置样式表
        self.parent.setStyleSheet(StyleSheetData.themeMap[selectedTheme])
        self.setStyleSheet(StyleSheetData.themeMap[selectedTheme])
        # 打印当前选择的主题
        print(f"current_theme: {selectedTheme}")
        # 刷新选择框
        if not self.parent.isMultiSelectMode:  
            if not self.parent.pointIsSelected: return
            self.parent.selectLabel.setStyleSheet(StyleSheetData.themeMap[UserData.settingsData['theme']])
        else:
            if not self.parent.selectedLabels: return
            for label in self.parent.selectedLabels:
                label.setStyleSheet(StyleSheetData.themeMap[UserData.settingsData['theme']])
        

    def changeFont(self):
        # 获取当前选择的字体
        selectedFont = self.FontSelect.currentText()
        # 更新 UserData 设置
        UserData.settingsData['font'] = selectedFont
        # 设置字体
        app = QApplication.instance()
        for widget in app.allWidgets():
            widget.setFont(StyleSheetData.fontMap[selectedFont])
        print(f"current_font: {selectedFont}")


    def upDateState(self):
        theme = StyleSheetData.getThemeNameCN(UserData.settingsData['theme'])
        self.ThemeSelect.setCurrentText(theme)
        self.FontSelect.setCurrentText(UserData.settingsData['font'])

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
