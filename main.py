import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 550)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget#widget{\n"
"    border:4px solid rgb(45,45,45);\n"
"    border-radius: 20px;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setEnabled(True)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"    background-color:rgb(20,20,20);\n"
"    border-top-left-radius:20px;\n"
"    border-top-left-radius:20px;\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(0,0,0);\n"
"    color:rgb(255,255,255);\n"
"    font:bold;\n"
"    font-size:15px;\n"
"    font-family:entypo;\n"
"    background:transparent\n"
"    }\n"
"QPushButton:hover{\n"
"    color:rgb(255, 73, 76)\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"color:rgb(91,88,53);\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setMinimumSize(QtCore.QSize(15, 15))
        self.label_7.setMaximumSize(QtCore.QSize(15, 15))
        self.label_7.setStyleSheet("background-color:rgb(255, 0, 4);\n"
"border-radius:7px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setMinimumSize(QtCore.QSize(15, 15))
        self.label_6.setMaximumSize(QtCore.QSize(15, 15))
        self.label_6.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:1px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(15, 15))
        self.label_5.setMaximumSize(QtCore.QSize(15, 15))
        font = QtGui.QFont()
        font.setFamily("entypo")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:rgb(0,0,0);\n"
"color:rgb(0, 255, 127);\n"
"font:bold;\n"
"font-size:30px;\n"
"font-family:entypo;\n"
"background:transparent")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(144,144,144);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.pushButton_turn = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_turn.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_turn.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("entypo")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_turn.setFont(font)
        self.pushButton_turn.setStyleSheet("")
        self.pushButton_turn.setObjectName("pushButton_turn")
        self.horizontalLayout.addWidget(self.pushButton_turn)
        self.pushButton_fullscreen = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_fullscreen.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_fullscreen.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_fullscreen.setCheckable(True)
        self.pushButton_fullscreen.setObjectName("pushButton_fullscreen")
        self.horizontalLayout.addWidget(self.pushButton_fullscreen)
        self.pushButton_exit = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_back = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_back.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_back.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout_2.addWidget(self.pushButton_back)
        self.pushButton_forward = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_forward.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_forward.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_forward.setObjectName("pushButton_forward")
        self.horizontalLayout_2.addWidget(self.pushButton_forward)
        self.pushButton_update = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_update.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_update.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_2.addWidget(self.pushButton_update)
        self.pushButton_settings = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_settings.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.horizontalLayout_2.addWidget(self.pushButton_settings)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setStyleSheet("background-color:rgb(31,31,31);\n"
"border-radius:5px;\n"
"color:rgb(144,144,144);\n"
"padding-left:5x;\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_enter = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_enter.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_enter.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.horizontalLayout_2.addWidget(self.pushButton_enter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setStyleSheet("background-color:rgb(67, 67, 67)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 45))
        self.label.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label.setStyleSheet("background-color:rgb(67, 67, 67);\n"
"border-bottom-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"color:rgb(144,144,144);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "▴"))
        self.label_3.setText(_translate("Form", "Shape Browser"))
        self.pushButton_turn.setText(_translate("Form", "-"))
        self.pushButton_fullscreen.setText(_translate("Form", ""))
        self.pushButton_exit.setText(_translate("Form", "X"))
        self.pushButton_back.setText(_translate("Form", "⬅"))
        self.pushButton_forward.setText(_translate("Form", "➡"))
        self.pushButton_update.setText(_translate("Form", "⟳"))
        self.pushButton_settings.setText(_translate("Form", "⚙"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Введите поисковый запрос или адрес"))
        self.pushButton_enter.setText(_translate("Form", "↳"))
        self.label.setText(_translate("Form", "Developed by Queeenace"))

class WebPage(QtWidgets.QTabWidget, Ui_Form):
    clicked = QtCore.pyqtSignal(int)
    def __init__(self, parent = None):
        super(WebPage, self).__init__(parent = parent)
        self.setupUi(self)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QTabWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())