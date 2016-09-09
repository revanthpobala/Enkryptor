import sys
from PyQt4.Qt import QWidget, QLabel, QPixmap
from PyQt4 import QtGui as qt
from encryption import encrypt_folder, decrypt_folder
import os
from PyQt4.QtGui import QSizePolicy

class FrontEnd(QWidget):
    def __init__(self, parent=None):
        super(FrontEnd, self).__init__(parent)
        self.setSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Header image.. Need to get a Quality image
        self.hlabel = QLabel()
        self.hpixmap = QPixmap(os.curdir()+'images\header.png')
        self.hlabel.setPixmap(self.hpixmap) 
        #self.hlabel.setMaximumWidth(400)
        
        # Password Stuff
        self._password = qt.QLabel('Please Provide a Password')
        self._passwordEdit = qt.QLineEdit()
        self._passwordEdit.setMaximumWidth(500)
        self._passwordEdit.setText("Password")
        self._passwordEdit.setEchoMode(qt.QLineEdit.Password)
        self._passwordEdit.setMaximumWidth(400)
       
        # Get the folder path 
        self._path = qt.QLabel("Please Provide a Path")
        self._path.setMaximumWidth(500)
        self._pathEdit = qt.QLineEdit()
        self._pathEdit.setText("/home or C:\\")
        self._pathEdit.setMaximumWidth(400)
        
        
        # Encrypt Button
        self._encryptButton = qt.QPushButton("Encrypt")
        self._encryptButton.clicked.connect(self.encryptFolder)
        #self._encryptButton.setStyleSheet("background-color: #79ff4d")
        self._encryptButton.setMaximumWidth(400)
        
        # Decrypt Button
        self._decryptButton = qt.QPushButton("Decrypt")
        self._decryptButton.clicked.connect(self.decryptFolder)
        #self._decryptButton.setStyleSheet("background-color: #ff4d4d")
        self._decryptButton.setMaximumWidth(400)
        
        
        # Footer Need to get a Quality image
        self.flabel = QLabel()
        self.fpixmap = QPixmap(os.curdir+'/images/footer.png')
        self.flabel.setPixmap(self.fpixmap) 
        
        
        
        
        # Add widgets to the grid
        self.widget = QWidget()
        self.grid = qt.QGridLayout(self.widget)
        self.grid.setSpacing(10)
        self.grid.maximumSize()
        self.grid.addWidget(self.hlabel,0,0)
        self.grid.addWidget(self._password,1,0)
        self.grid.addWidget(self._passwordEdit,2,0)
        self.grid.addWidget(self._path,3,0)
        self.grid.addWidget(self._pathEdit,4,0)
        self.grid.addWidget(self._encryptButton,5,0)
        self.grid.addWidget(self._decryptButton,6,0)
        self.grid.addWidget(self.flabel,7,0)
        
        
        self.setLayout(self.grid)
       
       
        
        self.setGeometry(350,300,350,300)
        self.setWindowTitle("Enkryptor- Keeps your files safe")
        self.show()
    
    """
        Slot functions.
    """
        
    def getPasswordData(self):
        self._passwordEdit.text()
        
    def getPathData(self):
        self._pathEdit.text()
    
    def encryptFolder(self):
        password =  str(self._passwordEdit.text())
        folder_path = str(self._pathEdit.text())
        encrypt_folder(folder_path, password)
        
    def decryptFolder(self):
        password =  str(self._passwordEdit.text())
        folder_path = str(self._pathEdit.text())
        decrypt_folder(folder_path, password)
    
        
def main():
        app = qt.QApplication(sys.argv)
        FE = FrontEnd()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()

