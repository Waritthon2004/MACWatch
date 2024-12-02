from PyQt5 import QtCore, QtGui, QtWidgets

class MacHostTableApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Set the window title and background color
        self.setWindowTitle("Analyser Agent")
        self.setStyleSheet("background-color: #f0f0f0;")
        
        # Create the main layout
        mainLayout = QtWidgets.QVBoxLayout(self)
        
        # Top bar layout
        topBar = QtWidgets.QWidget()
        topBar.setStyleSheet("background-color: #333333; color: white; font-weight: bold;")
        topBarLayout = QtWidgets.QHBoxLayout(topBar)
        topBarLayout.setContentsMargins(10, 5, 10, 5)
        
        titleLabel = QtWidgets.QLabel("Analyser Agent")
        titleLabel.setStyleSheet("font-size: 16px;")
        titleLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        
        profileIcon = QtWidgets.QLabel()
        profileIcon.setPixmap(QtGui.QPixmap("user_icon.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio))
        profileIcon.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        topBarLayout.addWidget(titleLabel)
        topBarLayout.addStretch()
        topBarLayout.addWidget(profileIcon)
        
        mainLayout.addWidget(topBar)
        
        # Title and icon layout
        titleWidget = QtWidgets.QWidget()
        titleLayout = QtWidgets.QHBoxLayout(titleWidget)
        titleLabel = QtWidgets.QLabel("MSU WIFI")
        titleLabel.setStyleSheet("font-size: 20px; font-weight: bold;")
        titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        
        wifiIcon = QtWidgets.QLabel()
        wifiIcon.setPixmap(QtGui.QPixmap("wifi_icon.png").scaled(24, 24, QtCore.Qt.KeepAspectRatio))
        wifiIcon.setAlignment(QtCore.Qt.AlignCenter)
        
        titleLayout.addStretch()
        titleLayout.addWidget(titleLabel)
        titleLayout.addWidget(wifiIcon)
        titleLayout.addStretch()
        
        mainLayout.addWidget(titleWidget)
        
        # Create the table widget
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Mac address", "Host name"])
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: #ADD8E6; font-weight: bold; font-size: 12pt;")
        self.tableWidget.setStyleSheet("QTableWidget::item { background-color: #F0F8FF; }")
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        
        # Add data to the table
        data = [
            ["00:1A:2B:3C:4D:5E", "laptop ruj"],
            ["00:1A:2B:3C:4D:5E", "desktopKong"],
            ["02:42:AC:11:00:02", "phone1"]
        ]
        for row, (mac, host) in enumerate(data):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(mac))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(host))
        
        mainLayout.addWidget(self.tableWidget)
        
        # Add buttons at the bottom
        buttonLayout = QtWidgets.QHBoxLayout()
        
        button1 = QtWidgets.QPushButton("Scan with Algorithm 1")
        button1.setStyleSheet("background-color: #D8BFD8; font-size: 12pt; border-radius: 15px; padding: 5px 10px;")
        buttonLayout.addWidget(button1)
        
        button2 = QtWidgets.QPushButton("Scan with Algorithm 2")
        button2.setStyleSheet("background-color: #87CEEB; font-size: 12pt; border-radius: 15px; padding: 5px 10px;")
        buttonLayout.addWidget(button2)
        
        mainLayout.addLayout(buttonLayout)
        
        # Set window size and layout
        self.resize(600, 400)
        self.setLayout(mainLayout)

# Run the application
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MacHostTableApp()
    window.show()
    sys.exit(app.exec_())
