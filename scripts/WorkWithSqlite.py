import sqlite3

class BD(object):
    """docstring for DB"""
    def __init__(self):
        super().__init__()


    def connectBD():
        wifiDB = sqlite3.connect('wi-fi.db')

        cursor = wifiDB.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS WIFI(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wifi TEXT(255) NOT NULL,
            password TEXT(255) NOT NULL,
            place TEXT(255) NOT NULL, 
            deleteFlag BOOLEAN NOT NULL
            )""")
        wifiDB.commit()
        return wifiDB


    def AddData(data):
        db = DB.connectBD()
        cursor = db.cursor()
        cursor.execute("INSERT INTO WIFI(wifi,password,place,deleteFlag) VALUES(?,?,?,?)", (data['wifi'],data['password'],data['place'], False))
        db.commit()


    def SelectData():
        bd = BD.connectBD()
        cursor = bd.cursor()
        dataOutput = []
        for i in cursor.execute(f"SELECT * FROM WIFI WHERE deleteFlag = {0}"):
            item = {}
            item['id'] = i[0]
            item['wi-fi'] = i[1]
            item['password'] = i[2]
            item['place'] = i[3]
            dataOutput.append(item)
        bd.commit()
        return dataOutput


    def DeleteData(id_row):
        bd = BD.connectBD()
        cursor = bd.cursor()
        cursor.execute(f"UPDATE WIFI SET deleteFlag = {True} WHERE id = {id_row}")
        bd.commit()


    def UpdateData(id_start, id_new):
        bd = BD.connectBD()
        cursor = bd.cursor()
        cursor.execute(f"UPDATE WIFI SET id = {id_new} WHERE id = {id_start}")
        bd.commit()


    def ClearAll(bd_i):
        bd = BD.connectBD()
        cursor = bd.cursor()
        if bd_i == 0:
            cursor.execute(f"DELETE FROM Expenses")
        else:
            cursor.execute(f"DELETE FROM Income")
        bd.commit()