# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MENU(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(233, 233)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_3.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "功能选择"))
        self.pushButton.setText(_translate("Form", "打开注释工具窗口"))
        self.checkBox.setText(_translate("Form", "窗口置顶"))
        self.pushButton_2.setText(_translate("Form", "打开机器人信息窗口"))
        self.checkBox_2.setText(_translate("Form", "窗口置顶"))
        self.pushButton_5.setText(_translate("Form", "打开发那科变量工具"))
        self.checkBox_3.setText(_translate("Form", "窗口置顶"))
        self.pushButton_4.setText(_translate("Form", "下载所有LS程序到本地"))
        self.pushButton_3.setText(_translate("Form", "关闭已经打开的所有窗口"))

        self.pushButton.clicked.connect(Form.mian_win_show)
        self.pushButton_2.clicked.connect(Form.rbinfo_win_show)
        self.pushButton_3.clicked.connect(Form.close_all_win)
        self.pushButton_4.clicked.connect(Form.download_all_ls)
        self.pushButton_5.clicked.connect(Form.fanuc_var_win_show)

        self.checkBox.clicked.connect(Form.mian_top)
        self.checkBox_2.clicked.connect(Form.rbinfo_top)
        self.checkBox_3.clicked.connect(Form.fanuc_var_top)
