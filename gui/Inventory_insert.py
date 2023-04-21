from distutils.util import execute
import pymysql
import random
import datetime
from tkinter import *
from tkinter import messagebox
import config as cf

CheckME = "0"
CheckNum = False
ValidNum = False
ValidDate = False
conn, cur = None, None
data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
sql = ""

list = range(1,1000)

def containsNumber(data):
    for Name in data:
        if Name.isdigit():
            return True
        return False
    
def querydata():
    conn2 = pymysql.connect(host = cf.host, user = cf.user,
                           password = cf.password, db = cf.database)
    
    curry = conn2.cursor()

    sql2 = "SELECT * from filament"
    david = curry.execute(sql2)
    #print(curry.fetchall())
    david2 = curry.fetchall()
    return david2


    


def insertdata(material_entry, color_entry, addetive_entry, brand_entry,remaining_entry):
    conn = pymysql.connect(host = cf.host, user = cf.user,
                           password = cf.password, db = cf.database)
    
    curr = conn.cursor()

    sql = "CREATE TABLE IF NOT EXISTS filament (Filament_ID int AUTO_INCREMENT, Material char(40), Color char(40), Addetive char(40), Brand char(40), Remaining char(40), PRIMARY KEY (FIlament_ID))"
    curr.execute(sql)
    curr.execute("SELECT * FROM filament")
    row = curr.fetchone()


    
    
    data2 = material_entry.get()
    CheckNum = containsNumber(data2)
    if(CheckNum == True):
        raise Exception(
            'Error', "please remove number ")  # if user add number in name entry show Error box.
    
    
    data3 = color_entry.get()
    CheckNum = containsNumber(data3)
    if(CheckNum == True):
        raise Exception(
            'Error', "please remove number ")  # if user add number in name entry show Error box.


    data4 = addetive_entry.get()
    CheckNum = containsNumber(data4)
    if(CheckNum == True):
        raise Exception(
            'Error', "please remove number ")  # if user add number in name entry show Error box.

    data5 = brand_entry.get()
    CheckNum = containsNumber(data5)
    if(CheckNum == True):
        raise Exception(
            'Error', "please remove number ")  # if user add number in name entry show Error box.

    data6 = remaining_entry.get()
    
    sql = "INSERT INTO filament (Material, Color, Addetive, Brand, Remaining) VALUES(%s, %s, %s, %s, %s)"
    val = (data2, data3, data4, data5, data6)
    curr.execute(sql , val)


    conn.commit()
    conn.close()        
        
        
