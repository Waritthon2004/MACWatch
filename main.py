from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1103, 809)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setAutoFillBackground(False)
        
        # Top black header
        self.header = QtWidgets.QWidget(Form)
        self.header.setGeometry(QtCore.QRect(0, 0, 1103, 80))
        self.header.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        # Header title
        self.headerLabel = QtWidgets.QLabel(self.header)
        self.headerLabel.setGeometry(QtCore.QRect(20, 20, 300, 40))
        self.headerLabel.setText("Analyser Agent")
        self.headerLabel.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        
        # User icon in header
        self.userIcon = QtWidgets.QLabel(self.header)
        self.userIcon.setGeometry(QtCore.QRect(1020, 15, 50, 50))
        self.userIcon.setStyleSheet("""
            background-color: #444;
            border-radius: 25px;
        """)
        
        # Left sidebar
        self.sidebar = QtWidgets.QWidget(Form)
        self.sidebar.setGeometry(QtCore.QRect(0, 80, 80, 729))
        self.sidebar.setStyleSheet("background-color: rgb(240, 240, 240);")
        
        # Sidebar buttons
        self.agentButton = QtWidgets.QPushButton(self.sidebar)
        self.agentButton.setGeometry(QtCore.QRect(15, 20, 50, 50))
        self.agentButton.setStyleSheet("""
            QPushButton {
                background-color: #333;
                border-radius: 25px;
            }
        """)
        
        self.addButton = QtWidgets.QPushButton(self.sidebar)
        self.addButton.setGeometry(QtCore.QRect(15, 90, 50, 50))
        self.addButton.setText("+")
        self.addButton.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid #ccc;
                border-radius: 25px;
                font-size: 24px;
            }
        """)
        
        # Main content
        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setGeometry(QtCore.QRect(450, 100, 200, 50))
        self.titleLabel.setText("MSU WIFI")
        self.titleLabel.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        # WiFi icon
        self.wifiIcon = QtWidgets.QLabel(Form)
        self.wifiIcon.setGeometry(QtCore.QRect(650, 100, 50, 50))
        
        # Table - Updated geometry and column widths
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(100, 180, 950, 400))  # Increased width
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Mac Address", "IP Address", "Hostname"])
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #e6f3ff;
                padding: 10px;
                border: none;
            }
        """)
        
        # Updated column widths to fit the table without scrolling
        self.tableWidget.setColumnWidth(0, 305)  # MAC address
        self.tableWidget.setColumnWidth(1, 305)  # IP Address
        self.tableWidget.setColumnWidth(2, 305)  # Hostname
        
        # Disable scrollbars
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        # Add sample data
        self.tableWidget.setRowCount(3)
        sample_data = [
            ("00:1A:2B:3C:4D:5E", "192.168.7.65", "laptop mj"),
            ("00:1A:2B:3C:4D:5E", "192.168.7.65", "desktopKong"),
            ("02:42:AC:11:00:02", "192.168.7.66", "phone1")
        ]
        for i, (mac, ip, host) in enumerate(sample_data):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(mac))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(ip))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(host))
        
        # Buttons
        self.scanButton1 = QtWidgets.QPushButton(Form)
        self.scanButton1.setGeometry(QtCore.QRect(150, 650, 250, 60))
        self.scanButton1.setText("Scan with Algorithm 1")
        self.scanButton1.setStyleSheet("""
            QPushButton {
                background-color: rgb(239, 159, 239);
                border-radius: 30px;
                font-size: 16px;
            }
        """)
        
        self.scanButton2 = QtWidgets.QPushButton(Form)
        self.scanButton2.setGeometry(QtCore.QRect(700, 650, 250, 60))
        self.scanButton2.setText("Scan with Algorithm 2")
        self.scanButton2.setStyleSheet("""
            QPushButton {
                background-color: rgb(0, 209, 209);
                border-radius: 30px;
                font-size: 16px;
            }
        """)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())