from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi 

class FormWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(FormWindow, self).__init__()
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

        name = self.lineName.text()
        id = self.lineID.text()
        validation = self.validate(name,id)

        if validation:
            controlPanel.create_user(name,id)
    
    def validate(self,name,id):
        
        return True