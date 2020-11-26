from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi 

class AuthFormWindow(QtWidgets.QDialog):

    def __init__(self):
        super(AuthFormWindow, self).__init__()
        self.ui = loadUi('GUI/adminAuthForm.ui',self)
        self.ui.show()

        self.submitButton = self.ui.buttonBox
        self.submitButton.accepted.connect(self.clickButton_accepted)
        self.submitButton.rejected.connect(self.clickButton_rejected)

        self.linePassword = self.ui.lineEdit_password


    def clickButton_accepted(self):
        pswd = self.linePassword.text()
        if self.validate('admin',pswd):
            self.accept()
        else:
            self.reject()

    def clickButton_rejected(self):
        print('rejected')
        self.reject()

    
    def validate(self,name,pswd):
        
        return False