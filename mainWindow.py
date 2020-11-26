from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi 
from formWindow import FormWindow
from controlPanel import ControlPanel   
import sys


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = loadUi('GUI/dashboard.ui',self)

        self.logButton = self.ui.pushButton_logs
        self.logButton.clicked.connect(self.clickButton_logs)

        self.resetButton = self.ui.pushButton_reset
        self.resetButton.clicked.connect(self.clickButton_reset)

        self.onOffButton = self.ui.pushButton_onOff
        self.onOffButton.clicked.connect(self.clickButton_onOff)

        self.usersButton = self.ui.pushButton_users
        self.usersButton.clicked.connect(self.clickButton_users)

        self.emergencyButton = self.ui.pushButton_EmergencyMode
        self.emergencyButton.clicked.connect(self.clickButton_emergency)

        self.manualOpenButton = self.ui.pushButton_manualOpen
        self.manualOpenButton.clicked.connect(self.clickButton_ManuallyOpen)

        self.manualCloseButton = self.ui.pushButton_manualClose
        self.manualCloseButton.clicked.connect(self.clickButton_ManuallyClose)

        self.labelStatus = self.ui.label_status

    def clickButton_logs(self):
        print("clicked logs")

    def clickButton_reset(self):
        print("clicked reset")
        ControlPanel.resetSystem()
    
    def clickButton_onOff(self):
        print("clicked on/off")
        ControlPanel.start()
    
    def clickButton_emergency(self):
        print(f"clicked emergency")

    def clickButton_ManuallyOpen(self):
        print(f"clicked manually open")
        self.entrances.cardScanner.ardunioSerial.write('open'.encode())
    
    def clickButton_ManuallyClose(self):
        print(f"clicked manually close")
        self.entrances.cardScanner.ardunioSerial.write('close'.encode())
    
    def clickButton_users(self):
        print("clicked users")
        FormWindow()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    app.exec_()