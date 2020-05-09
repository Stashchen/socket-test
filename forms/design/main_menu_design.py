# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_menu(object):
    def setupUi(self, main_menu):
        main_menu.setObjectName("main_menu")
        main_menu.resize(500, 600)
        self.centralwidget = QtWidgets.QWidget(main_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.create_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.create_btn.setFont(font)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.join_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.join_btn.setFont(font)
        self.join_btn.setObjectName("join_btn")
        self.verticalLayout.addWidget(self.join_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.exit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        main_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "SuperDumass"))
        self.label.setText(_translate("main_menu", "Svoya Igra BNTU edition"))
        self.create_btn.setText(_translate("main_menu", "CREATE"))
        self.join_btn.setText(_translate("main_menu", "JOIN"))
        self.exit_btn.setText(_translate("main_menu", "EXIT"))
        self.label_2.setText(_translate("main_menu", "Made by  - Zhenya and Pasha"))
