from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi 

class AuthFormWindow(QtWidgets.QDialog):

    def __init__(self):
        super(AuthFormWindow, self).__init__()
        self.ui = loadUi('GUI/adminAuthForm.ui',self)
        self.ui.show()

        self.submitButton = self.ui.pushButton_ok
        self.submitButton.clicked.connect(self.clickButton_accepted)
        
        self.cancelButton = self.ui.pushButton_cancel
        self.cancelButton.clicked.connect(self.clickButton_rejected)

        self.linePassword = self.ui.lineEdit_password
        self.labelError = self.ui.label_error

    def clickButton_accepted(self):
        pswd = self.linePassword.text()
        if self.validate('admin',pswd):
            self.accept()
        else:
            self.labelError.setText('invalid password')
            
    def clickButton_rejected(self):
        print('rejected')
        self.reject()
    
    def validate(self,name,pswd):
        if pswd == '123':
            return True
        else:
            return False