from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,QPixmap, QRadialGradient)
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QCheckBox, QTableWidgetItem, QGroupBox, QComboBox, QDateEdit, QLineEdit, QTabWidget, QSpinBox, QListWidget, QVBoxLayout
from MainWindow import MainWindow
from WorkWithSqlite import BD
from fuzzywuzzy import fuzz


class Main(QWidget, MainWindow):
    """docstring for Main"""
    def __init__(self):
        super().__init__()
        self.data = BD.SelectData()
        self.statusShowAll = True
        self.statusAddGroup = False
        self.statusDeleteGroup = False
        self.statusShowPasswords = False

        self.MadeWindow()
        self.fillTable(self.data)

        self.plusBtn.clicked.connect(self.showAddGroup)
        self.minusBtn.clicked.connect(self.showDeleteGroup)
        self.showPasswords.clicked.connect(self.requestPassword)
        self.showPasswordsBtn.clicked.connect(self.eventShowPassword)
        self.cancelShowPasswords.clicked.connect(self.cancelEventShowPasswords)
        self.addBtn.clicked.connect(self.addWIFI)
        self.deleteBtn.clicked.connect(self.deleteWIFI)
        self.btnSearch.clicked.connect(self.searchWIFI)


    def fillTable(self,data):
        for index in range(len(data)):
            self.listWIFI.setItem(index, 0, QTableWidgetItem(data[index]['wi-fi']))
            self.listWIFI.setItem(index, 1, QTableWidgetItem(len(data[index]['password'])*"•"))
            self.listWIFI.setItem(index, 2, QTableWidgetItem(data[index]['place']))
        self.listWIFI.setHorizontalHeaderLabels(('WI-FI', 'Password', 'Place/Person'))


    def requestPassword(self):
        if not self.statusShowPasswords:
            self.showPasswordsBtn.show()
            self.cancelShowPasswords.show()
            self.showPasswordsText.show()
            self.showPasswordsEntery.show()
            self.resize(800,1000)
        else:
            if self.statusShowAll:
                for index in range(len(self.data)):
                    self.listWIFI.setItem(index, 1, QTableWidgetItem(len(self.data[index]['password'])*"•"))
            else:
                for index in range(len(self.dataOutput)):
                    self.listWIFI.setItem(index, 1, QTableWidgetItem(len(self.dataOutput[index]['password'])*"•"))
            self.statusShowPasswords = False
            self.showPasswords.setText("показать всё")


    def eventShowPassword(self):
        if self.showPasswordsEntery.text() == "1570":
            if self.statusShowAll:
                for index in range(len(self.data)):
                    self.listWIFI.setItem(index, 1, QTableWidgetItem(self.data[index]['password']))
            else:
                for index in range(len(self.dataOutput)):
                    self.listWIFI.setItem(index, 1, QTableWidgetItem(self.dataOutput[index]['password']))
            self.showPasswordsEntery.clear()
            self.showPasswordsEntery.hide()
            self.resize(800,900)
            self.statusShowPasswords = True
            self.showPasswords.setText("скрыть всё")
        else:
            self.showPasswordsEntery.clear()
            self.showPasswordsEntery.hide()
            self.resize(800,900)


    def cancelEventShowPasswords(self):
        self.resize(800,900)
        self.showPasswordsEntery.clear()
        self.showPasswordsBtn.hide()
        self.cancelShowPasswords.hide()
        self.showPasswordsText.hide()
        self.showPasswordsEntery.hide()


    def showDeleteGroup(self):
        if not self.statusDeleteGroup:
            self.deleteGroup.show()
            self.addGroup.hide()
            self.resize(800,1200)
            self.statusDeleteGroup = True
            self.statusAddGroup = False
        else:
            self.deleteGroup.hide()
            self.resize(800,900)
            self.statusDeleteGroup = False


    def showAddGroup(self):
        if not self.statusAddGroup:
            self.addGroup.show()
            self.deleteGroup.hide()
            self.resize(800,1200)
            self.statusAddGroup = True
            self.statusDeleteGroup = False
        else:
            self.addGroup.hide()
            self.resize(800,900)
            self.statusAddGroup = False


    def addWIFI(self):
        wifi = self.wifiEntery.text()
        password = self.passwordEntery.text()
        place = self.placeEntery.text()
        if wifi != "" and password != "" and place != "":
            self.listWIFI.setItem((len(self.data)), 0, QTableWidgetItem(wifi))
            self.listWIFI.setItem((len(self.data)), 1, QTableWidgetItem(len(password)*"•"))
            self.listWIFI.setItem((len(self.data)), 2, QTableWidgetItem(place))

            items = {}
            items['id'] = len(self.data) + 1
            items['wifi'] = wifi
            items['password'] = password
            items['place'] = place
            self.data.append(items)

            BD.AddData(self.data[-1])
            self.wifiEntery.clear()
            self.passwordEntery.clear()
            self.passwordEntery.clear()


    def deleteWIFI(self):
        rowDelete = self.deleteEntery.value()
        self.listWIFI.removeRow(rowDelete-1)
        print(self.data[rowDelete-1])
        BD.DeleteData(self.data[rowDelete-1]['id'])
        del self.data[rowDelete-1]


    def searchWIFI(self):
        self.dataOutput = []
        wifi = self.enterySearch.text()
        if wifi != "":
            for index in range(len(self.data)):
                percent_1 = fuzz.ratio(self.data[index]['wi-fi'], wifi)
                percent_2 = fuzz.ratio(self.data[index]['place'], wifi)
                if percent_1 >= 65:
                    self.dataOutput.append(self.data[index])
                elif percent_2 >= 65:
                    self.dataOutput.append(self.data[index])
            self.statusShowAll = False
            self.listWIFI.clear()
            self.fillTable(self.dataOutput)
        else:
            self.statusShowAll = True
            self.listWIFI.clear()
            self.fillTable(self.data)



if __name__ == "__main__":
    import sys                                  
    app = QApplication(sys.argv)    
    window = Main()                           
    window.show()
    sys.exit(app.exec_())   