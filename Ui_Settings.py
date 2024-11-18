# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(511, 422)
        self.TitleWidget = QWidget(Form)
        self.TitleWidget.setObjectName(u"TitleWidget")
        self.TitleWidget.setGeometry(QRect(0, 0, 511, 31))
        self.TitleWidget.setStyleSheet(u"")
        self.hboxLayout = QHBoxLayout(self.TitleWidget)
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(15, 0, 15, 0)
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

        self.BackBoard = QWidget(Form)
        self.BackBoard.setObjectName(u"BackBoard")
        self.BackBoard.setGeometry(QRect(0, 30, 511, 391))
        self.BackBoard.setStyleSheet(u"")
        self.TabWidget = QTabWidget(self.BackBoard)
        self.TabWidget.setObjectName(u"TabWidget")
        self.TabWidget.setGeometry(QRect(0, 0, 511, 391))
        self.TabWidget.setStyleSheet(u"")
        self.Theme = QWidget()
        self.Theme.setObjectName(u"Theme")
        self.Theme.setStyleSheet(u"")
        self.ThemeSelects = QComboBox(self.Theme)
        self.ThemeSelects.setObjectName(u"ThemeSelects")
        self.ThemeSelects.setGeometry(QRect(10, 10, 181, 22))
        self.ThemeSelects.setStyleSheet(u"")
        self.TabWidget.addTab(self.Theme, "")
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.About.setStyleSheet(u"")
        self.AboutContent = QTextBrowser(self.About)
        self.AboutContent.setObjectName(u"AboutContent")
        self.AboutContent.setGeometry(QRect(0, 0, 511, 311))
        self.AboutContent.setStyleSheet(u"")
        self.ButtonBlog = QPushButton(self.About)
        self.ButtonBlog.setObjectName(u"ButtonBlog")
        self.ButtonBlog.setGeometry(QRect(160, 320, 191, 38))
        self.ButtonBlog.setMaximumSize(QSize(16777215, 38))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonBlog.setFont(font)
        self.ButtonBlog.setStyleSheet(u"")
        self.TabWidget.addTab(self.About, "")

        self.retranslateUi(Form)

        self.TabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.ButtonMin.setText("")
        self.ButtonExit.setText("")
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Theme), QCoreApplication.translate("Form", u"\u4e3b\u9898", None))
        self.AboutContent.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:10pt; font-weight:700; color:#565656;\">\u5173\u4e8e\u4f5c\u8005</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; color:#565656;\">\u5f00\u53d1\u8005\uff1a"
                        "ichinoseyuu </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; color:#565656;\">\u8054\u7cfb\u65b9\u5f0f\uff1a1915914448@qq.com</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:10pt; font-weight:700; color:#565656;\">\u5173\u4e8e\u8f6f\u4ef6</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; color:#565656;\">\u8f6f\u4ef6\u540d\u79f0\uff1aPortableBox</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'"
                        "\u5fae\u8f6f\u96c5\u9ed1'; color:#565656;\">\u7248\u672c\uff1av1.0b</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; color:#565656;\">\u7248\u6743\u4fe1\u606f\uff1a\u7248\u6743\u6240\u6709 \u00a9 2024 ichinoseyuu \u4fdd\u7559\u6240\u6709\u6743\u5229</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; color:#565656;\">\u4f7f\u7528\u6761\u6b3e\uff1a\u672c\u7a0b\u5e8f\u4ec5\u7528\u4e8e\u5b66\u4e60\u548c\u4e2a\u4eba\u7528\u9014\uff0c\u4e0d\u5f97\u7528\u4e8e\u5546\u4e1a\u76ee\u7684.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; color:#565656"
                        ";\">\u9690\u79c1\u653f\u7b56\uff1a\u672c\u7a0b\u5e8f\u4e0d\u4f1a\u6536\u96c6\u4efb\u4f55\u7528\u6237\u6570\u636e</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; color:#565656;\">\u514d\u8d23\u58f0\u660e\uff1a\u5bf9\u4e8e\u56e0\u4f7f\u7528\u672c\u7a0b\u5e8f\u9020\u6210\u7684\u4efb\u4f55\u635f\u5931\uff0c\u4f5c\u8005\u6982\u4e0d\u8d1f\u8d23.</span></p></body></html>", None))
        self.ButtonBlog.setText(QCoreApplication.translate("Form", u"\u53bb\u8e29\u4e00\u8e29\u6211\u7684\u4e3b\u9875  (\uff61\u2022\u0300\u1d17-)\u2727", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.About), QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
    # retranslateUi

