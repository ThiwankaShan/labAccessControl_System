from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys
from main import *

class formWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(formWindow, self).__init__()
        self.ui = loadUi('GUI/form.ui',self)
        self.ui.show()

        self.submitButton = self.ui.pushButton_ok
        self.submitButton.clicked.connect(self.clickButton_ok)

        self.lineName = self.ui.lineEdit_name
        self.lineID = self.ui.lineEdit_id

        self.labelNameError = self.ui.label_nameError
        self.labelIDError = self.ui.label_idError
        self.labelMessage = self.ui.label_message

    def clickButton_ok(self):
        print('clicked ok button')
        print(f'name : {self.lineName.text()}')
        print(f'id : {self.lineID.text()}')

        name = self.lineName.text()
        id = self.lineID.text()
        validation = self.validate(name,id)
    
    def validate(self,name,id):

        if name != 'shan': 
            self.labelNameError.setText('Invalid Name')
            return False

        if id != '17apc3111':
            self.labelIDError.setText('Invalid id')
            return False
        
        else:
            print('validated')
            self.labelMessage.setText('Sucessfull')
            return True
            


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

    def clickButton_logs(self):
        print("clicked logs")

    def clickButton_reset(self):
        print("clicked reset")
        controlPanel.resetSystem()
    
    def clickButton_onOff(self):
        print("clicked on/off")
    
    def clickButton_users(self):
        print("clicked users")
        formWindow()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    app.exec_()