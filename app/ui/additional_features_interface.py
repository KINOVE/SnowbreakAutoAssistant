# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'additional_features_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_additional_features(object):
    def setupUi(self, additional_features):
        additional_features.setObjectName("additional_features")
        additional_features.resize(760, 665)
        self.gridLayout = QtWidgets.QGridLayout(additional_features)
        self.gridLayout.setObjectName("gridLayout")
        self.SegmentedWidget = SegmentedWidget(additional_features)
        self.SegmentedWidget.setObjectName("SegmentedWidget")
        self.gridLayout.addWidget(self.SegmentedWidget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(additional_features)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_fishing = QtWidgets.QWidget()
        self.page_fishing.setObjectName("page_fishing")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_fishing)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BodyLabel = BodyLabel(self.page_fishing)
        self.BodyLabel.setObjectName("BodyLabel")
        self.gridLayout_2.addWidget(self.BodyLabel, 0, 0, 1, 1)
        self.PushButton = PushButton(self.page_fishing)
        self.PushButton.setObjectName("PushButton")
        self.gridLayout_2.addWidget(self.PushButton, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_fishing)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BodyLabel_2 = BodyLabel(self.page_2)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.gridLayout_3.addWidget(self.BodyLabel_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.BodyLabel_3 = BodyLabel(self.page_3)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.gridLayout_4.addWidget(self.BodyLabel_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.retranslateUi(additional_features)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(additional_features)

    def retranslateUi(self, additional_features):
        _translate = QtCore.QCoreApplication.translate
        additional_features.setWindowTitle(_translate("additional_features", "Frame"))
        self.BodyLabel.setText(_translate("additional_features", "自动钓鱼页面"))
        self.PushButton.setText(_translate("additional_features", "开始钓鱼"))
        self.BodyLabel_2.setText(_translate("additional_features", "待开发"))
        self.BodyLabel_3.setText(_translate("additional_features", "待开发"))
from qfluentwidgets import BodyLabel, PushButton, SegmentedWidget
