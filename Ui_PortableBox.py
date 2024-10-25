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
        MainWindow.resize(1024, 720)
        MainWindow.setMinimumSize(QSize(1024, 720))
        self.BackGroundWidget = QWidget(MainWindow)
        self.BackGroundWidget.setObjectName(u"BackGroundWidget")
        self.BackGroundWidget.setStyleSheet(u"QWidget{background-color: rgba(255, 254, 244, 250);}\n"
"")
        self.TitleWidget = QWidget(self.BackGroundWidget)
        self.TitleWidget.setObjectName(u"TitleWidget")
        self.TitleWidget.setGeometry(QRect(0, 0, 1024, 40))
        self.TitleWidget.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"background-color: rgb(202, 116, 151);\n"
"")
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
        self.Icon.setMinimumSize(QSize(32, 32))
        self.Icon.setMaximumSize(QSize(32, 32))
        self.Icon.setStyleSheet(u"QLabel{	\n"
"	image:url(:/icon/images/app_icon.png);}")

        self.hboxLayout.addWidget(self.Icon)

        self.Title = QLabel(self.TitleWidget)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"QLabel{\n"
"    color: rgb(241, 241, 184);\n"
"	background-color: rgba(200 ,200, 200,0);\n"
"	qproperty-alignment: AlignCenter;\n"
"}")

        self.hboxLayout.addWidget(self.Title)

        self.TitleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.TitleSpacer)

        self.ButtonMin = QPushButton(self.TitleWidget)
        self.ButtonMin.setObjectName(u"ButtonMin")
        self.ButtonMin.setMinimumSize(QSize(16, 16))
        self.ButtonMin.setMaximumSize(QSize(16, 16))
        self.ButtonMin.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"    border-radius: 8px;\n"
"	background-color: rgb(255, 190, 0);}\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 170, 255);}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 170, 255);}")

        self.hboxLayout.addWidget(self.ButtonMin)

        self.TitleSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.TitleSpacer_2)

        self.ButtonExit = QPushButton(self.TitleWidget)
        self.ButtonExit.setObjectName(u"ButtonExit")
        self.ButtonExit.setMinimumSize(QSize(16, 16))
        self.ButtonExit.setMaximumSize(QSize(16, 16))
        self.ButtonExit.setStyleSheet(u"QPushButton {\n"
"	border: 0px;\n"
"    border-radius: 8px;\n"
"	background-color: rgb(255, 60, 0);}\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 170, 255);}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 170, 255);}")

        self.hboxLayout.addWidget(self.ButtonExit)

        self.InfoWidget = QWidget(self.BackGroundWidget)
        self.InfoWidget.setObjectName(u"InfoWidget")
        self.InfoWidget.setGeometry(QRect(0, 470, 741, 251))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.InfoWidget.sizePolicy().hasHeightForWidth())
        self.InfoWidget.setSizePolicy(sizePolicy1)
        self.InfoWidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(234, 214, 229);}")
        self.gridLayout = QGridLayout(self.InfoWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TargetPath = QLabel(self.InfoWidget)
        self.TargetPath.setObjectName(u"TargetPath")
        self.TargetPath.setMinimumSize(QSize(80, 20))
        self.TargetPath.setMaximumSize(QSize(80, 20))
        self.TargetPath.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")

        self.gridLayout.addWidget(self.TargetPath, 5, 0, 1, 1)

        self.FileSizeLabel = QLabel(self.InfoWidget)
        self.FileSizeLabel.setObjectName(u"FileSizeLabel")
        self.FileSizeLabel.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")
        self.FileSizeLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.FileSizeLabel, 1, 1, 1, 1)

        self.CreateTimeLabel = QLabel(self.InfoWidget)
        self.CreateTimeLabel.setObjectName(u"CreateTimeLabel")
        self.CreateTimeLabel.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")
        self.CreateTimeLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.CreateTimeLabel, 3, 1, 1, 1)

        self.TotalSize = QLabel(self.InfoWidget)
        self.TotalSize.setObjectName(u"TotalSize")
        self.TotalSize.setMinimumSize(QSize(80, 20))
        self.TotalSize.setMaximumSize(QSize(80, 20))
        self.TotalSize.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")

        self.gridLayout.addWidget(self.TotalSize, 6, 0, 1, 1)

        self.LastModifiedTime = QLabel(self.InfoWidget)
        self.LastModifiedTime.setObjectName(u"LastModifiedTime")
        self.LastModifiedTime.setMinimumSize(QSize(80, 20))
        self.LastModifiedTime.setMaximumSize(QSize(80, 20))
        self.LastModifiedTime.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")

        self.gridLayout.addWidget(self.LastModifiedTime, 2, 0, 1, 1)

        self.LastModifiedLabel = QLabel(self.InfoWidget)
        self.LastModifiedLabel.setObjectName(u"LastModifiedLabel")
        self.LastModifiedLabel.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")
        self.LastModifiedLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.LastModifiedLabel, 2, 1, 1, 1)

        self.AddTimeLabel = QLabel(self.InfoWidget)
        self.AddTimeLabel.setObjectName(u"AddTimeLabel")
        self.AddTimeLabel.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")
        self.AddTimeLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.AddTimeLabel, 4, 1, 1, 1)

        self.TargetPathLine = QLineEdit(self.InfoWidget)
        self.TargetPathLine.setObjectName(u"TargetPathLine")
        self.TargetPathLine.setStyleSheet(u"QLineEdit{border:none;color: rgb(170, 91, 113);}")
        self.TargetPathLine.setReadOnly(True)

        self.gridLayout.addWidget(self.TargetPathLine, 5, 1, 1, 1)

        self.CreateTime = QLabel(self.InfoWidget)
        self.CreateTime.setObjectName(u"CreateTime")
        self.CreateTime.setMinimumSize(QSize(80, 20))
        self.CreateTime.setMaximumSize(QSize(80, 20))
        self.CreateTime.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")

        self.gridLayout.addWidget(self.CreateTime, 3, 0, 1, 1)

        self.AddTime = QLabel(self.InfoWidget)
        self.AddTime.setObjectName(u"AddTime")
        self.AddTime.setMinimumSize(QSize(80, 20))
        self.AddTime.setMaximumSize(QSize(80, 20))
        self.AddTime.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")

        self.gridLayout.addWidget(self.AddTime, 4, 0, 1, 1)

        self.TotalSizeLabel = QLabel(self.InfoWidget)
        self.TotalSizeLabel.setObjectName(u"TotalSizeLabel")
        self.TotalSizeLabel.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")
        self.TotalSizeLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.TotalSizeLabel, 6, 1, 1, 1)

        self.FileName = QLabel(self.InfoWidget)
        self.FileName.setObjectName(u"FileName")
        self.FileName.setMinimumSize(QSize(80, 20))
        self.FileName.setMaximumSize(QSize(80, 20))
        self.FileName.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")

        self.gridLayout.addWidget(self.FileName, 0, 0, 1, 1)

        self.FileSize = QLabel(self.InfoWidget)
        self.FileSize.setObjectName(u"FileSize")
        self.FileSize.setMinimumSize(QSize(80, 20))
        self.FileSize.setMaximumSize(QSize(80, 20))
        self.FileSize.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")

        self.gridLayout.addWidget(self.FileSize, 1, 0, 1, 1)

        self.FileNameLabel = QLabel(self.InfoWidget)
        self.FileNameLabel.setObjectName(u"FileNameLabel")
        self.FileNameLabel.setStyleSheet(u"QLabel{color: rgb(170, 91, 113);}")
        self.FileNameLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.FileNameLabel, 0, 1, 1, 1)

        self.BtnWidget = QWidget(self.BackGroundWidget)
        self.BtnWidget.setObjectName(u"BtnWidget")
        self.BtnWidget.setGeometry(QRect(741, 40, 283, 681))
        sizePolicy1.setHeightForWidth(self.BtnWidget.sizePolicy().hasHeightForWidth())
        self.BtnWidget.setSizePolicy(sizePolicy1)
        self.BtnWidget.setMinimumSize(QSize(283, 681))
        self.BtnWidget.setMaximumSize(QSize(283, 681))
        self.BtnWidget.setStyleSheet(u"QWidget{background-color: rgb(207, 209, 225);}")
        self.BtnWidget_2 = QWidget(self.BackGroundWidget)
        self.BtnWidget_2.setObjectName(u"BtnWidget_2")
        self.BtnWidget_2.setGeometry(QRect(0, 40, 741, 41))
        sizePolicy1.setHeightForWidth(self.BtnWidget_2.sizePolicy().hasHeightForWidth())
        self.BtnWidget_2.setSizePolicy(sizePolicy1)
        self.BtnWidget_2.setStyleSheet(u"QWidget{background-color: #f2debd;}")
        self.widget = QWidget(self.BtnWidget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 741, 41))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 0, 0, 0)
        self.ButtonAdd = QPushButton(self.widget)
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
        self.ButtonAdd.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"	image: url(:/btn/images/add_64px.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"	stop: 0 rgba(236, 210, 226, 255), stop: 1 rgb(220, 223, 243)); \n"
"	color: #555;\n"
"	border: 1px solid rgb(212, 208, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"		stop: 0 rgba(212, 212, 236, 255), stop: 1 rgba(226, 207, 216, 255));\n"
"	border: 1px solid rgb(212, 208, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.ButtonAdd)

        self.ButtonDel = QPushButton(self.widget)
        self.ButtonDel.setObjectName(u"ButtonDel")
        sizePolicy.setHeightForWidth(self.ButtonDel.sizePolicy().hasHeightForWidth())
        self.ButtonDel.setSizePolicy(sizePolicy)
        self.ButtonDel.setMinimumSize(QSize(32, 32))
        self.ButtonDel.setMaximumSize(QSize(32, 32))
        self.ButtonDel.setFont(font)
        self.ButtonDel.setStyleSheet(u"QPushButton {\n"
"	image: url(:/btn/images/del_64px.png);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"	stop: 0 rgba(236, 210, 226, 255), stop: 1 rgb(220, 223, 243)); \n"
"	color: #555;\n"
"	border: 1px solid rgb(212, 208, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"		stop: 0 rgba(212, 212, 236, 255), stop: 1 rgba(226, 207, 216, 255));\n"
"	border: 1px solid rgb(212, 208, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.ButtonDel)

        self.horizontalSpacer_7 = QSpacerItem(40, 32, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.AppWidget = QWidget(self.BackGroundWidget)
        self.AppWidget.setObjectName(u"AppWidget")
        self.AppWidget.setGeometry(QRect(0, 80, 741, 391))
        self.AppWidget.setStyleSheet(u"QWidget{background-color: rgba(241, 239, 212, 240)}")
        self.widget1 = QWidget(self.AppWidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 741, 71))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")

        self.horizontalLayout_2.addLayout(self.gridLayout_12)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")

        self.horizontalLayout_2.addLayout(self.gridLayout_11)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.horizontalLayout_2.addLayout(self.gridLayout_9)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.horizontalLayout_2.addLayout(self.gridLayout_8)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")

        self.horizontalLayout_2.addLayout(self.gridLayout_7)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.horizontalLayout_2.addLayout(self.gridLayout_6)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.horizontalLayout_2.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.horizontalLayout_2.addLayout(self.gridLayout_4)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.horizontalLayout_2.addLayout(self.gridLayout_10)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.horizontalLayout_2.addLayout(self.gridLayout_5)

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
        self.ButtonAdd.setText("")
        pass
    # retranslateUi
