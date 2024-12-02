# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1126, 858)  # Set to specified size
        Form.setWindowTitle("MACWatch")
        Form.setStyleSheet("background-color: white;")
        
        # Main Layout
        self.central_layout = QtWidgets.QVBoxLayout(Form)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)
        
        # Top Header Bar
        self.header = QtWidgets.QWidget()
        self.header.setStyleSheet("background-color: black;")
        self.header.setFixedHeight(80)
        header_layout = QtWidgets.QHBoxLayout(self.header)
        header_layout.setContentsMargins(30, 0, 30, 0)  # Adjust margins to match design
        
        # MACWatch Label
        self.title_label = QtWidgets.QLabel("MACWatch")
        self.title_label.setStyleSheet("""
            color: white;
            font-size: 22pt;
            padding: 10px;
        """)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        
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
        
        # Main Content Area
        self.content = QtWidgets.QHBoxLayout()
        self.content.setSpacing(0)
        
        # Left Sidebar
        self.sidebar = QtWidgets.QWidget()
        self.sidebar.setFixedWidth(120)
        self.sidebar.setStyleSheet("background-color: rgb(240, 240, 240);")
        sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(30, 20, 10, 20)
        
        # Agent Button
        self.agent_btn = QtWidgets.QPushButton("Agent1")
        self.agent_btn.setFixedSize(60, 60) 
        self.agent_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid #ccc;
                border-radius: 25px;    
                font-size: 15px;
                font-weight: bold;
                text-align: center;      
                line-height: 50px;  
            }
        """)
        sidebar_layout.addWidget(self.agent_btn)
        
        # Add Button
        self.add_btn = QtWidgets.QPushButton("+")
        self.add_btn.setFixedSize(60, 60)  # Match exact size
        self.add_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid #ccc;
                border-radius: 25px;    
                font-size: 15px;
                font-weight: bold;
                text-align: center;      
                line-height: 50px;  
            }
        """)
        sidebar_layout.addWidget(self.add_btn)
        sidebar_layout.addStretch()
        
        # Main Content
        self.main_content = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(self.main_content)
        main_layout.setAlignment(QtCore.Qt.AlignHCenter)
        main_layout.setSpacing(20) 
     
        # Monitor Label
        self.monitor_label = QtWidgets.QLabel("Monitor")
        self.monitor_label.setStyleSheet("""
            font-size: 20pt;
            font-weight: bold;
            margin-top: 40px;
        """)
        self.monitor_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # IT404 Label
        self.it_label = QtWidgets.QLabel("IT 404")
        self.it_label.setStyleSheet("""
            font-size: 20pt;
            font-weight: bold;
            margin-top: 20px;
        """)
        self.it_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # Description Label
        self.desc_label = QtWidgets.QLabel("ตรวจจับการ MAC spoofing ที่ห้อง IT404")
        self.desc_label.setStyleSheet("""
            font-size: 16pt;
            margin-top: 20px;
        """)
        self.desc_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # Disconnect Button
        self.disconnect_btn = QtWidgets.QPushButton("Disconnect")
        self.disconnect_btn.setFixedSize(93, 28)  # Match exact size
        self.disconnect_btn.setStyleSheet("""
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

        
        # Add widgets to main layout
        main_layout.addStretch()
        main_layout.addWidget(self.monitor_label)
        main_layout.addWidget(self.it_label)
        main_layout.addWidget(self.desc_label)
        main_layout.addWidget(self.disconnect_btn, alignment=QtCore.Qt.AlignCenter)
        main_layout.addStretch()
        
        # Add all main sections to the central layout
        self.central_layout.addWidget(self.header)
        self.content.addWidget(self.sidebar)
        self.content.addWidget(self.main_content)
        self.central_layout.addLayout(self.content)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())