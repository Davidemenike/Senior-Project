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


def containsNumber(data):
    for Name in data:
        if Name.isdigit():
            return True
        return False
    

    


def insertdata(material_entry, color_entry, addetive_entry, brand_entry,remaining_entry):
    conn = pymysql.connect(host = cf.host, user = cf.user,
                           password = cf.password, db = cf.database)
    
    curr = conn.cursor()

    sql = "CREATE TABLE IF NOT EXISTS filament (Filament_ID char(10), Material char(10), Color char(10), Addetive char(10), Brand char(10), Remaining char(10), PRIMARY KEY (FIlament_ID))"
    curr.execute(sql)
    curr.execute("SELECT * FROM filament")
    row = curr.fetchone()


    
    data1 = str(1)
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
    
    sql = "INSERT INTO filament VALUES("+data1 + \
        ",'"+data2+"','"+data3+"',"+data4+","+data5+"','"+str(data6)+")"
    curr.execute(sql)


    conn.commit()
    conn.close()        
        
        
