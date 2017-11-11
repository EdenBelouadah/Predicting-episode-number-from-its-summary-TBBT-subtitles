# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(868, 602)
        Dialog.setWhatsThis("")
        Dialog.setSizeGripEnabled(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 781, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.summary_text = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.summary_text.setObjectName("summary_text")
        self.verticalLayout.addWidget(self.summary_text)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.season_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.season_combo_box.setObjectName("season_combo_box")
        self.horizontalLayout_2.addWidget(self.season_combo_box)
        self.load_summary_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_summary_button.setObjectName("load_summary_button")
        self.horizontalLayout_2.addWidget(self.load_summary_button)
        self.run_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.run_button.setObjectName("run_button")
        self.horizontalLayout_2.addWidget(self.run_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.episode_text = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.episode_text.setObjectName("episode_text")
        self.verticalLayout.addWidget(self.episode_text)
        self.clear_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout.addWidget(self.clear_button)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 31, 631, 23))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Finding episode\'s number from it\'s summary-Big Bang Theory subtitles"))
        self.load_summary_button.setText(_translate("Dialog", "Load Summary"))
        self.run_button.setText(_translate("Dialog", "Run"))
        self.label.setText(_translate("Dialog", "The episode is:"))
        self.clear_button.setText(_translate("Dialog", "Clear"))
        self.label_2.setText(_translate("Dialog", "Please choose a season, Load a summary then press the \"Run\" button:"))

