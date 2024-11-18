# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PortableBox.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(741, 624)
        MainWindow.setMinimumSize(QSize(741, 624))
        self.BackGroundWidget = QWidget(MainWindow)
        self.BackGroundWidget.setObjectName(u"BackGroundWidget")
        self.BackGroundWidget.setStyleSheet(u"")
        self.TitleWidget = QWidget(self.BackGroundWidget)
        self.TitleWidget.setObjectName(u"TitleWidget")
        self.TitleWidget.setGeometry(QRect(0, 0, 741, 31))
        self.TitleWidget.setStyleSheet(u"")
        self.hboxLayout = QHBoxLayout(self.TitleWidget)
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(15, 0, 15, 0)
        self.Icon = QLabel(self.TitleWidget)
        self.Icon.setObjectName(u"Icon")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon.sizePolicy().hasHeightForWidth())
        self.Icon.setSizePolicy(sizePolicy)
        self.Icon.setMinimumSize(QSize(25, 25))
        self.Icon.setMaximumSize(QSize(25, 25))
        self.Icon.setStyleSheet(u"QLabel{	\n"
"	image:url(:/icon/images/app_icon.png);}")

        self.hboxLayout.addWidget(self.Icon)

        self.Title = QLabel(self.TitleWidget)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"")

        self.hboxLayout.addWidget(self.Title)

        self.TitleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.TitleSpacer)

        self.ButtonMin = QPushButton(self.TitleWidget)
        self.ButtonMin.setObjectName(u"ButtonMin")
        self.ButtonMin.setMinimumSize(QSize(16, 16))
        self.ButtonMin.setMaximumSize(QSize(16, 16))
        self.ButtonMin.setStyleSheet(u"")

        self.hboxLayout.addWidget(self.ButtonMin)

        self.TitleSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.TitleSpacer_2)

        self.ButtonExit = QPushButton(self.TitleWidget)
        self.ButtonExit.setObjectName(u"ButtonExit")
        self.ButtonExit.setMinimumSize(QSize(16, 16))
        self.ButtonExit.setMaximumSize(QSize(16, 16))
        self.ButtonExit.setStyleSheet(u"")

        self.hboxLayout.addWidget(self.ButtonExit)

        self.InfoWidget = QWidget(self.BackGroundWidget)
        self.InfoWidget.setObjectName(u"InfoWidget")
        self.InfoWidget.setGeometry(QRect(0, 393, 741, 231))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.InfoWidget.sizePolicy().hasHeightForWidth())
        self.InfoWidget.setSizePolicy(sizePolicy1)
        self.InfoWidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.InfoWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TargetPath = QLabel(self.InfoWidget)
        self.TargetPath.setObjectName(u"TargetPath")
        self.TargetPath.setMinimumSize(QSize(80, 20))
        self.TargetPath.setMaximumSize(QSize(80, 20))
        self.TargetPath.setStyleSheet(u"")

        self.gridLayout.addWidget(self.TargetPath, 5, 0, 1, 1)

        self.FileSizeLabel = QLabel(self.InfoWidget)
        self.FileSizeLabel.setObjectName(u"FileSizeLabel")
        self.FileSizeLabel.setStyleSheet(u"")
        self.FileSizeLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.FileSizeLabel, 1, 1, 1, 1)

        self.CreateTimeLabel = QLabel(self.InfoWidget)
        self.CreateTimeLabel.setObjectName(u"CreateTimeLabel")
        self.CreateTimeLabel.setStyleSheet(u"")
        self.CreateTimeLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.CreateTimeLabel, 3, 1, 1, 1)

        self.TotalSize = QLabel(self.InfoWidget)
        self.TotalSize.setObjectName(u"TotalSize")
        self.TotalSize.setMinimumSize(QSize(80, 20))
        self.TotalSize.setMaximumSize(QSize(80, 20))
        self.TotalSize.setStyleSheet(u"")

        self.gridLayout.addWidget(self.TotalSize, 6, 0, 1, 1)

        self.LastModifiedTime = QLabel(self.InfoWidget)
        self.LastModifiedTime.setObjectName(u"LastModifiedTime")
        self.LastModifiedTime.setMinimumSize(QSize(80, 20))
        self.LastModifiedTime.setMaximumSize(QSize(80, 20))
        self.LastModifiedTime.setStyleSheet(u"")

        self.gridLayout.addWidget(self.LastModifiedTime, 2, 0, 1, 1)

        self.LastModifiedLabel = QLabel(self.InfoWidget)
        self.LastModifiedLabel.setObjectName(u"LastModifiedLabel")
        self.LastModifiedLabel.setStyleSheet(u"")
        self.LastModifiedLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.LastModifiedLabel, 2, 1, 1, 1)

        self.AddTimeLabel = QLabel(self.InfoWidget)
        self.AddTimeLabel.setObjectName(u"AddTimeLabel")
        self.AddTimeLabel.setStyleSheet(u"")
        self.AddTimeLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.AddTimeLabel, 4, 1, 1, 1)

        self.TargetPathLine = QLineEdit(self.InfoWidget)
        self.TargetPathLine.setObjectName(u"TargetPathLine")
        self.TargetPathLine.setStyleSheet(u"")
        self.TargetPathLine.setReadOnly(True)

        self.gridLayout.addWidget(self.TargetPathLine, 5, 1, 1, 1)

        self.CreateTime = QLabel(self.InfoWidget)
        self.CreateTime.setObjectName(u"CreateTime")
        self.CreateTime.setMinimumSize(QSize(80, 20))
        self.CreateTime.setMaximumSize(QSize(80, 20))
        self.CreateTime.setStyleSheet(u"")

        self.gridLayout.addWidget(self.CreateTime, 3, 0, 1, 1)

        self.AddTime = QLabel(self.InfoWidget)
        self.AddTime.setObjectName(u"AddTime")
        self.AddTime.setMinimumSize(QSize(80, 20))
        self.AddTime.setMaximumSize(QSize(80, 20))
        self.AddTime.setStyleSheet(u"")

        self.gridLayout.addWidget(self.AddTime, 4, 0, 1, 1)

        self.TotalSizeLabel = QLabel(self.InfoWidget)
        self.TotalSizeLabel.setObjectName(u"TotalSizeLabel")
        self.TotalSizeLabel.setStyleSheet(u"")
        self.TotalSizeLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.TotalSizeLabel, 6, 1, 1, 1)

        self.FileName = QLabel(self.InfoWidget)
        self.FileName.setObjectName(u"FileName")
        self.FileName.setMinimumSize(QSize(80, 20))
        self.FileName.setMaximumSize(QSize(80, 20))
        self.FileName.setStyleSheet(u"")

        self.gridLayout.addWidget(self.FileName, 0, 0, 1, 1)

        self.FileSize = QLabel(self.InfoWidget)
        self.FileSize.setObjectName(u"FileSize")
        self.FileSize.setMinimumSize(QSize(80, 20))
        self.FileSize.setMaximumSize(QSize(80, 20))
        self.FileSize.setStyleSheet(u"")

        self.gridLayout.addWidget(self.FileSize, 1, 0, 1, 1)

        self.FileNameLabel = QLabel(self.InfoWidget)
        self.FileNameLabel.setObjectName(u"FileNameLabel")
        self.FileNameLabel.setStyleSheet(u"")
        self.FileNameLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.FileNameLabel, 0, 1, 1, 1)

        self.BtnWidget = QWidget(self.BackGroundWidget)
        self.BtnWidget.setObjectName(u"BtnWidget")
        self.BtnWidget.setGeometry(QRect(0, 31, 741, 41))
        sizePolicy1.setHeightForWidth(self.BtnWidget.sizePolicy().hasHeightForWidth())
        self.BtnWidget.setSizePolicy(sizePolicy1)
        self.BtnWidget.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.BtnWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 741, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, 0, 0, 0)
        self.ButtonAdd = QPushButton(self.layoutWidget)
        self.ButtonAdd.setObjectName(u"ButtonAdd")
        sizePolicy.setHeightForWidth(self.ButtonAdd.sizePolicy().hasHeightForWidth())
        self.ButtonAdd.setSizePolicy(sizePolicy)
        self.ButtonAdd.setMinimumSize(QSize(32, 32))
        self.ButtonAdd.setMaximumSize(QSize(32, 32))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonAdd.setFont(font)
        self.ButtonAdd.setStyleSheet(u"image: url(:/btn/images/add_64px.png);\n"
"")

        self.horizontalLayout_7.addWidget(self.ButtonAdd)

        self.ButtonDel = QPushButton(self.layoutWidget)
        self.ButtonDel.setObjectName(u"ButtonDel")
        sizePolicy.setHeightForWidth(self.ButtonDel.sizePolicy().hasHeightForWidth())
        self.ButtonDel.setSizePolicy(sizePolicy)
        self.ButtonDel.setMinimumSize(QSize(32, 32))
        self.ButtonDel.setMaximumSize(QSize(32, 32))
        self.ButtonDel.setFont(font)
        self.ButtonDel.setStyleSheet(u"image: url(:/btn/images/del_64px.png);")

        self.horizontalLayout_7.addWidget(self.ButtonDel)

        self.ButtonSelectMore = QPushButton(self.layoutWidget)
        self.ButtonSelectMore.setObjectName(u"ButtonSelectMore")
        sizePolicy.setHeightForWidth(self.ButtonSelectMore.sizePolicy().hasHeightForWidth())
        self.ButtonSelectMore.setSizePolicy(sizePolicy)
        self.ButtonSelectMore.setMinimumSize(QSize(32, 32))
        self.ButtonSelectMore.setMaximumSize(QSize(32, 32))
        self.ButtonSelectMore.setFont(font)
        self.ButtonSelectMore.setStyleSheet(u"image: url(:/btn/images/select_more_64px.png);\n"
"")

        self.horizontalLayout_7.addWidget(self.ButtonSelectMore)

        self.ButtonSettings = QPushButton(self.layoutWidget)
        self.ButtonSettings.setObjectName(u"ButtonSettings")
        sizePolicy.setHeightForWidth(self.ButtonSettings.sizePolicy().hasHeightForWidth())
        self.ButtonSettings.setSizePolicy(sizePolicy)
        self.ButtonSettings.setMinimumSize(QSize(32, 32))
        self.ButtonSettings.setMaximumSize(QSize(32, 32))
        self.ButtonSettings.setFont(font)
        self.ButtonSettings.setStyleSheet(u"image: url(:/btn/images/settings_64px.png);\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.ButtonSettings)

        self.BtnSpacer = QSpacerItem(40, 32, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.BtnSpacer)

        self.BackWidget = QWidget(self.BackGroundWidget)
        self.BackWidget.setObjectName(u"BackWidget")
        self.BackWidget.setGeometry(QRect(0, 72, 741, 321))
        self.BackWidget.setStyleSheet(u"")
        self.AppWidget = QWidget(self.BackWidget)
        self.AppWidget.setObjectName(u"AppWidget")
        self.AppWidget.setGeometry(QRect(50, 10, 644, 303))
        sizePolicy1.setHeightForWidth(self.AppWidget.sizePolicy().hasHeightForWidth())
        self.AppWidget.setSizePolicy(sizePolicy1)
        self.AppWidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.AppWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Row_0 = QGridLayout()
        self.Row_0.setObjectName(u"Row_0")
        self.Row_0.setContentsMargins(6, 6, 6, 6)
        self.ColWidget_00 = QWidget(self.AppWidget)
        self.ColWidget_00.setObjectName(u"ColWidget_00")
        self.ColWidget_00.setMinimumSize(QSize(56, 56))
        self.ColWidget_00.setMaximumSize(QSize(56, 56))
        self.Col_00 = QGridLayout(self.ColWidget_00)
        self.Col_00.setObjectName(u"Col_00")
        self.Col_00.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_00, 0, 0, 1, 1)

        self.ColWidget_01 = QWidget(self.AppWidget)
        self.ColWidget_01.setObjectName(u"ColWidget_01")
        self.ColWidget_01.setMinimumSize(QSize(56, 56))
        self.ColWidget_01.setMaximumSize(QSize(56, 56))
        self.Col_01 = QGridLayout(self.ColWidget_01)
        self.Col_01.setObjectName(u"Col_01")
        self.Col_01.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_01, 0, 1, 1, 1)

        self.ColWidget_02 = QWidget(self.AppWidget)
        self.ColWidget_02.setObjectName(u"ColWidget_02")
        self.ColWidget_02.setMinimumSize(QSize(56, 56))
        self.ColWidget_02.setMaximumSize(QSize(56, 56))
        self.Col_02 = QGridLayout(self.ColWidget_02)
        self.Col_02.setObjectName(u"Col_02")
        self.Col_02.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_02, 0, 2, 1, 1)

        self.ColWidget_03 = QWidget(self.AppWidget)
        self.ColWidget_03.setObjectName(u"ColWidget_03")
        self.ColWidget_03.setMinimumSize(QSize(56, 56))
        self.ColWidget_03.setMaximumSize(QSize(56, 56))
        self.Col_03 = QGridLayout(self.ColWidget_03)
        self.Col_03.setObjectName(u"Col_03")
        self.Col_03.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_03, 0, 3, 1, 1)

        self.ColWidget_04 = QWidget(self.AppWidget)
        self.ColWidget_04.setObjectName(u"ColWidget_04")
        self.ColWidget_04.setMinimumSize(QSize(56, 56))
        self.ColWidget_04.setMaximumSize(QSize(56, 56))
        self.Col_04 = QGridLayout(self.ColWidget_04)
        self.Col_04.setObjectName(u"Col_04")
        self.Col_04.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_04, 0, 4, 1, 1)

        self.ColWidget_05 = QWidget(self.AppWidget)
        self.ColWidget_05.setObjectName(u"ColWidget_05")
        self.ColWidget_05.setMinimumSize(QSize(56, 56))
        self.ColWidget_05.setMaximumSize(QSize(56, 56))
        self.Col_05 = QGridLayout(self.ColWidget_05)
        self.Col_05.setObjectName(u"Col_05")
        self.Col_05.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_05, 0, 5, 1, 1)

        self.ColWidget_06 = QWidget(self.AppWidget)
        self.ColWidget_06.setObjectName(u"ColWidget_06")
        self.ColWidget_06.setMinimumSize(QSize(56, 56))
        self.ColWidget_06.setMaximumSize(QSize(56, 56))
        self.Col_06 = QGridLayout(self.ColWidget_06)
        self.Col_06.setObjectName(u"Col_06")
        self.Col_06.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_06, 0, 6, 1, 1)

        self.ColWidget_07 = QWidget(self.AppWidget)
        self.ColWidget_07.setObjectName(u"ColWidget_07")
        self.ColWidget_07.setMinimumSize(QSize(56, 56))
        self.ColWidget_07.setMaximumSize(QSize(56, 56))
        self.Col_07 = QGridLayout(self.ColWidget_07)
        self.Col_07.setObjectName(u"Col_07")
        self.Col_07.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_07, 0, 7, 1, 1)

        self.ColWidget_08 = QWidget(self.AppWidget)
        self.ColWidget_08.setObjectName(u"ColWidget_08")
        self.ColWidget_08.setMinimumSize(QSize(56, 56))
        self.ColWidget_08.setMaximumSize(QSize(56, 56))
        self.Col_08 = QGridLayout(self.ColWidget_08)
        self.Col_08.setObjectName(u"Col_08")
        self.Col_08.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_08, 0, 8, 1, 1)

        self.ColWidget_09 = QWidget(self.AppWidget)
        self.ColWidget_09.setObjectName(u"ColWidget_09")
        self.ColWidget_09.setMinimumSize(QSize(56, 56))
        self.ColWidget_09.setMaximumSize(QSize(56, 56))
        self.Col_09 = QGridLayout(self.ColWidget_09)
        self.Col_09.setObjectName(u"Col_09")
        self.Col_09.setContentsMargins(0, 0, 0, 0)

        self.Row_0.addWidget(self.ColWidget_09, 0, 9, 1, 1)


        self.gridLayout_2.addLayout(self.Row_0, 0, 0, 1, 1)

        self.Row_1 = QGridLayout()
        self.Row_1.setObjectName(u"Row_1")
        self.Row_1.setContentsMargins(6, 6, 6, 6)
        self.ColWidget_10 = QWidget(self.AppWidget)
        self.ColWidget_10.setObjectName(u"ColWidget_10")
        self.ColWidget_10.setMinimumSize(QSize(56, 56))
        self.ColWidget_10.setMaximumSize(QSize(56, 56))
        self.Col_10 = QGridLayout(self.ColWidget_10)
        self.Col_10.setObjectName(u"Col_10")
        self.Col_10.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_10, 0, 0, 1, 1)

        self.ColWidget_11 = QWidget(self.AppWidget)
        self.ColWidget_11.setObjectName(u"ColWidget_11")
        self.ColWidget_11.setMinimumSize(QSize(56, 56))
        self.ColWidget_11.setMaximumSize(QSize(56, 56))
        self.Col_11 = QGridLayout(self.ColWidget_11)
        self.Col_11.setObjectName(u"Col_11")
        self.Col_11.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_11, 0, 1, 1, 1)

        self.ColWidget_12 = QWidget(self.AppWidget)
        self.ColWidget_12.setObjectName(u"ColWidget_12")
        self.ColWidget_12.setMinimumSize(QSize(56, 56))
        self.ColWidget_12.setMaximumSize(QSize(56, 56))
        self.Col_12 = QGridLayout(self.ColWidget_12)
        self.Col_12.setObjectName(u"Col_12")
        self.Col_12.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_12, 0, 2, 1, 1)

        self.ColWidget_13 = QWidget(self.AppWidget)
        self.ColWidget_13.setObjectName(u"ColWidget_13")
        self.ColWidget_13.setMinimumSize(QSize(56, 56))
        self.ColWidget_13.setMaximumSize(QSize(56, 56))
        self.Col_13 = QGridLayout(self.ColWidget_13)
        self.Col_13.setObjectName(u"Col_13")
        self.Col_13.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_13, 0, 3, 1, 1)

        self.ColWidget_14 = QWidget(self.AppWidget)
        self.ColWidget_14.setObjectName(u"ColWidget_14")
        self.ColWidget_14.setMinimumSize(QSize(56, 56))
        self.ColWidget_14.setMaximumSize(QSize(56, 56))
        self.Col_14 = QGridLayout(self.ColWidget_14)
        self.Col_14.setObjectName(u"Col_14")
        self.Col_14.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_14, 0, 4, 1, 1)

        self.ColWidget_15 = QWidget(self.AppWidget)
        self.ColWidget_15.setObjectName(u"ColWidget_15")
        self.ColWidget_15.setMinimumSize(QSize(56, 56))
        self.ColWidget_15.setMaximumSize(QSize(56, 56))
        self.Col_15 = QGridLayout(self.ColWidget_15)
        self.Col_15.setObjectName(u"Col_15")
        self.Col_15.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_15, 0, 5, 1, 1)

        self.ColWidget_16 = QWidget(self.AppWidget)
        self.ColWidget_16.setObjectName(u"ColWidget_16")
        self.ColWidget_16.setMinimumSize(QSize(56, 56))
        self.ColWidget_16.setMaximumSize(QSize(56, 56))
        self.Col_16 = QGridLayout(self.ColWidget_16)
        self.Col_16.setObjectName(u"Col_16")
        self.Col_16.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_16, 0, 6, 1, 1)

        self.ColWidget_17 = QWidget(self.AppWidget)
        self.ColWidget_17.setObjectName(u"ColWidget_17")
        self.ColWidget_17.setMinimumSize(QSize(56, 56))
        self.ColWidget_17.setMaximumSize(QSize(56, 56))
        self.Col_17 = QGridLayout(self.ColWidget_17)
        self.Col_17.setObjectName(u"Col_17")
        self.Col_17.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_17, 0, 7, 1, 1)

        self.ColWidget_18 = QWidget(self.AppWidget)
        self.ColWidget_18.setObjectName(u"ColWidget_18")
        self.ColWidget_18.setMinimumSize(QSize(56, 56))
        self.ColWidget_18.setMaximumSize(QSize(56, 56))
        self.Col_18 = QGridLayout(self.ColWidget_18)
        self.Col_18.setObjectName(u"Col_18")
        self.Col_18.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_18, 0, 8, 1, 1)

        self.ColWidget_19 = QWidget(self.AppWidget)
        self.ColWidget_19.setObjectName(u"ColWidget_19")
        self.ColWidget_19.setMinimumSize(QSize(56, 56))
        self.ColWidget_19.setMaximumSize(QSize(56, 56))
        self.Col_19 = QGridLayout(self.ColWidget_19)
        self.Col_19.setObjectName(u"Col_19")
        self.Col_19.setContentsMargins(0, 0, 0, 0)

        self.Row_1.addWidget(self.ColWidget_19, 0, 9, 1, 1)


        self.gridLayout_2.addLayout(self.Row_1, 1, 0, 1, 1)

        self.Row_2 = QGridLayout()
        self.Row_2.setObjectName(u"Row_2")
        self.Row_2.setContentsMargins(6, 6, 6, 6)
        self.ColWidget_20 = QWidget(self.AppWidget)
        self.ColWidget_20.setObjectName(u"ColWidget_20")
        self.ColWidget_20.setMinimumSize(QSize(56, 56))
        self.ColWidget_20.setMaximumSize(QSize(56, 56))
        self.Col_20 = QGridLayout(self.ColWidget_20)
        self.Col_20.setObjectName(u"Col_20")
        self.Col_20.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_20, 0, 0, 1, 1)

        self.ColWidget_21 = QWidget(self.AppWidget)
        self.ColWidget_21.setObjectName(u"ColWidget_21")
        self.ColWidget_21.setMinimumSize(QSize(56, 56))
        self.ColWidget_21.setMaximumSize(QSize(56, 56))
        self.Col_21 = QGridLayout(self.ColWidget_21)
        self.Col_21.setObjectName(u"Col_21")
        self.Col_21.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_21, 0, 1, 1, 1)

        self.ColWidget_22 = QWidget(self.AppWidget)
        self.ColWidget_22.setObjectName(u"ColWidget_22")
        self.ColWidget_22.setMinimumSize(QSize(56, 56))
        self.ColWidget_22.setMaximumSize(QSize(56, 56))
        self.Col_22 = QGridLayout(self.ColWidget_22)
        self.Col_22.setObjectName(u"Col_22")
        self.Col_22.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_22, 0, 2, 1, 1)

        self.ColWidget_23 = QWidget(self.AppWidget)
        self.ColWidget_23.setObjectName(u"ColWidget_23")
        self.ColWidget_23.setMinimumSize(QSize(56, 56))
        self.ColWidget_23.setMaximumSize(QSize(56, 56))
        self.Col_23 = QGridLayout(self.ColWidget_23)
        self.Col_23.setObjectName(u"Col_23")
        self.Col_23.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_23, 0, 3, 1, 1)

        self.ColWidget_24 = QWidget(self.AppWidget)
        self.ColWidget_24.setObjectName(u"ColWidget_24")
        self.ColWidget_24.setMinimumSize(QSize(56, 56))
        self.ColWidget_24.setMaximumSize(QSize(56, 56))
        self.Col_24 = QGridLayout(self.ColWidget_24)
        self.Col_24.setObjectName(u"Col_24")
        self.Col_24.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_24, 0, 4, 1, 1)

        self.ColWidget_25 = QWidget(self.AppWidget)
        self.ColWidget_25.setObjectName(u"ColWidget_25")
        self.ColWidget_25.setMinimumSize(QSize(56, 56))
        self.ColWidget_25.setMaximumSize(QSize(56, 56))
        self.Col_25 = QGridLayout(self.ColWidget_25)
        self.Col_25.setObjectName(u"Col_25")
        self.Col_25.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_25, 0, 5, 1, 1)

        self.ColWidget_26 = QWidget(self.AppWidget)
        self.ColWidget_26.setObjectName(u"ColWidget_26")
        self.ColWidget_26.setMinimumSize(QSize(56, 56))
        self.ColWidget_26.setMaximumSize(QSize(56, 56))
        self.Col_26 = QGridLayout(self.ColWidget_26)
        self.Col_26.setObjectName(u"Col_26")
        self.Col_26.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_26, 0, 6, 1, 1)

        self.ColWidget_27 = QWidget(self.AppWidget)
        self.ColWidget_27.setObjectName(u"ColWidget_27")
        self.ColWidget_27.setMinimumSize(QSize(56, 56))
        self.ColWidget_27.setMaximumSize(QSize(56, 56))
        self.Col_27 = QGridLayout(self.ColWidget_27)
        self.Col_27.setObjectName(u"Col_27")
        self.Col_27.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_27, 0, 7, 1, 1)

        self.ColWidget_28 = QWidget(self.AppWidget)
        self.ColWidget_28.setObjectName(u"ColWidget_28")
        self.ColWidget_28.setMinimumSize(QSize(56, 56))
        self.ColWidget_28.setMaximumSize(QSize(56, 56))
        self.Col_28 = QGridLayout(self.ColWidget_28)
        self.Col_28.setObjectName(u"Col_28")
        self.Col_28.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_28, 0, 8, 1, 1)

        self.ColWidget_29 = QWidget(self.AppWidget)
        self.ColWidget_29.setObjectName(u"ColWidget_29")
        self.ColWidget_29.setMinimumSize(QSize(56, 56))
        self.ColWidget_29.setMaximumSize(QSize(56, 56))
        self.Col_29 = QGridLayout(self.ColWidget_29)
        self.Col_29.setObjectName(u"Col_29")
        self.Col_29.setContentsMargins(0, 0, 0, 0)

        self.Row_2.addWidget(self.ColWidget_29, 0, 9, 1, 1)


        self.gridLayout_2.addLayout(self.Row_2, 2, 0, 1, 1)

        self.Row_3 = QGridLayout()
        self.Row_3.setObjectName(u"Row_3")
        self.Row_3.setContentsMargins(6, 6, 6, -1)
        self.ColWidget_30 = QWidget(self.AppWidget)
        self.ColWidget_30.setObjectName(u"ColWidget_30")
        self.ColWidget_30.setMinimumSize(QSize(56, 56))
        self.ColWidget_30.setMaximumSize(QSize(56, 56))
        self.Col_30 = QGridLayout(self.ColWidget_30)
        self.Col_30.setObjectName(u"Col_30")
        self.Col_30.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_30, 0, 0, 1, 1)

        self.ColWidget_31 = QWidget(self.AppWidget)
        self.ColWidget_31.setObjectName(u"ColWidget_31")
        self.ColWidget_31.setMinimumSize(QSize(56, 56))
        self.ColWidget_31.setMaximumSize(QSize(56, 56))
        self.Col_31 = QGridLayout(self.ColWidget_31)
        self.Col_31.setObjectName(u"Col_31")
        self.Col_31.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_31, 0, 1, 1, 1)

        self.ColWidget_32 = QWidget(self.AppWidget)
        self.ColWidget_32.setObjectName(u"ColWidget_32")
        self.ColWidget_32.setMinimumSize(QSize(56, 56))
        self.ColWidget_32.setMaximumSize(QSize(56, 56))
        self.Col_32 = QGridLayout(self.ColWidget_32)
        self.Col_32.setObjectName(u"Col_32")
        self.Col_32.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_32, 0, 2, 1, 1)

        self.ColWidget_33 = QWidget(self.AppWidget)
        self.ColWidget_33.setObjectName(u"ColWidget_33")
        self.ColWidget_33.setMinimumSize(QSize(56, 56))
        self.ColWidget_33.setMaximumSize(QSize(56, 56))
        self.Col_33 = QGridLayout(self.ColWidget_33)
        self.Col_33.setObjectName(u"Col_33")
        self.Col_33.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_33, 0, 3, 1, 1)

        self.ColWidget_34 = QWidget(self.AppWidget)
        self.ColWidget_34.setObjectName(u"ColWidget_34")
        self.ColWidget_34.setMinimumSize(QSize(56, 56))
        self.ColWidget_34.setMaximumSize(QSize(56, 56))
        self.Col_34 = QGridLayout(self.ColWidget_34)
        self.Col_34.setObjectName(u"Col_34")
        self.Col_34.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_34, 0, 4, 1, 1)

        self.ColWidget_35 = QWidget(self.AppWidget)
        self.ColWidget_35.setObjectName(u"ColWidget_35")
        self.ColWidget_35.setMinimumSize(QSize(56, 56))
        self.ColWidget_35.setMaximumSize(QSize(56, 56))
        self.Col_35 = QGridLayout(self.ColWidget_35)
        self.Col_35.setObjectName(u"Col_35")
        self.Col_35.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_35, 0, 5, 1, 1)

        self.ColWidget_36 = QWidget(self.AppWidget)
        self.ColWidget_36.setObjectName(u"ColWidget_36")
        self.ColWidget_36.setMinimumSize(QSize(56, 56))
        self.ColWidget_36.setMaximumSize(QSize(56, 56))
        self.Col_36 = QGridLayout(self.ColWidget_36)
        self.Col_36.setObjectName(u"Col_36")
        self.Col_36.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_36, 0, 6, 1, 1)

        self.ColWidget_37 = QWidget(self.AppWidget)
        self.ColWidget_37.setObjectName(u"ColWidget_37")
        self.ColWidget_37.setMinimumSize(QSize(56, 56))
        self.ColWidget_37.setMaximumSize(QSize(56, 56))
        self.Col_37 = QGridLayout(self.ColWidget_37)
        self.Col_37.setObjectName(u"Col_37")
        self.Col_37.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_37, 0, 7, 1, 1)

        self.ColWidget_38 = QWidget(self.AppWidget)
        self.ColWidget_38.setObjectName(u"ColWidget_38")
        self.ColWidget_38.setMinimumSize(QSize(56, 56))
        self.ColWidget_38.setMaximumSize(QSize(56, 56))
        self.Col_38 = QGridLayout(self.ColWidget_38)
        self.Col_38.setObjectName(u"Col_38")
        self.Col_38.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_38, 0, 8, 1, 1)

        self.ColWidget_39 = QWidget(self.AppWidget)
        self.ColWidget_39.setObjectName(u"ColWidget_39")
        self.ColWidget_39.setMinimumSize(QSize(56, 56))
        self.ColWidget_39.setMaximumSize(QSize(56, 56))
        self.Col_39 = QGridLayout(self.ColWidget_39)
        self.Col_39.setObjectName(u"Col_39")
        self.Col_39.setContentsMargins(0, 0, 0, 0)

        self.Row_3.addWidget(self.ColWidget_39, 0, 9, 1, 1)


        self.gridLayout_2.addLayout(self.Row_3, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.BackGroundWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.Icon.setText("")
        self.Title.setText(QCoreApplication.translate("MainWindow", u"PortableBox", None))
        self.ButtonMin.setText("")
        self.ButtonExit.setText("")
        self.TargetPath.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u4f4d\u7f6e\uff1a", None))
        self.FileSizeLabel.setText("")
        self.CreateTimeLabel.setText("")
        self.TotalSize.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u603b\u5927\u5c0f\uff1a", None))
        self.LastModifiedTime.setText(QCoreApplication.translate("MainWindow", u"\u6700\u540e\u4fee\u6539\u65f6\u95f4\uff1a", None))
        self.LastModifiedLabel.setText("")
        self.AddTimeLabel.setText("")
        self.TargetPathLine.setText("")
        self.CreateTime.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u65f6\u95f4\uff1a", None))
        self.AddTime.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u65f6\u95f4\uff1a", None))
        self.TotalSizeLabel.setText("")
        self.FileName.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u540d\u79f0\uff1a", None))
        self.FileSize.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5927\u5c0f\uff1a", None))
        self.FileNameLabel.setText("")
        pass
    # retranslateUi

