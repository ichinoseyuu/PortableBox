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
        self.TitleWidget.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"background-color: rgb(202, 116, 151);\n"
"")
        self.hboxLayout = QHBoxLayout(self.TitleWidget)
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(15, 0, 15, 0)
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

        self.Backboard = QWidget(Form)
        self.Backboard.setObjectName(u"Backboard")
        self.Backboard.setGeometry(QRect(0, 30, 511, 391))
        self.Backboard.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"background-color: rgba(241, 239, 212, 240)")
        self.TabWidget = QTabWidget(self.Backboard)
        self.TabWidget.setObjectName(u"TabWidget")
        self.TabWidget.setGeometry(QRect(0, 0, 511, 391))
        self.TabWidget.setStyleSheet(u"QTabWidget {\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;  /* \u53bb\u9664\u9762\u677f\u7684\u8fb9\u6846 */\n"
"}\n"
"\n"
"QTabBar {\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #f5f5f5;  /* \u9009\u9879\u5361\u80cc\u666f */\n"
"    color: #333;  /* \u6587\u5b57\u989c\u8272 */\n"
"    border: 1px solid #dcdcdc;  /* \u9009\u9879\u5361\u7684\u8fb9\u6846 */\n"
"    padding: 5px 10px;  /* \u5185\u8fb9\u8ddd */\n"
"    margin-right: 0px;  /* \u9009\u9879\u5361\u4e4b\u95f4\u7684\u95f4\u8ddd */\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #ffffff;  /* \u9009\u4e2d\u7684\u9009\u9879\u5361\u80cc\u666f */\n"
"    color: #000000;  /* \u9009\u4e2d\u65f6\u7684\u6587\u5b57\u989c\u8272 */\n"
"    border-color: #0078d4;  /* \u9009\u4e2d\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #e0e0e0;  /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f */\n"
"}\n"
"\n"
""
                        "QTabBar::tab:!selected {\n"
"    background-color: #f5f5f5;  /* \u975e\u9009\u4e2d\u65f6\u7684\u80cc\u666f */\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"    image: url(data:image/svg+xml;base64,...);  /* \u8bbe\u7f6e\u5173\u95ed\u6309\u94ae\u7684\u56fe\u6807 */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    background-color: #ff0000;  /* \u9f20\u6807\u60ac\u505c\u65f6\u5173\u95ed\u6309\u94ae\u80cc\u666f */\n"
"}\n"
"")
        self.Theme = QWidget()
        self.Theme.setObjectName(u"Theme")
        self.ThemeSelects = QComboBox(self.Theme)
        self.ThemeSelects.setObjectName(u"ThemeSelects")
        self.ThemeSelects.setGeometry(QRect(10, 10, 211, 22))
        self.ButtonSave = QPushButton(self.Theme)
        self.ButtonSave.setObjectName(u"ButtonSave")
        self.ButtonSave.setGeometry(QRect(430, 320, 71, 38))
        self.ButtonSave.setMaximumSize(QSize(16777215, 38))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.ButtonSave.setFont(font)
        self.ButtonSave.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(241, 204, 184);\n"
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
        self.TabWidget.addTab(self.Theme, "")
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.textBrowser = QTextBrowser(self.About)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 511, 311))
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border:none;\n"
"    padding: 5px;\n"
"}\n"
"QTextBrowser::verticalScrollBar {\n"
"    width: 10px;\n"
"    background-color: #ddd;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"QTextBrowser::verticalScrollBar::handle {\n"
"    background-color: #999;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"QTextBrowser::verticalScrollBar, \n"
"QTextBrowser::horizontalScrollBar {\n"
"	width: 0px;\n"
"	height: 0px;\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.ButtonBlog = QPushButton(self.About)
        self.ButtonBlog.setObjectName(u"ButtonBlog")
        self.ButtonBlog.setGeometry(QRect(160, 320, 191, 38))
        self.ButtonBlog.setMaximumSize(QSize(16777215, 38))
        self.ButtonBlog.setFont(font)
        self.ButtonBlog.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(241, 204, 184);\n"
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
        self.TabWidget.addTab(self.About, "")

        self.retranslateUi(Form)

        self.TabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.ButtonMin.setText("")
        self.ButtonExit.setText("")
        self.ButtonSave.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Theme), QCoreApplication.translate("Form", u"\u4e3b\u9898", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#2d2d2d;\">\u5173\u4e8e\u4f5c\u8005</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#2d2d2d;\">\u5f00\u53d1\u8005\uff1aichinoseyuu </span></p>\n"
"<p align=\"center\" style=\" margin-top:12"
                        "px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#2d2d2d;\">\u8054\u7cfb\u65b9\u5f0f\uff1a1915914448@qq.com</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#2d2d2d;\">\u5173\u4e8e\u8f6f\u4ef6</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#2d2d2d;\">\u8f6f\u4ef6\u540d\u79f0\uff1aPortableBox</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#2d2d2d;\">\u7248\u672c\uff1av1.0b</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" font-size:9pt; color:#2d2d2d;\">\u7248\u6743\u4fe1\u606f\uff1a\u7248\u6743\u6240\u6709 \u00a9 2024 ichinoseyuu \u4fdd\u7559\u6240\u6709\u6743\u5229</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#2d2d2d;\">\u4f7f\u7528\u6761\u6b3e\uff1a\u672c\u7a0b\u5e8f\u4ec5\u7528\u4e8e\u5b66\u4e60\u548c\u4e2a\u4eba\u7528\u9014\uff0c\u4e0d\u5f97\u7528\u4e8e\u5546\u4e1a\u76ee\u7684.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#2d2d2d;\">\u9690\u79c1\u653f\u7b56\uff1a\u672c\u7a0b\u5e8f\u4e0d\u4f1a\u6536\u96c6\u4efb\u4f55\u7528\u6237\u6570\u636e</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span st"
                        "yle=\" font-size:9pt; color:#2d2d2d;\">\u514d\u8d23\u58f0\u660e\uff1a\u5bf9\u4e8e\u56e0\u4f7f\u7528\u672c\u7a0b\u5e8f\u9020\u6210\u7684\u4efb\u4f55\u635f\u5931\uff0c\u4f5c\u8005\u6982\u4e0d\u8d1f\u8d23.</span></p></body></html>", None))
        self.ButtonBlog.setText(QCoreApplication.translate("Form", u"\u53bb\u8e29\u4e00\u8e29\u6211\u7684\u4e3b\u9875  (\uff61\u2022\u0300\u1d17-)\u2727", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.About), QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
    # retranslateUi

