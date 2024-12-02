from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1126, 858)  # Set to specified size
        
        # Main window background
        Form.setStyleSheet("background-color: white;")
        
        # Top header widget - full width
        self.header = QtWidgets.QWidget(Form)
        self.header.setGeometry(QtCore.QRect(0, 0, 1126, 80))
        self.header.setStyleSheet("background-color: rgb(51, 51, 51);")
        
        # MACWatch title
        self.title = QtWidgets.QLabel(self.header)
        self.title.setGeometry(QtCore.QRect(30, 15, 231, 51))
        self.title.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        self.title.setText("MACWatch")
        
        # User icon (top right)
        self.userIcon = QtWidgets.QPushButton(self.header)
        self.userIcon.setGeometry(QtCore.QRect(1066, 20, 30, 30))
        self.userIcon.setStyleSheet("""
            QPushButton {
                background-color: #666;
                border-radius: 15px;
                color: white;
            }
        """)
        self.userIcon.setText("👤")
        
        # Left sidebar - full height
        self.sidebar = QtWidgets.QWidget(Form)
        self.sidebar.setGeometry(QtCore.QRect(0, 80, 120, 778))
        self.sidebar.setStyleSheet("background-color: rgb(240, 240, 240);")
        
        # Add button in sidebar
        # Add button in sidebar (circular)
        self.addButton = QtWidgets.QPushButton(self.sidebar)
        self.addButton.setGeometry(QtCore.QRect(30, 40, 60, 60))  # ตั้งความกว้างและความสูงเท่ากัน (50x50)
        self.addButton.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid #ccc;
                border-radius: 25px;    
                font-size: 20px;
                font-weight: bold;
                text-align: center;      
                line-height: 50px;       
            }
            QPushButton:hover {
                background-color: #f0f0f0;  
            }
        """)
        self.addButton.setText("+")
        
        # Main content area
        self.content = QtWidgets.QWidget(Form)
        self.content.setGeometry(QtCore.QRect(250, 110, 691, 651))
        
        # Add MACWatch title
        self.addTitle = QtWidgets.QLabel(self.content)
        self.addTitle.setGeometry(QtCore.QRect(230, 10, 181, 51))
        self.addTitle.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.addTitle.setText("Add MACWatch")
        
        # Form fields with adjusted positions
        # Name field
        self.nameLabel = QtWidgets.QLabel(self.content)
        self.nameLabel.setGeometry(QtCore.QRect(170, 120, 151, 21))
        self.nameLabel.setStyleSheet("font-size: 14px;")
        self.nameLabel.setText("Name MACWatch")
        
        self.nameInput = QtWidgets.QLineEdit(self.content)
        self.nameInput.setGeometry(QtCore.QRect(170, 150, 311, 41))
        self.nameInput.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        
        # Authentication Key field
        self.authLabel = QtWidgets.QLabel(self.content)
        self.authLabel.setGeometry(QtCore.QRect(170, 220, 151, 21))
        self.authLabel.setStyleSheet("font-size: 14px;")
        self.authLabel.setText("Authentication Key")
        
        self.authInput = QtWidgets.QLineEdit(self.content)
        self.authInput.setGeometry(QtCore.QRect(170, 250, 311, 41))
        self.authInput.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        
        # Description field
        self.descLabel = QtWidgets.QLabel(self.content)
        self.descLabel.setGeometry(QtCore.QRect(170, 330, 151, 21))
        self.descLabel.setStyleSheet("font-size: 14px;")
        self.descLabel.setText("Description")
        
        self.descInput = QtWidgets.QLineEdit(self.content)
        self.descInput.setGeometry(QtCore.QRect(170, 360, 311, 41))
        self.descInput.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        
        # IP field
        self.ipLabel = QtWidgets.QLabel(self.content)
        self.ipLabel.setGeometry(QtCore.QRect(170, 440, 151, 21))
        self.ipLabel.setStyleSheet("font-size: 14px;")
        self.ipLabel.setText("IP")
        
        self.ipInput = QtWidgets.QLineEdit(self.content)
        self.ipInput.setGeometry(QtCore.QRect(170, 470, 311, 41))
        self.ipInput.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        
        # Submit button
        self.submitButton = QtWidgets.QPushButton(self.content)
        self.submitButton.setGeometry(QtCore.QRect(260, 580, 93, 28))
        self.submitButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(51, 51, 51);
                color: white;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: rgb(75, 75, 75);
            }
            QPushButton:pressed {
                background-color: rgb(40, 40, 40);
            }
        """)
        self.submitButton.setText("SUBMIT")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())