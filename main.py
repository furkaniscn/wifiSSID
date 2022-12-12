from PyQt5 import QtWidgets
from furkan import Ui_MainWindow
import sys
import SSID

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.kaydet.clicked.connect(self.kaydet)
    
    def kaydet(self):
        SSID.fonk()
        QtWidgets.QMessageBox.about(self,"","Kaydedildi")    

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())

app()





