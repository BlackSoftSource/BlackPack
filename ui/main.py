# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zielak/Dokumenty/Programowanie/BlackPack/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BlackPackWizard(object):
    def setupUi(self, BlackPackWizard):
        BlackPackWizard.setObjectName("BlackPackWizard")
        BlackPackWizard.setEnabled(True)
        BlackPackWizard.resize(831, 594)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pixmaps/blackpack-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BlackPackWizard.setWindowIcon(icon)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.gridLayout = QtWidgets.QGridLayout(self.wizardPage1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.wizardPage1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.wizardPage1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.wizardPage1)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.wizardPage1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.wizardPage1)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1)
        self.pkgversion = QtWidgets.QLineEdit(self.wizardPage1)
        self.pkgversion.setObjectName("pkgversion")
        self.gridLayout.addWidget(self.pkgversion, 2, 1, 1, 2)
        self.pkgrelease = QtWidgets.QLineEdit(self.wizardPage1)
        self.pkgrelease.setObjectName("pkgrelease")
        self.gridLayout.addWidget(self.pkgrelease, 3, 1, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.wizardPage1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 6, 1, 1, 2)
        self.comboBox_3 = QtWidgets.QComboBox(self.wizardPage1)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 7, 1, 1, 2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.wizardPage1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.wizardPage1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.wizardPage1)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.pkgdesc = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.pkgdesc.setObjectName("pkgdesc")
        self.gridLayout_29.addWidget(self.pkgdesc, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 8, 0, 1, 3)
        self.pkgsummary = QtWidgets.QLineEdit(self.wizardPage1)
        self.pkgsummary.setObjectName("pkgsummary")
        self.gridLayout.addWidget(self.pkgsummary, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.wizardPage1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.pkgname = QtWidgets.QLineEdit(self.wizardPage1)
        self.pkgname.setObjectName("pkgname")
        self.gridLayout.addWidget(self.pkgname, 0, 2, 1, 1)
        BlackPackWizard.addPage(self.wizardPage1)
        self.wizardPage = QtWidgets.QWizardPage()
        self.wizardPage.setObjectName("wizardPage")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.wizardPage)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_7 = QtWidgets.QGroupBox(self.wizardPage)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_20 = QtWidgets.QLabel(self.groupBox_7)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 0, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_7.addWidget(self.lineEdit_10, 0, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_7.addWidget(self.toolButton_2, 0, 2, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_7, 0, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(201, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.wizardPage)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_10.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.wizardPage)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_10.addWidget(self.pushButton_11, 1, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.wizardPage)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_10.addWidget(self.pushButton_12, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(201, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 1, 4, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.wizardPage)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_10.addWidget(self.listWidget_3, 2, 0, 1, 5)
        BlackPackWizard.addPage(self.wizardPage)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.wizardPage2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_17 = QtWidgets.QLabel(self.wizardPage2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 2)
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.wizardPage2)
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.gridLayout_9.addWidget(self.plainTextEdit_6, 1, 0, 1, 2)
        BlackPackWizard.addPage(self.wizardPage2)
        self.wizardPage3 = QtWidgets.QWizardPage()
        self.wizardPage3.setObjectName("wizardPage3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wizardPage3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.wizardPage3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_4.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout_5.addWidget(self.plainTextEdit_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.gridLayout_6.addWidget(self.plainTextEdit_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.gridLayout_11.addWidget(self.plainTextEdit_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        BlackPackWizard.addPage(self.wizardPage3)
        self.wizardPage4 = QtWidgets.QWizardPage()
        self.wizardPage4.setObjectName("wizardPage4")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.wizardPage4)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.wizardPage4)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.plainTextEdit_11 = QtWidgets.QPlainTextEdit(self.tab_11)
        self.plainTextEdit_11.setObjectName("plainTextEdit_11")
        self.gridLayout_13.addWidget(self.plainTextEdit_11, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.plainTextEdit_12 = QtWidgets.QPlainTextEdit(self.tab_12)
        self.plainTextEdit_12.setObjectName("plainTextEdit_12")
        self.gridLayout_14.addWidget(self.plainTextEdit_12, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.plainTextEdit_13 = QtWidgets.QPlainTextEdit(self.tab_13)
        self.plainTextEdit_13.setObjectName("plainTextEdit_13")
        self.gridLayout_15.addWidget(self.plainTextEdit_13, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_14)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.plainTextEdit_14 = QtWidgets.QPlainTextEdit(self.tab_14)
        self.plainTextEdit_14.setObjectName("plainTextEdit_14")
        self.gridLayout_16.addWidget(self.plainTextEdit_14, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_14, "")
        self.gridLayout_18.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        BlackPackWizard.addPage(self.wizardPage4)
        self.wizardPage6 = QtWidgets.QWizardPage()
        self.wizardPage6.setObjectName("wizardPage6")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.wizardPage6)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.pushButton_9 = QtWidgets.QPushButton(self.wizardPage6)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_26.addWidget(self.pushButton_9, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.wizardPage6)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_8.addWidget(self.lineEdit, 0, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        icon = QtGui.QIcon.fromTheme("folder")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        icon = QtGui.QIcon.fromTheme("folder")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_8.addWidget(self.pushButton_8, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem3, 1, 3, 1, 1)
        self.gridLayout_26.addWidget(self.groupBox_2, 0, 0, 1, 4)
        self.groupBox = QtWidgets.QGroupBox(self.wizardPage6)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setEnabled(False)
        self.toolButton.setText("")
        icon = QtGui.QIcon.fromTheme("folder")
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_23.addWidget(self.toolButton, 2, 4, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_23.addWidget(self.checkBox_2, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout_23.addWidget(self.label_15, 0, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_23.addWidget(self.lineEdit_5, 0, 2, 1, 3)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setText("")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_23.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_23.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_23.addWidget(self.comboBox_2, 1, 1, 1, 4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_23.addWidget(self.lineEdit_2, 2, 1, 1, 3)
        self.gridLayout_26.addWidget(self.groupBox, 0, 4, 1, 4)
        self.pushButton_3 = QtWidgets.QPushButton(self.wizardPage6)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_26.addWidget(self.pushButton_3, 2, 5, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.wizardPage6)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_26.addWidget(self.pushButton_2, 2, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.wizardPage6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout_26.addWidget(self.tableWidget, 1, 0, 1, 8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_26.addItem(spacerItem4, 2, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.wizardPage6)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_26.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.wizardPage6)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_26.addWidget(self.pushButton_4, 2, 6, 1, 1)
        BlackPackWizard.addPage(self.wizardPage6)
        self.wizardPage7 = QtWidgets.QWizardPage()
        self.wizardPage7.setObjectName("wizardPage7")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.wizardPage7)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.groupBox_3 = QtWidgets.QGroupBox(self.wizardPage7)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_27.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_27.addWidget(self.label_8, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_27.addItem(spacerItem5, 2, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_27.addWidget(self.lineEdit_3, 0, 1, 1, 4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_27.addItem(spacerItem6, 2, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_27.addItem(spacerItem7, 2, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_27.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.gridLayout_28.addWidget(self.groupBox_3, 0, 0, 1, 5)
        spacerItem8 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_28.addItem(spacerItem8, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.wizardPage7)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_28.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.wizardPage7)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_28.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.wizardPage7)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_28.addWidget(self.pushButton_7, 1, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_28.addItem(spacerItem9, 1, 4, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.wizardPage7)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.gridLayout_28.addWidget(self.tableWidget_2, 2, 0, 1, 5)
        BlackPackWizard.addPage(self.wizardPage7)
        self.wizardPage8 = QtWidgets.QWizardPage()
        self.wizardPage8.setObjectName("wizardPage8")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.wizardPage8)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.groupBox_5 = QtWidgets.QGroupBox(self.wizardPage8)
        self.groupBox_5.setCheckable(True)
        self.groupBox_5.setChecked(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_31.addWidget(self.label_6, 0, 0, 1, 1)
        self.pkgname_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.pkgname_2.setObjectName("pkgname_2")
        self.gridLayout_31.addWidget(self.pkgname_2, 0, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_31.addWidget(self.label_13, 1, 0, 1, 1)
        self.pkgversion_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.pkgversion_2.setObjectName("pkgversion_2")
        self.gridLayout_31.addWidget(self.pkgversion_2, 1, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.gridLayout_31.addWidget(self.label_10, 2, 0, 1, 1)
        self.pkgrelease_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.pkgrelease_2.setObjectName("pkgrelease_2")
        self.gridLayout_31.addWidget(self.pkgrelease_2, 2, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_31.addWidget(self.label_12, 3, 0, 1, 1)
        self.pkgsummary_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.pkgsummary_2.setObjectName("pkgsummary_2")
        self.gridLayout_31.addWidget(self.pkgsummary_2, 3, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout_31.addWidget(self.label_14, 4, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_31.addWidget(self.checkBox, 4, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(607, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_31.addItem(spacerItem10, 4, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_31.addWidget(self.label_11, 5, 0, 1, 1)
        self.pkgrelease_3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.pkgrelease_3.setObjectName("pkgrelease_3")
        self.gridLayout_31.addWidget(self.pkgrelease_3, 5, 1, 1, 2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.pkgdesc_2 = QtWidgets.QPlainTextEdit(self.groupBox_6)
        self.pkgdesc_2.setObjectName("pkgdesc_2")
        self.gridLayout_30.addWidget(self.pkgdesc_2, 0, 0, 1, 1)
        self.gridLayout_31.addWidget(self.groupBox_6, 6, 0, 1, 3)
        self.gridLayout_32.addWidget(self.groupBox_5, 0, 0, 1, 1)
        BlackPackWizard.addPage(self.wizardPage8)

        self.retranslateUi(BlackPackWizard)
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(3)
        self.radioButton.toggled['bool'].connect(self.lineEdit_2.setDisabled)
        self.radioButton.toggled['bool'].connect(self.toolButton.setDisabled)
        self.radioButton_2.toggled['bool'].connect(self.comboBox_2.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.lineEdit_5.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(BlackPackWizard)

    def retranslateUi(self, BlackPackWizard):
        _translate = QtCore.QCoreApplication.translate
        BlackPackWizard.setWindowTitle(_translate("BlackPackWizard", "BlackPack"))
        self.wizardPage1.setTitle(_translate("BlackPackWizard", "Create RPM packages easy"))
        self.wizardPage1.setSubTitle(_translate("BlackPackWizard", "SPEC file"))
        self.label.setText(_translate("BlackPackWizard", "Package name: "))
        self.label_4.setText(_translate("BlackPackWizard", "Summary:"))
        self.label_9.setText(_translate("BlackPackWizard", "Architecture:"))
        self.label_2.setText(_translate("BlackPackWizard", "Version:"))
        self.label_16.setText(_translate("BlackPackWizard", "Website:"))
        self.comboBox.setItemText(0, _translate("BlackPackWizard", "GPL-3"))
        self.comboBox.setItemText(1, _translate("BlackPackWizard", "GPL-2"))
        self.comboBox.setItemText(2, _translate("BlackPackWizard", "GPL-1"))
        self.comboBox.setItemText(3, _translate("BlackPackWizard", "Apache"))
        self.comboBox.setItemText(4, _translate("BlackPackWizard", "Other..."))
        self.comboBox_3.setItemText(0, _translate("BlackPackWizard", "x86_64"))
        self.comboBox_3.setItemText(1, _translate("BlackPackWizard", "x86"))
        self.comboBox_3.setItemText(2, _translate("BlackPackWizard", "noarch"))
        self.label_3.setText(_translate("BlackPackWizard", "Release:"))
        self.groupBox_4.setTitle(_translate("BlackPackWizard", "Description"))
        self.label_5.setText(_translate("BlackPackWizard", "License:"))
        self.wizardPage.setTitle(_translate("BlackPackWizard", "Create RPM packages easy"))
        self.wizardPage.setSubTitle(_translate("BlackPackWizard", "Add source tarballs"))
        self.label_20.setText(_translate("BlackPackWizard", "Source path:"))
        self.toolButton_2.setText(_translate("BlackPackWizard", "..."))
        self.pushButton_10.setText(_translate("BlackPackWizard", "Add source"))
        self.pushButton_11.setText(_translate("BlackPackWizard", "Remove source"))
        self.pushButton_12.setText(_translate("BlackPackWizard", "Clean all"))
        self.wizardPage2.setTitle(_translate("BlackPackWizard", "Create RPM packages easy"))
        self.wizardPage2.setSubTitle(_translate("BlackPackWizard", "Program license"))
        self.label_17.setText(_translate("BlackPackWizard", "Will save in /usr/share/doc/<program_name>/copyright"))
        self.plainTextEdit_6.setPlainText(_translate("BlackPackWizard", "                    GNU GENERAL PUBLIC LICENSE\n"
"                       Version 3, 29 June 2007\n"
"\n"
" Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>\n"
" Everyone is permitted to copy and distribute verbatim copies\n"
" of this license document, but changing it is not allowed.\n"
"\n"
"                            Preamble\n"
"\n"
"  The GNU General Public License is a free, copyleft license for\n"
"software and other kinds of works.\n"
"\n"
"  The licenses for most software and other practical works are designed\n"
"to take away your freedom to share and change the works.  By contrast,\n"
"the GNU General Public License is intended to guarantee your freedom to\n"
"share and change all versions of a program--to make sure it remains free\n"
"software for all its users.  We, the Free Software Foundation, use the\n"
"GNU General Public License for most of our software; it applies also to\n"
"any other work released this way by its authors.  You can apply it to\n"
"your programs, too.\n"
"\n"
"  When we speak of free software, we are referring to freedom, not\n"
"price.  Our General Public Licenses are designed to make sure that you\n"
"have the freedom to distribute copies of free software (and charge for\n"
"them if you wish), that you receive source code or can get it if you\n"
"want it, that you can change the software or use pieces of it in new\n"
"free programs, and that you know you can do these things.\n"
"\n"
"  To protect your rights, we need to prevent others from denying you\n"
"these rights or asking you to surrender the rights.  Therefore, you have\n"
"certain responsibilities if you distribute copies of the software, or if\n"
"you modify it: responsibilities to respect the freedom of others.\n"
"\n"
"  For example, if you distribute copies of such a program, whether\n"
"gratis or for a fee, you must pass on to the recipients the same\n"
"freedoms that you received.  You must make sure that they, too, receive\n"
"or can get the source code.  And you must show them these terms so they\n"
"know their rights.\n"
"\n"
"  Developers that use the GNU GPL protect your rights with two steps:\n"
"(1) assert copyright on the software, and (2) offer you this License\n"
"giving you legal permission to copy, distribute and/or modify it.\n"
"\n"
"  For the developers\' and authors\' protection, the GPL clearly explains\n"
"that there is no warranty for this free software.  For both users\' and\n"
"authors\' sake, the GPL requires that modified versions be marked as\n"
"changed, so that their problems will not be attributed erroneously to\n"
"authors of previous versions.\n"
"\n"
"  Some devices are designed to deny users access to install or run\n"
"modified versions of the software inside them, although the manufacturer\n"
"can do so.  This is fundamentally incompatible with the aim of\n"
"protecting users\' freedom to change the software.  The systematic\n"
"pattern of such abuse occurs in the area of products for individuals to\n"
"use, which is precisely where it is most unacceptable.  Therefore, we\n"
"have designed this version of the GPL to prohibit the practice for those\n"
"products.  If such problems arise substantially in other domains, we\n"
"stand ready to extend this provision to those domains in future versions\n"
"of the GPL, as needed to protect the freedom of users.\n"
"\n"
"  Finally, every program is threatened constantly by software patents.\n"
"States should not allow patents to restrict development and use of\n"
"software on general-purpose computers, but in those that do, we wish to\n"
"avoid the special danger that patents applied to a free program could\n"
"make it effectively proprietary.  To prevent this, the GPL assures that\n"
"patents cannot be used to render the program non-free.\n"
"\n"
"  The precise terms and conditions for copying, distribution and\n"
"modification follow.\n"
"\n"
"                       TERMS AND CONDITIONS\n"
"\n"
"  0. Definitions.\n"
"\n"
"  \"This License\" refers to version 3 of the GNU General Public License.\n"
"\n"
"  \"Copyright\" also means copyright-like laws that apply to other kinds of\n"
"works, such as semiconductor masks.\n"
"\n"
"  \"The Program\" refers to any copyrightable work licensed under this\n"
"License.  Each licensee is addressed as \"you\".  \"Licensees\" and\n"
"\"recipients\" may be individuals or organizations.\n"
"\n"
"  To \"modify\" a work means to copy from or adapt all or part of the work\n"
"in a fashion requiring copyright permission, other than the making of an\n"
"exact copy.  The resulting work is called a \"modified version\" of the\n"
"earlier work or a work \"based on\" the earlier work.\n"
"\n"
"  A \"covered work\" means either the unmodified Program or a work based\n"
"on the Program.\n"
"\n"
"  To \"propagate\" a work means to do anything with it that, without\n"
"permission, would make you directly or secondarily liable for\n"
"infringement under applicable copyright law, except executing it on a\n"
"computer or modifying a private copy.  Propagation includes copying,\n"
"distribution (with or without modification), making available to the\n"
"public, and in some countries other activities as well.\n"
"\n"
"  To \"convey\" a work means any kind of propagation that enables other\n"
"parties to make or receive copies.  Mere interaction with a user through\n"
"a computer network, with no transfer of a copy, is not conveying.\n"
"\n"
"  An interactive user interface displays \"Appropriate Legal Notices\"\n"
"to the extent that it includes a convenient and prominently visible\n"
"feature that (1) displays an appropriate copyright notice, and (2)\n"
"tells the user that there is no warranty for the work (except to the\n"
"extent that warranties are provided), that licensees may convey the\n"
"work under this License, and how to view a copy of this License.  If\n"
"the interface presents a list of user commands or options, such as a\n"
"menu, a prominent item in the list meets this criterion.\n"
"\n"
"  1. Source Code.\n"
"\n"
"  The \"source code\" for a work means the preferred form of the work\n"
"for making modifications to it.  \"Object code\" means any non-source\n"
"form of a work.\n"
"\n"
"  A \"Standard Interface\" means an interface that either is an official\n"
"standard defined by a recognized standards body, or, in the case of\n"
"interfaces specified for a particular programming language, one that\n"
"is widely used among developers working in that language.\n"
"\n"
"  The \"System Libraries\" of an executable work include anything, other\n"
"than the work as a whole, that (a) is included in the normal form of\n"
"packaging a Major Component, but which is not part of that Major\n"
"Component, and (b) serves only to enable use of the work with that\n"
"Major Component, or to implement a Standard Interface for which an\n"
"implementation is available to the public in source code form.  A\n"
"\"Major Component\", in this context, means a major essential component\n"
"(kernel, window system, and so on) of the specific operating system\n"
"(if any) on which the executable work runs, or a compiler used to\n"
"produce the work, or an object code interpreter used to run it.\n"
"\n"
"  The \"Corresponding Source\" for a work in object code form means all\n"
"the source code needed to generate, install, and (for an executable\n"
"work) run the object code and to modify the work, including scripts to\n"
"control those activities.  However, it does not include the work\'s\n"
"System Libraries, or general-purpose tools or generally available free\n"
"programs which are used unmodified in performing those activities but\n"
"which are not part of the work.  For example, Corresponding Source\n"
"includes interface definition files associated with source files for\n"
"the work, and the source code for shared libraries and dynamically\n"
"linked subprograms that the work is specifically designed to require,\n"
"such as by intimate data communication or control flow between those\n"
"subprograms and other parts of the work.\n"
"\n"
"  The Corresponding Source need not include anything that users\n"
"can regenerate automatically from other parts of the Corresponding\n"
"Source.\n"
"\n"
"  The Corresponding Source for a work in source code form is that\n"
"same work.\n"
"\n"
"  2. Basic Permissions.\n"
"\n"
"  All rights granted under this License are granted for the term of\n"
"copyright on the Program, and are irrevocable provided the stated\n"
"conditions are met.  This License explicitly affirms your unlimited\n"
"permission to run the unmodified Program.  The output from running a\n"
"covered work is covered by this License only if the output, given its\n"
"content, constitutes a covered work.  This License acknowledges your\n"
"rights of fair use or other equivalent, as provided by copyright law.\n"
"\n"
"  You may make, run and propagate covered works that you do not\n"
"convey, without conditions so long as your license otherwise remains\n"
"in force.  You may convey covered works to others for the sole purpose\n"
"of having them make modifications exclusively for you, or provide you\n"
"with facilities for running those works, provided that you comply with\n"
"the terms of this License in conveying all material for which you do\n"
"not control copyright.  Those thus making or running the covered works\n"
"for you must do so exclusively on your behalf, under your direction\n"
"and control, on terms that prohibit them from making any copies of\n"
"your copyrighted material outside their relationship with you.\n"
"\n"
"  Conveying under any other circumstances is permitted solely under\n"
"the conditions stated below.  Sublicensing is not allowed; section 10\n"
"makes it unnecessary.\n"
"\n"
"  3. Protecting Users\' Legal Rights From Anti-Circumvention Law.\n"
"\n"
"  No covered work shall be deemed part of an effective technological\n"
"measure under any applicable law fulfilling obligations under article\n"
"11 of the WIPO copyright treaty adopted on 20 December 1996, or\n"
"similar laws prohibiting or restricting circumvention of such\n"
"measures.\n"
"\n"
"  When you convey a covered work, you waive any legal power to forbid\n"
"circumvention of technological measures to the extent such circumvention\n"
"is effected by exercising rights under this License with respect to\n"
"the covered work, and you disclaim any intention to limit operation or\n"
"modification of the work as a means of enforcing, against the work\'s\n"
"users, your or third parties\' legal rights to forbid circumvention of\n"
"technological measures.\n"
"\n"
"  4. Conveying Verbatim Copies.\n"
"\n"
"  You may convey verbatim copies of the Program\'s source code as you\n"
"receive it, in any medium, provided that you conspicuously and\n"
"appropriately publish on each copy an appropriate copyright notice;\n"
"keep intact all notices stating that this License and any\n"
"non-permissive terms added in accord with section 7 apply to the code;\n"
"keep intact all notices of the absence of any warranty; and give all\n"
"recipients a copy of this License along with the Program.\n"
"\n"
"  You may charge any price or no price for each copy that you convey,\n"
"and you may offer support or warranty protection for a fee.\n"
"\n"
"  5. Conveying Modified Source Versions.\n"
"\n"
"  You may convey a work based on the Program, or the modifications to\n"
"produce it from the Program, in the form of source code under the\n"
"terms of section 4, provided that you also meet all of these conditions:\n"
"\n"
"    a) The work must carry prominent notices stating that you modified\n"
"    it, and giving a relevant date.\n"
"\n"
"    b) The work must carry prominent notices stating that it is\n"
"    released under this License and any conditions added under section\n"
"    7.  This requirement modifies the requirement in section 4 to\n"
"    \"keep intact all notices\".\n"
"\n"
"    c) You must license the entire work, as a whole, under this\n"
"    License to anyone who comes into possession of a copy.  This\n"
"    License will therefore apply, along with any applicable section 7\n"
"    additional terms, to the whole of the work, and all its parts,\n"
"    regardless of how they are packaged.  This License gives no\n"
"    permission to license the work in any other way, but it does not\n"
"    invalidate such permission if you have separately received it.\n"
"\n"
"    d) If the work has interactive user interfaces, each must display\n"
"    Appropriate Legal Notices; however, if the Program has interactive\n"
"    interfaces that do not display Appropriate Legal Notices, your\n"
"    work need not make them do so.\n"
"\n"
"  A compilation of a covered work with other separate and independent\n"
"works, which are not by their nature extensions of the covered work,\n"
"and which are not combined with it such as to form a larger program,\n"
"in or on a volume of a storage or distribution medium, is called an\n"
"\"aggregate\" if the compilation and its resulting copyright are not\n"
"used to limit the access or legal rights of the compilation\'s users\n"
"beyond what the individual works permit.  Inclusion of a covered work\n"
"in an aggregate does not cause this License to apply to the other\n"
"parts of the aggregate.\n"
"\n"
"  6. Conveying Non-Source Forms.\n"
"\n"
"  You may convey a covered work in object code form under the terms\n"
"of sections 4 and 5, provided that you also convey the\n"
"machine-readable Corresponding Source under the terms of this License,\n"
"in one of these ways:\n"
"\n"
"    a) Convey the object code in, or embodied in, a physical product\n"
"    (including a physical distribution medium), accompanied by the\n"
"    Corresponding Source fixed on a durable physical medium\n"
"    customarily used for software interchange.\n"
"\n"
"    b) Convey the object code in, or embodied in, a physical product\n"
"    (including a physical distribution medium), accompanied by a\n"
"    written offer, valid for at least three years and valid for as\n"
"    long as you offer spare parts or customer support for that product\n"
"    model, to give anyone who possesses the object code either (1) a\n"
"    copy of the Corresponding Source for all the software in the\n"
"    product that is covered by this License, on a durable physical\n"
"    medium customarily used for software interchange, for a price no\n"
"    more than your reasonable cost of physically performing this\n"
"    conveying of source, or (2) access to copy the\n"
"    Corresponding Source from a network server at no charge.\n"
"\n"
"    c) Convey individual copies of the object code with a copy of the\n"
"    written offer to provide the Corresponding Source.  This\n"
"    alternative is allowed only occasionally and noncommercially, and\n"
"    only if you received the object code with such an offer, in accord\n"
"    with subsection 6b.\n"
"\n"
"    d) Convey the object code by offering access from a designated\n"
"    place (gratis or for a charge), and offer equivalent access to the\n"
"    Corresponding Source in the same way through the same place at no\n"
"    further charge.  You need not require recipients to copy the\n"
"    Corresponding Source along with the object code.  If the place to\n"
"    copy the object code is a network server, the Corresponding Source\n"
"    may be on a different server (operated by you or a third party)\n"
"    that supports equivalent copying facilities, provided you maintain\n"
"    clear directions next to the object code saying where to find the\n"
"    Corresponding Source.  Regardless of what server hosts the\n"
"    Corresponding Source, you remain obligated to ensure that it is\n"
"    available for as long as needed to satisfy these requirements.\n"
"\n"
"    e) Convey the object code using peer-to-peer transmission, provided\n"
"    you inform other peers where the object code and Corresponding\n"
"    Source of the work are being offered to the general public at no\n"
"    charge under subsection 6d.\n"
"\n"
"  A separable portion of the object code, whose source code is excluded\n"
"from the Corresponding Source as a System Library, need not be\n"
"included in conveying the object code work.\n"
"\n"
"  A \"User Product\" is either (1) a \"consumer product\", which means any\n"
"tangible personal property which is normally used for personal, family,\n"
"or household purposes, or (2) anything designed or sold for incorporation\n"
"into a dwelling.  In determining whether a product is a consumer product,\n"
"doubtful cases shall be resolved in favor of coverage.  For a particular\n"
"product received by a particular user, \"normally used\" refers to a\n"
"typical or common use of that class of product, regardless of the status\n"
"of the particular user or of the way in which the particular user\n"
"actually uses, or expects or is expected to use, the product.  A product\n"
"is a consumer product regardless of whether the product has substantial\n"
"commercial, industrial or non-consumer uses, unless such uses represent\n"
"the only significant mode of use of the product.\n"
"\n"
"  \"Installation Information\" for a User Product means any methods,\n"
"procedures, authorization keys, or other information required to install\n"
"and execute modified versions of a covered work in that User Product from\n"
"a modified version of its Corresponding Source.  The information must\n"
"suffice to ensure that the continued functioning of the modified object\n"
"code is in no case prevented or interfered with solely because\n"
"modification has been made.\n"
"\n"
"  If you convey an object code work under this section in, or with, or\n"
"specifically for use in, a User Product, and the conveying occurs as\n"
"part of a transaction in which the right of possession and use of the\n"
"User Product is transferred to the recipient in perpetuity or for a\n"
"fixed term (regardless of how the transaction is characterized), the\n"
"Corresponding Source conveyed under this section must be accompanied\n"
"by the Installation Information.  But this requirement does not apply\n"
"if neither you nor any third party retains the ability to install\n"
"modified object code on the User Product (for example, the work has\n"
"been installed in ROM).\n"
"\n"
"  The requirement to provide Installation Information does not include a\n"
"requirement to continue to provide support service, warranty, or updates\n"
"for a work that has been modified or installed by the recipient, or for\n"
"the User Product in which it has been modified or installed.  Access to a\n"
"network may be denied when the modification itself materially and\n"
"adversely affects the operation of the network or violates the rules and\n"
"protocols for communication across the network.\n"
"\n"
"  Corresponding Source conveyed, and Installation Information provided,\n"
"in accord with this section must be in a format that is publicly\n"
"documented (and with an implementation available to the public in\n"
"source code form), and must require no special password or key for\n"
"unpacking, reading or copying.\n"
"\n"
"  7. Additional Terms.\n"
"\n"
"  \"Additional permissions\" are terms that supplement the terms of this\n"
"License by making exceptions from one or more of its conditions.\n"
"Additional permissions that are applicable to the entire Program shall\n"
"be treated as though they were included in this License, to the extent\n"
"that they are valid under applicable law.  If additional permissions\n"
"apply only to part of the Program, that part may be used separately\n"
"under those permissions, but the entire Program remains governed by\n"
"this License without regard to the additional permissions.\n"
"\n"
"  When you convey a copy of a covered work, you may at your option\n"
"remove any additional permissions from that copy, or from any part of\n"
"it.  (Additional permissions may be written to require their own\n"
"removal in certain cases when you modify the work.)  You may place\n"
"additional permissions on material, added by you to a covered work,\n"
"for which you have or can give appropriate copyright permission.\n"
"\n"
"  Notwithstanding any other provision of this License, for material you\n"
"add to a covered work, you may (if authorized by the copyright holders of\n"
"that material) supplement the terms of this License with terms:\n"
"\n"
"    a) Disclaiming warranty or limiting liability differently from the\n"
"    terms of sections 15 and 16 of this License; or\n"
"\n"
"    b) Requiring preservation of specified reasonable legal notices or\n"
"    author attributions in that material or in the Appropriate Legal\n"
"    Notices displayed by works containing it; or\n"
"\n"
"    c) Prohibiting misrepresentation of the origin of that material, or\n"
"    requiring that modified versions of such material be marked in\n"
"    reasonable ways as different from the original version; or\n"
"\n"
"    d) Limiting the use for publicity purposes of names of licensors or\n"
"    authors of the material; or\n"
"\n"
"    e) Declining to grant rights under trademark law for use of some\n"
"    trade names, trademarks, or service marks; or\n"
"\n"
"    f) Requiring indemnification of licensors and authors of that\n"
"    material by anyone who conveys the material (or modified versions of\n"
"    it) with contractual assumptions of liability to the recipient, for\n"
"    any liability that these contractual assumptions directly impose on\n"
"    those licensors and authors.\n"
"\n"
"  All other non-permissive additional terms are considered \"further\n"
"restrictions\" within the meaning of section 10.  If the Program as you\n"
"received it, or any part of it, contains a notice stating that it is\n"
"governed by this License along with a term that is a further\n"
"restriction, you may remove that term.  If a license document contains\n"
"a further restriction but permits relicensing or conveying under this\n"
"License, you may add to a covered work material governed by the terms\n"
"of that license document, provided that the further restriction does\n"
"not survive such relicensing or conveying.\n"
"\n"
"  If you add terms to a covered work in accord with this section, you\n"
"must place, in the relevant source files, a statement of the\n"
"additional terms that apply to those files, or a notice indicating\n"
"where to find the applicable terms.\n"
"\n"
"  Additional terms, permissive or non-permissive, may be stated in the\n"
"form of a separately written license, or stated as exceptions;\n"
"the above requirements apply either way.\n"
"\n"
"  8. Termination.\n"
"\n"
"  You may not propagate or modify a covered work except as expressly\n"
"provided under this License.  Any attempt otherwise to propagate or\n"
"modify it is void, and will automatically terminate your rights under\n"
"this License (including any patent licenses granted under the third\n"
"paragraph of section 11).\n"
"\n"
"  However, if you cease all violation of this License, then your\n"
"license from a particular copyright holder is reinstated (a)\n"
"provisionally, unless and until the copyright holder explicitly and\n"
"finally terminates your license, and (b) permanently, if the copyright\n"
"holder fails to notify you of the violation by some reasonable means\n"
"prior to 60 days after the cessation.\n"
"\n"
"  Moreover, your license from a particular copyright holder is\n"
"reinstated permanently if the copyright holder notifies you of the\n"
"violation by some reasonable means, this is the first time you have\n"
"received notice of violation of this License (for any work) from that\n"
"copyright holder, and you cure the violation prior to 30 days after\n"
"your receipt of the notice.\n"
"\n"
"  Termination of your rights under this section does not terminate the\n"
"licenses of parties who have received copies or rights from you under\n"
"this License.  If your rights have been terminated and not permanently\n"
"reinstated, you do not qualify to receive new licenses for the same\n"
"material under section 10.\n"
"\n"
"  9. Acceptance Not Required for Having Copies.\n"
"\n"
"  You are not required to accept this License in order to receive or\n"
"run a copy of the Program.  Ancillary propagation of a covered work\n"
"occurring solely as a consequence of using peer-to-peer transmission\n"
"to receive a copy likewise does not require acceptance.  However,\n"
"nothing other than this License grants you permission to propagate or\n"
"modify any covered work.  These actions infringe copyright if you do\n"
"not accept this License.  Therefore, by modifying or propagating a\n"
"covered work, you indicate your acceptance of this License to do so.\n"
"\n"
"  10. Automatic Licensing of Downstream Recipients.\n"
"\n"
"  Each time you convey a covered work, the recipient automatically\n"
"receives a license from the original licensors, to run, modify and\n"
"propagate that work, subject to this License.  You are not responsible\n"
"for enforcing compliance by third parties with this License.\n"
"\n"
"  An \"entity transaction\" is a transaction transferring control of an\n"
"organization, or substantially all assets of one, or subdividing an\n"
"organization, or merging organizations.  If propagation of a covered\n"
"work results from an entity transaction, each party to that\n"
"transaction who receives a copy of the work also receives whatever\n"
"licenses to the work the party\'s predecessor in interest had or could\n"
"give under the previous paragraph, plus a right to possession of the\n"
"Corresponding Source of the work from the predecessor in interest, if\n"
"the predecessor has it or can get it with reasonable efforts.\n"
"\n"
"  You may not impose any further restrictions on the exercise of the\n"
"rights granted or affirmed under this License.  For example, you may\n"
"not impose a license fee, royalty, or other charge for exercise of\n"
"rights granted under this License, and you may not initiate litigation\n"
"(including a cross-claim or counterclaim in a lawsuit) alleging that\n"
"any patent claim is infringed by making, using, selling, offering for\n"
"sale, or importing the Program or any portion of it.\n"
"\n"
"  11. Patents.\n"
"\n"
"  A \"contributor\" is a copyright holder who authorizes use under this\n"
"License of the Program or a work on which the Program is based.  The\n"
"work thus licensed is called the contributor\'s \"contributor version\".\n"
"\n"
"  A contributor\'s \"essential patent claims\" are all patent claims\n"
"owned or controlled by the contributor, whether already acquired or\n"
"hereafter acquired, that would be infringed by some manner, permitted\n"
"by this License, of making, using, or selling its contributor version,\n"
"but do not include claims that would be infringed only as a\n"
"consequence of further modification of the contributor version.  For\n"
"purposes of this definition, \"control\" includes the right to grant\n"
"patent sublicenses in a manner consistent with the requirements of\n"
"this License.\n"
"\n"
"  Each contributor grants you a non-exclusive, worldwide, royalty-free\n"
"patent license under the contributor\'s essential patent claims, to\n"
"make, use, sell, offer for sale, import and otherwise run, modify and\n"
"propagate the contents of its contributor version.\n"
"\n"
"  In the following three paragraphs, a \"patent license\" is any express\n"
"agreement or commitment, however denominated, not to enforce a patent\n"
"(such as an express permission to practice a patent or covenant not to\n"
"sue for patent infringement).  To \"grant\" such a patent license to a\n"
"party means to make such an agreement or commitment not to enforce a\n"
"patent against the party.\n"
"\n"
"  If you convey a covered work, knowingly relying on a patent license,\n"
"and the Corresponding Source of the work is not available for anyone\n"
"to copy, free of charge and under the terms of this License, through a\n"
"publicly available network server or other readily accessible means,\n"
"then you must either (1) cause the Corresponding Source to be so\n"
"available, or (2) arrange to deprive yourself of the benefit of the\n"
"patent license for this particular work, or (3) arrange, in a manner\n"
"consistent with the requirements of this License, to extend the patent\n"
"license to downstream recipients.  \"Knowingly relying\" means you have\n"
"actual knowledge that, but for the patent license, your conveying the\n"
"covered work in a country, or your recipient\'s use of the covered work\n"
"in a country, would infringe one or more identifiable patents in that\n"
"country that you have reason to believe are valid.\n"
"\n"
"  If, pursuant to or in connection with a single transaction or\n"
"arrangement, you convey, or propagate by procuring conveyance of, a\n"
"covered work, and grant a patent license to some of the parties\n"
"receiving the covered work authorizing them to use, propagate, modify\n"
"or convey a specific copy of the covered work, then the patent license\n"
"you grant is automatically extended to all recipients of the covered\n"
"work and works based on it.\n"
"\n"
"  A patent license is \"discriminatory\" if it does not include within\n"
"the scope of its coverage, prohibits the exercise of, or is\n"
"conditioned on the non-exercise of one or more of the rights that are\n"
"specifically granted under this License.  You may not convey a covered\n"
"work if you are a party to an arrangement with a third party that is\n"
"in the business of distributing software, under which you make payment\n"
"to the third party based on the extent of your activity of conveying\n"
"the work, and under which the third party grants, to any of the\n"
"parties who would receive the covered work from you, a discriminatory\n"
"patent license (a) in connection with copies of the covered work\n"
"conveyed by you (or copies made from those copies), or (b) primarily\n"
"for and in connection with specific products or compilations that\n"
"contain the covered work, unless you entered into that arrangement,\n"
"or that patent license was granted, prior to 28 March 2007.\n"
"\n"
"  Nothing in this License shall be construed as excluding or limiting\n"
"any implied license or other defenses to infringement that may\n"
"otherwise be available to you under applicable patent law.\n"
"\n"
"  12. No Surrender of Others\' Freedom.\n"
"\n"
"  If conditions are imposed on you (whether by court order, agreement or\n"
"otherwise) that contradict the conditions of this License, they do not\n"
"excuse you from the conditions of this License.  If you cannot convey a\n"
"covered work so as to satisfy simultaneously your obligations under this\n"
"License and any other pertinent obligations, then as a consequence you may\n"
"not convey it at all.  For example, if you agree to terms that obligate you\n"
"to collect a royalty for further conveying from those to whom you convey\n"
"the Program, the only way you could satisfy both those terms and this\n"
"License would be to refrain entirely from conveying the Program.\n"
"\n"
"  13. Use with the GNU Affero General Public License.\n"
"\n"
"  Notwithstanding any other provision of this License, you have\n"
"permission to link or combine any covered work with a work licensed\n"
"under version 3 of the GNU Affero General Public License into a single\n"
"combined work, and to convey the resulting work.  The terms of this\n"
"License will continue to apply to the part which is the covered work,\n"
"but the special requirements of the GNU Affero General Public License,\n"
"section 13, concerning interaction through a network will apply to the\n"
"combination as such.\n"
"\n"
"  14. Revised Versions of this License.\n"
"\n"
"  The Free Software Foundation may publish revised and/or new versions of\n"
"the GNU General Public License from time to time.  Such new versions will\n"
"be similar in spirit to the present version, but may differ in detail to\n"
"address new problems or concerns.\n"
"\n"
"  Each version is given a distinguishing version number.  If the\n"
"Program specifies that a certain numbered version of the GNU General\n"
"Public License \"or any later version\" applies to it, you have the\n"
"option of following the terms and conditions either of that numbered\n"
"version or of any later version published by the Free Software\n"
"Foundation.  If the Program does not specify a version number of the\n"
"GNU General Public License, you may choose any version ever published\n"
"by the Free Software Foundation.\n"
"\n"
"  If the Program specifies that a proxy can decide which future\n"
"versions of the GNU General Public License can be used, that proxy\'s\n"
"public statement of acceptance of a version permanently authorizes you\n"
"to choose that version for the Program.\n"
"\n"
"  Later license versions may give you additional or different\n"
"permissions.  However, no additional obligations are imposed on any\n"
"author or copyright holder as a result of your choosing to follow a\n"
"later version.\n"
"\n"
"  15. Disclaimer of Warranty.\n"
"\n"
"  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY\n"
"APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT\n"
"HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM \"AS IS\" WITHOUT WARRANTY\n"
"OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,\n"
"THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR\n"
"PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM\n"
"IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF\n"
"ALL NECESSARY SERVICING, REPAIR OR CORRECTION.\n"
"\n"
"  16. Limitation of Liability.\n"
"\n"
"  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING\n"
"WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS\n"
"THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY\n"
"GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE\n"
"USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF\n"
"DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD\n"
"PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),\n"
"EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF\n"
"SUCH DAMAGES.\n"
"\n"
"  17. Interpretation of Sections 15 and 16.\n"
"\n"
"  If the disclaimer of warranty and limitation of liability provided\n"
"above cannot be given local legal effect according to their terms,\n"
"reviewing courts shall apply local law that most closely approximates\n"
"an absolute waiver of all civil liability in connection with the\n"
"Program, unless a warranty or assumption of liability accompanies a\n"
"copy of the Program in return for a fee.\n"
"\n"
"                     END OF TERMS AND CONDITIONS\n"
"\n"
"            How to Apply These Terms to Your New Programs\n"
"\n"
"  If you develop a new program, and you want it to be of the greatest\n"
"possible use to the public, the best way to achieve this is to make it\n"
"free software which everyone can redistribute and change under these terms.\n"
"\n"
"  To do so, attach the following notices to the program.  It is safest\n"
"to attach them to the start of each source file to most effectively\n"
"state the exclusion of warranty; and each file should have at least\n"
"the \"copyright\" line and a pointer to where the full notice is found.\n"
"\n"
"    <one line to give the program\'s name and a brief idea of what it does.>\n"
"    Copyright (C) <year>  <name of author>\n"
"\n"
"    This program is free software: you can redistribute it and/or modify\n"
"    it under the terms of the GNU General Public License as published by\n"
"    the Free Software Foundation, either version 3 of the License, or\n"
"    (at your option) any later version.\n"
"\n"
"    This program is distributed in the hope that it will be useful,\n"
"    but WITHOUT ANY WARRANTY; without even the implied warranty of\n"
"    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n"
"    GNU General Public License for more details.\n"
"\n"
"    You should have received a copy of the GNU General Public License\n"
"    along with this program.  If not, see <https://www.gnu.org/licenses/>.\n"
"\n"
"Also add information on how to contact you by electronic and paper mail.\n"
"\n"
"  If the program does terminal interaction, make it output a short\n"
"notice like this when it starts in an interactive mode:\n"
"\n"
"    <program>  Copyright (C) <year>  <name of author>\n"
"    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w\'.\n"
"    This is free software, and you are welcome to redistribute it\n"
"    under certain conditions; type `show c\' for details.\n"
"\n"
"The hypothetical commands `show w\' and `show c\' should show the appropriate\n"
"parts of the General Public License.  Of course, your program\'s commands\n"
"might be different; for a GUI interface, you would use an \"about box\".\n"
"\n"
"  You should also get your employer (if you work as a programmer) or school,\n"
"if any, to sign a \"copyright disclaimer\" for the program, if necessary.\n"
"For more information on this, and how to apply and follow the GNU GPL, see\n"
"<https://www.gnu.org/licenses/>.\n"
"\n"
"  The GNU General Public License does not permit incorporating your program\n"
"into proprietary programs.  If your program is a subroutine library, you\n"
"may consider it more useful to permit linking proprietary applications with\n"
"the library.  If this is what you want to do, use the GNU Lesser General\n"
"Public License instead of this License.  But first, please read\n"
"<https://www.gnu.org/licenses/why-not-lgpl.html>.\n"
""))
        self.wizardPage3.setTitle(_translate("BlackPackWizard", "Create RPM packages easy"))
        self.wizardPage3.setSubTitle(_translate("BlackPackWizard", "Build scripts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BlackPackWizard", "%prep"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("BlackPackWizard", "%build"))
        self.plainTextEdit_3.setPlainText(_translate("BlackPackWizard", "mkdir -p %{buildroot}/\n"
"cp -r ./* %buildroot/"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("BlackPackWizard", "%install"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("BlackPackWizard", "%check"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("BlackPackWizard", "%changelog"))
        self.wizardPage4.setTitle(_translate("BlackPackWizard", "Create RPM packages easy"))
        self.wizardPage4.setSubTitle(_translate("BlackPackWizard", "RPM install scripts"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("BlackPackWizard", "%post"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("BlackPackWizard", "%pre"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), _translate("BlackPackWizard", "%preun"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_14), _translate("BlackPackWizard", "%postun"))
        self.wizardPage6.setTitle(_translate("BlackPackWizard", "Create RPM packages easy"))
        self.wizardPage6.setSubTitle(_translate("BlackPackWizard", "Files"))
        self.pushButton_9.setText(_translate("BlackPackWizard", "Add folder"))
        self.groupBox_2.setTitle(_translate("BlackPackWizard", "Select file from disk"))
        self.lineEdit.setPlaceholderText(_translate("BlackPackWizard", "/path/to/file.txt or dierctory"))
        self.pushButton.setText(_translate("BlackPackWizard", "Browse for files ..."))
        self.pushButton_8.setText(_translate("BlackPackWizard", "Browse for directories ..."))
        self.groupBox.setTitle(_translate("BlackPackWizard", "Install file to:"))
        self.label_15.setText(_translate("BlackPackWizard", "Rename:"))
        self.comboBox_2.setItemText(0, _translate("BlackPackWizard", "/usr/bin/"))
        self.comboBox_2.setItemText(1, _translate("BlackPackWizard", "/usr/share/<package_name>/"))
        self.comboBox_2.setItemText(2, _translate("BlackPackWizard", "/usr/share/"))
        self.comboBox_2.setItemText(3, _translate("BlackPackWizard", "/usr/share/applications/"))
        self.comboBox_2.setItemText(4, _translate("BlackPackWizard", "/usr/share/pixmaps/"))
        self.lineEdit_2.setPlaceholderText(_translate("BlackPackWizard", "/usr/bin/myprogram"))
        self.pushButton_3.setText(_translate("BlackPackWizard", "Remove file"))
        self.pushButton_2.setText(_translate("BlackPackWizard", "Add file"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BlackPackWizard", "From:"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BlackPackWizard", "Unpack to:"))
        self.pushButton_4.setText(_translate("BlackPackWizard", "Clean all"))
        self.wizardPage7.setTitle(_translate("BlackPackWizard", "Create RPM packages easy"))
        self.wizardPage7.setSubTitle(_translate("BlackPackWizard", "Requires"))
        self.groupBox_3.setTitle(_translate("BlackPackWizard", "Add package"))
        self.label_7.setText(_translate("BlackPackWizard", "Package name:"))
        self.label_8.setText(_translate("BlackPackWizard", "Version:"))
        self.lineEdit_4.setPlaceholderText(_translate("BlackPackWizard", "(newest)"))
        self.pushButton_6.setText(_translate("BlackPackWizard", "Add package"))
        self.pushButton_5.setText(_translate("BlackPackWizard", "Remove package"))
        self.pushButton_7.setText(_translate("BlackPackWizard", "Clean all"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("BlackPackWizard", "Package:"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("BlackPackWizard", "Version:"))
        self.wizardPage8.setTitle(_translate("BlackPackWizard", "Create RPM packages easy"))
        self.wizardPage8.setSubTitle(_translate("BlackPackWizard", "Application menu"))
        self.groupBox_5.setTitle(_translate("BlackPackWizard", "Application menu"))
        self.label_6.setText(_translate("BlackPackWizard", "Application name:"))
        self.label_13.setText(_translate("BlackPackWizard", "Icon:"))
        self.pkgversion_2.setPlaceholderText(_translate("BlackPackWizard", "Program icon when installed, /usr/pixmaps/myprogram.png"))
        self.label_10.setText(_translate("BlackPackWizard", "Comment:"))
        self.label_12.setText(_translate("BlackPackWizard", "Exec:"))
        self.pkgsummary_2.setPlaceholderText(_translate("BlackPackWizard", "Program exec when installed, /usr/bin/myprogram"))
        self.label_14.setText(_translate("BlackPackWizard", "Terminal:"))
        self.label_11.setText(_translate("BlackPackWizard", "Categories:"))
        self.groupBox_6.setTitle(_translate("BlackPackWizard", "Other options:"))
