# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1245, 862)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(-10, -10, 1241, 871))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("/* 设置QTableWidget的整体样式 */\n"
"QTableWidget {\n"
"    border: 2px solid #4796f0;  /* 边框颜色 */\n"
"    border-radius: 10px;        /* 圆角 */\n"
"    background-color: #f0f0f0;  /* 背景颜色 */\n"
"    gridline-color: #c0c0c0;    /* 表格线颜色 */\n"
"}\n"
"\n"
"/* 设置表头样式 */\n"
"QHeaderView::section {\n"
"    background-color: #4796f0;  /* 表头背景颜色 */\n"
"    color: white;               /* 表头文字颜色 */\n"
"    padding: 5px;               /* 内边距 */\n"
"    border: 1px solid #c0c0c0;  /* 表头边框 */\n"
"}\n"
"\n"
"/* 设置单元格的样式 */\n"
"QTableWidget::item {\n"
"    border: 1px solid #c0c0c0;  /* 单元格边框颜色 */\n"
"    padding: 5px;               /* 单元格内边距 */\n"
"}\n"
"\n"
"/* 设置选中单元格的样式 */\n"
"QTableWidget::item:selected {\n"
"    background-color: #4796f0;  /* 选中的单元格背景颜色 */\n"
"    color: white;               /* 选中的单元格文字颜色 */\n"
"}\n"
"\n"
"/* 设置TabWidget的样式 */\n"
"QTabWidget::pane {\n"
"    border: 2px solid #4796f0;  /* Tab外框颜色 */\n"
"    background: #e0e0e0;        /* 背景颜色 */\n"
"    padding: 10px;              /* 内边距，增加Tab之间的间距 */\n"
"    border-radius: 10px;        /* 圆角 */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #d0d0d0); /* 渐变背景 */\n"
"    border: 1px solid #a0a0a0;  /* 边框颜色 */\n"
"    padding: 10px;              /* 内边距，控制tab的大小 */\n"
"    margin-right: 5px;          /* Tab之间的间距 */\n"
"    border-radius: 5px;         /* 圆角 */\n"
"    color: #333;                /* 文字颜色 */\n"
"}\n"
"\n"
"/* 设置鼠标悬停时的Tab样式 */\n"
"QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #d0d0d0, stop: 1 #a0a0a0); /* 悬停时的渐变背景 */\n"
"}\n"
"\n"
"/* 设置选中的Tab样式 */\n"
"QTabBar::tab:selected {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #4796f0, stop: 1 #2077c0); /* 选中时的渐变背景 */\n"
"    color: white;               /* 选中时的文字颜色 */\n"
"}\n"
"\n"
"/* 设置Tab选项卡的最低宽高 */\n"
"QTabBar::tab {\n"
"    min-width: 100px;           /* Tab最小宽度 */\n"
"    min-height: 30px;           /* Tab最小高度 */\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_8)
        self.textBrowser.setGeometry(QtCore.QRect(370, 30, 431, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_8)
        self.formLayoutWidget.setGeometry(QtCore.QRect(250, 250, 721, 236))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("/* QLabel 样式 */\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    padding: 5px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("/* QLabel 样式 */\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    padding: 5px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setStyleSheet("/* QLabel 样式 */\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    padding: 5px;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setStyleSheet("/* QLabel 样式 */\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    padding: 5px;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setStyleSheet("/* QLabel 样式 */\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333333;\n"
"    padding: 5px;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox_gender = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_gender.setStyleSheet("/* QComboBox 样式 */\n"
"QComboBox {\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    border: 1px solid #C0C0C0;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;  /* 设置下拉框最小高度 */\n"
"    min-width: 250px;  /* 设置下拉框最小宽度 */\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"/* QComboBox 下拉列表项样式 */\n"
"QComboBox QAbstractItemView {\n"
"    font-size: 14px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #F0F0F0; /* 下拉列表项的选中背景颜色 */\n"
"    border: 1px solid #C0C0C0;\n"
"}\n"
"")
        self.comboBox_gender.setObjectName("comboBox_gender")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_gender)
        self.lineEdit_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_name.setStyleSheet("/* QLineEdit 样式 */\n"
"QLineEdit {\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    border: 1px solid #C0C0C0;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;  /* 设置输入框最小高度 */\n"
"    min-width: 250px;  /* 设置输入框最小宽度 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.lineEdit_age = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_age.setStyleSheet("/* QLineEdit 样式 */\n"
"QLineEdit {\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    border: 1px solid #C0C0C0;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;  /* 设置输入框最小高度 */\n"
"    min-width: 250px;  /* 设置输入框最小宽度 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_age)
        self.dateEdit_diagnosis = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit_diagnosis.setStyleSheet("/* QDateEdit 样式 */\n"
"QDateEdit {\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    border: 1px solid #C0C0C0;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;  /* 设置日期选择框最小高度 */\n"
"    min-width: 250px;  /* 设置日期选择框最小宽度 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.dateEdit_diagnosis.setObjectName("dateEdit_diagnosis")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEdit_diagnosis)
        self.lineEdit_location = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_location.setStyleSheet("/* QLineEdit 样式 */\n"
"QLineEdit {\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    border: 1px solid #C0C0C0;\n"
"    border-radius: 5px;\n"
"    min-height: 30px;  /* 设置输入框最小高度 */\n"
"    min-width: 250px;  /* 设置输入框最小宽度 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lineEdit_location.setObjectName("lineEdit_location")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_location)
        self.pushButton_upload_info = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_upload_info.setGeometry(QtCore.QRect(480, 700, 241, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_upload_info.sizePolicy().hasHeightForWidth())
        self.pushButton_upload_info.setSizePolicy(sizePolicy)
        self.pushButton_upload_info.setStyleSheet("QPushButton {\n"
"    background-color: lightblue;  /* 默认背景颜色 */\n"
"    color: black;  /* 按钮文字颜色 */\n"
"    border: 1px solid black;  /* 按钮边框 */\n"
"    border-radius: 5px;  /* 按钮圆角 */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;  /* 鼠标悬停时的颜色 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: yellow;  /* 按钮被按下时的颜色 */\n"
"}\n"
"")
        self.pushButton_upload_info.setObjectName("pushButton_upload_info")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(-10, 0, 1231, 801))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_upload_image = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_upload_image.setGeometry(QtCore.QRect(480, 640, 241, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_upload_image.sizePolicy().hasHeightForWidth())
        self.pushButton_upload_image.setSizePolicy(sizePolicy)
        self.pushButton_upload_image.setStyleSheet("QPushButton {\n"
"    background-color: lightblue;  /* 默认背景颜色 */\n"
"    color: black;  /* 按钮文字颜色 */\n"
"    border: 1px solid black;  /* 按钮边框 */\n"
"    border-radius: 5px;  /* 按钮圆角 */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;  /* 鼠标悬停时的颜色 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: yellow;  /* 按钮被按下时的颜色 */\n"
"}\n"
"")
        self.pushButton_upload_image.setObjectName("pushButton_upload_image")
        self.label_upload_image = QtWidgets.QLabel(self.tab_5)
        self.label_upload_image.setGeometry(QtCore.QRect(30, 20, 1131, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_upload_image.sizePolicy().hasHeightForWidth())
        self.label_upload_image.setSizePolicy(sizePolicy)
        self.label_upload_image.setStyleSheet("QLabel {\n"
"    background-color: lightblue;  /* 默认背景颜色 */\n"
"    color: black;  /* 按钮文字颜色 */\n"
"    border: 1px solid black;  /* 按钮边框 */\n"
"    border-radius: 5px;  /* 按钮圆角 */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: lightgreen;  /* 鼠标悬停时的颜色 */\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    background-color: yellow;  /* 被按下时的颜色 */\n"
"}\n"
"")
        self.label_upload_image.setScaledContents(True)
        self.label_upload_image.setWordWrap(False)
        self.label_upload_image.setObjectName("label_upload_image")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_processed_image = QtWidgets.QLabel(self.tab_4)
        self.label_processed_image.setGeometry(QtCore.QRect(30, 20, 1131, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_processed_image.sizePolicy().hasHeightForWidth())
        self.label_processed_image.setSizePolicy(sizePolicy)
        self.label_processed_image.setStyleSheet("QLabel {\n"
"    background-color: lightblue;  /* 默认背景颜色 */\n"
"    color: black;  /* 按钮文字颜色 */\n"
"    border: 1px solid black;  /* 按钮边框 */\n"
"    border-radius: 5px;  /* 按钮圆角 */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: lightgreen;  /* 鼠标悬停时的颜色 */\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    background-color: yellow;  /* 被按下时的颜色 */\n"
"}\n"
"")
        self.label_processed_image.setScaledContents(True)
        self.label_processed_image.setWordWrap(False)
        self.label_processed_image.setObjectName("label_processed_image")
        self.pushButton_predict = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_predict.setGeometry(QtCore.QRect(480, 640, 241, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_predict.sizePolicy().hasHeightForWidth())
        self.pushButton_predict.setSizePolicy(sizePolicy)
        self.pushButton_predict.setStyleSheet("QPushButton {\n"
"    background-color: lightblue;  /* 默认背景颜色 */\n"
"    color: black;  /* 按钮文字颜色 */\n"
"    border: 1px solid black;  /* 按钮边框 */\n"
"    border-radius: 5px;  /* 按钮圆角 */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;  /* 鼠标悬停时的颜色 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: yellow;  /* 按钮被按下时的颜色 */\n"
"}\n"
"")
        self.pushButton_predict.setObjectName("pushButton_predict")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(-10, 0, 1231, 801))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_prediction_result = QtWidgets.QLabel(self.tab_6)
        self.label_prediction_result.setGeometry(QtCore.QRect(30, 20, 1131, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_prediction_result.sizePolicy().hasHeightForWidth())
        self.label_prediction_result.setSizePolicy(sizePolicy)
        self.label_prediction_result.setStyleSheet("QLabel {\n"
"    background-color: #e6f7ff;  /* 淡蓝色背景，柔和且不刺眼 */\n"
"    color: #333333;  /* 深灰色文字，清晰可见 */\n"
"    border: 2px solid #0099cc;  /* 更显眼的蓝色边框 */\n"
"    border-radius: 10px;  /* 更圆滑的圆角，给人舒适的视觉感受 */\n"
"    padding: 10px 15px;  /* 增加内部边距，确保文字不会紧贴边框 */\n"
"    font-family: \"Arial\", sans-serif;  /* 使用常见的现代字体 */\n"
"    font-size: 16px;  /* 增加文字大小，使其更易读 */\n"
"    font-weight: bold;  /* 加粗字体，强调诊断结果 */\n"
"    text-align: center;  /* 文字居中，适合展示重要信息 */\n"
"    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);  /* 添加阴影效果，提升层次感 */\n"
"    transition: background-color 0.3s ease, box-shadow 0.3s ease;  /* 平滑过渡效果 */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #ccffcc;  /* 鼠标悬停时的柔和绿色 */\n"
"    box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.3);  /* 鼠标悬停时的阴影加深 */\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    background-color: #ffeb99;  /* 按下时的黄色背景 */\n"
"    box-shadow: none;  /* 按下时取消阴影 */\n"
"}\n"
"\n"
"")
        self.label_prediction_result.setScaledContents(True)
        self.label_prediction_result.setWordWrap(False)
        self.label_prediction_result.setObjectName("label_prediction_result")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 640, 241, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: lightblue;  /* 默认背景颜色 */\n"
"    color: black;  /* 按钮文字颜色 */\n"
"    border: 1px solid black;  /* 按钮边框 */\n"
"    border-radius: 5px;  /* 按钮圆角 */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;  /* 鼠标悬停时的颜色 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: yellow;  /* 按钮被按下时的颜色 */\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ROP智能检查"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">请务必在这里上传你的个人信息！！！</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("Form", "姓名"))
        self.label_5.setText(_translate("Form", "年龄"))
        self.label_6.setText(_translate("Form", "诊断地点"))
        self.label_7.setText(_translate("Form", "诊断时间"))
        self.label_8.setText(_translate("Form", "性别"))
        self.comboBox_gender.setItemText(0, _translate("Form", "男性"))
        self.comboBox_gender.setItemText(1, _translate("Form", "女性"))
        self.pushButton_upload_info.setText(_translate("Form", "点击上传"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Form", "信息上传"))
        self.pushButton_upload_image.setText(_translate("Form", "点击上传"))
        self.label_upload_image.setText(_translate("Form", "上传图片预览"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "预处理上传"))
        self.label_processed_image.setText(_translate("Form", "预处理图片预览"))
        self.pushButton_predict.setText(_translate("Form", "点击进行ROP诊断"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "预处理结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "图像上传"))
        self.label_prediction_result.setText(_translate("Form", "ROP诊断结果"))
        self.pushButton_3.setText(_translate("Form", "查看医疗建议"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("Form", "ROP处理图像"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("Form", "医疗建议"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "ROP诊断结果及建议"))