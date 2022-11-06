from PyQt5 import QtWidgets, QtCore, QtWebEngine, QtWebEngineCore
import sys
from PyQt5 import QtGui
from browser_ui import Ui


class Browser(QtWidgets.QWidget,Ui):
    def __init__(self):
        super(Browser, self).__init__()
        self.setupUi(self)
        # Полнорежимный экран
        self.pushButton_fullscreen.clicked.connect(self.window_show_maximized)
        # Сворачивание окна
        self.pushButton_turn.clicked.connect(self.showMinimized)
        # Выход
        self.pushButton_exit.clicked.connect(sys.exit)
        # Загрузка url нажатием на Enter
        self.lineEdit.returnPressed.connect(self.load)
        # Загрузка url нажатием на кнопку
        self.pushButton_enter.clicked.connect(self.load)
        # Обновление страницы
        self.pushButton_update.clicked.connect(self.reload)
        # Кнопка назад
        self.pushButton_back.clicked.connect(self.back)
        # Кнопка вперед
        self.pushButton_forward.clicked.connect(self.forward)
    
    # Метод окна на весь монитор
    def window_show_maximized(self):
        if self.pushButton_fullscreen.isChecked():
            self.showMaximized() 
        else:
            self.showNormal()
    
    # Сохраняет место щелчка по окну
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    # Перемещние окна между точкой щелчка и текущим положением мыши
    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
    # Загрузка url
    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)
    
    # Обновление страницы
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)
    
    # Кнопка вперед
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)
    
    # Кнопка назад
    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)




if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Form = Browser()
        Form.show()
        sys.exit(app.exec_())
