# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 850)
        Form.setMaximumSize(QtCore.QSize(650, 850))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setMaximumSize(QtCore.QSize(608, 850))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(110, 30, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.widget_7 = QtWidgets.QWidget(self.page)
        self.widget_7.setGeometry(QtCore.QRect(60, 80, 561, 121))
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lb_show = QtWidgets.QLabel(self.page)
        self.lb_show.setGeometry(QtCore.QRect(150, 190, 301, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_show.sizePolicy().hasHeightForWidth())
        self.lb_show.setSizePolicy(sizePolicy)
        self.lb_show.setText("")
        self.lb_show.setScaledContents(True)
        self.lb_show.setWordWrap(False)
        self.lb_show.setObjectName("lb_show")
        self.file_widget = QtWidgets.QWidget(self.page)
        self.file_widget.setGeometry(QtCore.QRect(0, 640, 215, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_widget.sizePolicy().hasHeightForWidth())
        self.file_widget.setSizePolicy(sizePolicy)
        self.file_widget.setObjectName("file_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.file_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.file_widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.file_widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pb_open = QtWidgets.QPushButton(self.page)
        self.pb_open.setGeometry(QtCore.QRect(270, 420, 75, 31))
        self.pb_open.setObjectName("pb_open")
        self.type_combox = QtWidgets.QComboBox(self.page)
        self.type_combox.setGeometry(QtCore.QRect(230, 240, 150, 31))
        self.type_combox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.type_combox.setObjectName("type_combox")
        self.pb_browser = QtWidgets.QToolButton(self.page)
        self.pb_browser.setGeometry(QtCore.QRect(80, 280, 450, 108))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_browser.sizePolicy().hasHeightForWidth())
        self.pb_browser.setSizePolicy(sizePolicy)
        self.pb_browser.setMaximumSize(QtCore.QSize(460, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("select_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_browser.setIcon(icon)
        self.pb_browser.setIconSize(QtCore.QSize(500, 400))
        self.pb_browser.setAutoRepeatDelay(500)
        self.pb_browser.setAutoRepeatInterval(150)
        self.pb_browser.setAutoRaise(True)
        self.pb_browser.setObjectName("pb_browser")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(270, 470, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.name_list = QtWidgets.QListWidget(self.page)
        self.name_list.setGeometry(QtCore.QRect(90, 540, 151, 221))
        self.name_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_list.setObjectName("name_list")
        self.label_list = QtWidgets.QListWidget(self.page)
        self.label_list.setGeometry(QtCore.QRect(240, 540, 131, 221))
        self.label_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_list.setObjectName("label_list")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(130, 510, 81, 18))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(270, 510, 81, 18))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.time_list = QtWidgets.QListWidget(self.page)
        self.time_list.setGeometry(QtCore.QRect(370, 540, 151, 221))
        self.time_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time_list.setObjectName("time_list")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(400, 510, 81, 18))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.select_type_label = QtWidgets.QLabel(self.page)
        self.select_type_label.setGeometry(QtCore.QRect(160, 200, 286, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.select_type_label.setFont(font)
        self.select_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.select_type_label.setObjectName("select_type_label")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setGeometry(QtCore.QRect(80, 420, 271, 81))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.type_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.type_label.setFont(font)
        self.type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.type_label.setObjectName("type_label")
        self.gridLayout_2.addWidget(self.type_label, 1, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(80, 510, 451, 131))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 3, 1, 1)
        self.amb_rate = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.amb_rate.setFont(font)
        self.amb_rate.setText("")
        self.amb_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.amb_rate.setObjectName("amb_rate")
        self.gridLayout_3.addWidget(self.amb_rate, 1, 0, 1, 1)
        self.micro_rate = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.micro_rate.setFont(font)
        self.micro_rate.setText("")
        self.micro_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.micro_rate.setObjectName("micro_rate")
        self.gridLayout_3.addWidget(self.micro_rate, 1, 1, 1, 1)
        self.fungus_rate = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fungus_rate.setFont(font)
        self.fungus_rate.setText("")
        self.fungus_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.fungus_rate.setObjectName("fungus_rate")
        self.gridLayout_3.addWidget(self.fungus_rate, 1, 2, 1, 1)
        self.virus_rate = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.virus_rate.setFont(font)
        self.virus_rate.setText("")
        self.virus_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.virus_rate.setObjectName("virus_rate")
        self.gridLayout_3.addWidget(self.virus_rate, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(80, 150, 403, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lb_show_2 = QtWidgets.QLabel(self.page_2)
        self.lb_show_2.setGeometry(QtCore.QRect(150, 190, 301, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_show_2.sizePolicy().hasHeightForWidth())
        self.lb_show_2.setSizePolicy(sizePolicy)
        self.lb_show_2.setText("")
        self.lb_show_2.setScaledContents(True)
        self.lb_show_2.setWordWrap(False)
        self.lb_show_2.setObjectName("lb_show_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(120, 30, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(80, 100, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.widget_8 = QtWidgets.QWidget(self.page_2)
        self.widget_8.setGeometry(QtCore.QRect(80, 650, 261, 81))
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.time_label = QtWidgets.QLabel(self.widget_8)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.gridLayout_4.addWidget(self.time_label, 1, 1, 1, 1)
        self.return_btn = QtWidgets.QPushButton(self.page_2)
        self.return_btn.setGeometry(QtCore.QRect(410, 750, 112, 34))
        self.return_btn.setObjectName("return_btn")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Keratitis Diagnosis System"))
        self.label_5.setText(_translate("Form", "Keratitis Diagnosis System"))
        self.label.setText(_translate("Form", "Project：Keratitis Image Recognition via DL System"))
        self.label_3.setText(_translate("Form", "Upload Your Image:"))
        self.label_2.setText(_translate("Form", "file_path:"))
        self.pb_open.setText(_translate("Form", "Submit"))
        self.pb_browser.setWhatsThis(_translate("Form", "<html><head/><body><p>浏览文件</p></body></html>"))
        self.pb_browser.setText(_translate("Form", "Select"))
        self.label_16.setText(_translate("Form", "history"))
        self.label_17.setText(_translate("Form", "name"))
        self.label_18.setText(_translate("Form", "label"))
        self.label_19.setText(_translate("Form", "time"))
        self.select_type_label.setText(_translate("Form", "Select Picture Type"))
        self.label_9.setText(_translate("Form", "Your Label is:"))
        self.type_label.setText(_translate("Form", "han"))
        self.label_10.setText(_translate("Form", "Score for 4 types of Keratits："))
        self.label_11.setText(_translate("Form", "amb"))
        self.label_12.setText(_translate("Form", "micro"))
        self.label_13.setText(_translate("Form", "fubgus"))
        self.label_14.setText(_translate("Form", "virus"))
        self.label_4.setText(_translate("Form", "For image:"))
        self.label_6.setText(_translate("Form", "Keratitis Diagnosis System"))
        self.label_7.setText(_translate("Form", "Congrats! Your image is successfully identitfied!"))
        self.label_8.setText(_translate("Form", "Time Consuming:"))
        self.time_label.setText(_translate("Form", "s"))
        self.return_btn.setText(_translate("Form", "Return"))
import res_rc
