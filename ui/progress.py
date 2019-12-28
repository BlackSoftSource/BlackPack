# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zielak/Dokumenty/Programowanie/BlackPack/ui/progress.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(458, 229)
        Dialog.setMaximumSize(QtCore.QSize(483, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../.designer/pixmaps/blackpack-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(101)
        sizePolicy.setVerticalStretch(81)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(101, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../../.designer/pixmaps/blackpack-logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 3)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setMaximum(200)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(182, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(142, 0))
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BlackPack"))
        self.label.setText(_translate("Dialog", "Building RPM package ..."))
        self.progressBar.setFormat(_translate("Dialog", "%p%"))
        self.label_3.setText(_translate("Dialog", "Generating SPEC ..."))
        self.pushButton.setText(_translate("Dialog", "Cancel"))
