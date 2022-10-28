from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5 import QtGui
from browserUi import Ui_Form

# ДОДЕЛАТЬ КЛАСС ДЕЙСТВИЯ С ОКНОМ
class Actions(QtWidgets.QWidget):
    def __init__(self):
        super(Actions, self).__init__()
        
class browserApp(Actions, Ui_Form):
    def __init__(self):
        super(browserApp, self).__init__()
        self.setupUi(self)
        # Полнорежимный экран
        self.pushButton_fullscreen.clicked.connect(self.window_show_maximized)
        # Сворачивание окна
        self.pushButton_turn.clicked.connect(self.showMinimized)
        # Выход
        self.pushButton_exit.clicked.connect(sys.exit)
    
    # Метод окна на весь монитор
    def window_show_maximized(self):
        if self.pushButton_fullscreen.isChecked():
            self.showMaximized()
        else:
            self.showNormal()


if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Form = browserApp()
        Form.show()
        sys.exit(app.exec_())
