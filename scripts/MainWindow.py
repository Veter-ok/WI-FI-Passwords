from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,QPixmap, QRadialGradient)
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QCheckBox, QTableWidgetItem, QGroupBox, QComboBox, QDateEdit, QLineEdit, QTabWidget, QSpinBox, QListWidget, QVBoxLayout


class MainWindow(object):

	def MadeWindow(self):
		self.resize(800,900)
		self.setStyleSheet("background-color: #1D1C1A;\ncolor: black;\nfont-size: 30px;")
		self.setWindowIcon(QIcon("icons/wifi-icon.ico"))
		self.setWindowTitle("Список WI-FI")

		self.enterySearch = QLineEdit(self)
		self.enterySearch.setStyleSheet("background-color: white;")
		self.enterySearch.setGeometry(10,10,660,50)

		self.btnSearch = QPushButton(self)
		self.btnSearch.setText("search")
		self.btnSearch.setStyleSheet("background-color: grey;\ncolor: white;")
		self.btnSearch.setGeometry(680,10,100,50)

		self.listWIFI = QTableWidget(self)
		self.listWIFI.setGeometry(10,80,780,750)
		self.listWIFI.setStyleSheet("background-color: white;")
		self.listWIFI.setRowCount(1000)
		self.listWIFI.setColumnCount(3)
		self.listWIFI.horizontalHeader().setDefaultSectionSize(220)
		self.listWIFI.verticalHeader().setDefaultSectionSize(50)
		self.listWIFI.setHorizontalHeaderLabels(('WI-FI', 'Password', 'Place/Person'))

		self.plusBtn = QPushButton(self)
		self.plusBtn.setText("+")
		self.plusBtn.setStyleSheet("background-color: grey")
		self.plusBtn.setGeometry(90,840,80,50)

		self.minusBtn = QPushButton(self)
		self.minusBtn.setText("-")
		self.minusBtn.setStyleSheet("background-color: grey;")
		self.minusBtn.setGeometry(10,840,80,50)

		self.showPasswords = QPushButton(self)
		self.showPasswords.setText("show all")
		self.showPasswords.setStyleSheet("background-color: grey;")
		self.showPasswords.setGeometry(590,840,200,50)

		self.showPasswordsText = QLabel(self)
		self.showPasswordsText.setText("enetery password")
		self.showPasswordsText.setStyleSheet("color: white;")
		self.showPasswordsText.setGeometry(60,900,220,50)

		self.showPasswordsEntery = QLineEdit(self)
		self.showPasswordsEntery.setEchoMode(QLineEdit.Password)
		self.showPasswordsEntery.setStyleSheet("background-color: white;\ncolor: black;")
		self.showPasswordsEntery.setGeometry(290,900,350,50)

		self.showPasswordsBtn = QPushButton(self)
		self.showPasswordsBtn.setText("Ввод")
		self.showPasswordsBtn.setStyleSheet("background-color: grey;")
		self.showPasswordsBtn.setGeometry(660,900,80,50)

		self.cancelShowPasswords = QPushButton(self)
		self.cancelShowPasswords.setText("Отмена")
		self.cancelShowPasswords.setStyleSheet("background-color: grey;")
		self.cancelShowPasswords.setGeometry(400,950,120,50)

		self.addGroup = QGroupBox(self)
		self.addGroup.setTitle('add')
		self.addGroup.setStyleSheet("color: white;")
		self.addGroup.setGeometry(10,890,770,300)

		self.wifiText = QLabel(self.addGroup)
		self.wifiText.setText("WI-FI")
		self.wifiText.setStyleSheet("color: white;")
		self.wifiText.setGeometry(10,50,80,50)

		self.wifiEntery = QLineEdit(self.addGroup)
		self.wifiEntery.setStyleSheet("background-color: white;\ncolor: black;")
		self.wifiEntery.setGeometry(150,50,500,50)

		self.passwordText = QLabel(self.addGroup)
		self.passwordText.setText("Password")
		self.passwordText.setStyleSheet("color: white;")
		self.passwordText.setGeometry(10,120,150,50)

		self.passwordEntery = QLineEdit(self.addGroup)
		self.passwordEntery.setEchoMode(QLineEdit.Password)
		self.passwordEntery.setStyleSheet("background-color: white;\ncolor: black;")
		self.passwordEntery.setGeometry(150,120,500,50)

		self.placeText = QLabel(self.addGroup)
		self.placeText.setText("Place")
		self.placeText.setStyleSheet("color: white;")
		self.placeText.setGeometry(10,190,150,50)

		self.placeEntery = QLineEdit(self.addGroup)
		self.placeEntery.setStyleSheet("background-color: white;\ncolor: black;")
		self.placeEntery.setGeometry(150,190,500,50)

		self.addBtn = QPushButton(self.addGroup)
		self.addBtn.setText("add")
		self.addBtn.setStyleSheet("background-color: grey;")
		self.addBtn.setGeometry(300,250,140,50)

		self.deleteGroup = QGroupBox(self)
		self.deleteGroup.setTitle('delete')
		self.deleteGroup.setStyleSheet("color: white;")
		self.deleteGroup.setGeometry(10,890,770,300)

		self.rowText = QLabel(self.deleteGroup)
		self.rowText.setText("line")
		self.rowText.setStyleSheet("color: white;")
		self.rowText.setGeometry(10,50,100,50)

		self.deleteEntery = QSpinBox(self.deleteGroup)
		self.deleteEntery.setStyleSheet("background-color: white;\ncolor: black;")
		self.deleteEntery.setGeometry(120, 50, 300, 50)
		self.deleteEntery.setMaximum(1000000000)
		self.deleteEntery.setMinimum(1)

		self.deleteBtn = QPushButton(self.deleteGroup)
		self.deleteBtn.setText("delete")
		self.deleteBtn.setStyleSheet("background-color: grey;")
		self.deleteBtn.setGeometry(300,250,140,50)

		self.show()
		self.addGroup.hide()
		self.deleteGroup.hide()