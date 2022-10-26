import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget,QMainWindow
from PyQt5.QtGui import QImage,QMovie
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


from ui_main_window import *

class MainWindow(QMainWindow):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
