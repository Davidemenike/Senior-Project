from distutils.util import execute
from sqlite3 import connect
import pymysql
import config as cf
from tkinter import messagebox
import datetime

conn, cur = None, None
data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
row = None

conn = pymysql.connect(host=cf.host, user=cf.user,
                       password=cf.password, db=cf.database, charset='utf8')
cur = conn.cursor()


def updateData(material, color, addetive, brand, remaining, Filament_Id):
    data1 = material.get()
    data2 = color.get()
    data3 = addetive.get()
    data4 = brand.get()
    data5 = remaining.get()
    data6 = Filament_Id




    update_info = "update filament set Material= '" + data1 + "', Color= '" + \
        data2 + "', Addetive='" +data3 +"', Brand='" + \
        data4 + "', Remaining=" +str(data5) +" where Filament_ID = "+ str(data6) + ";"
    
    try:
        cur.execute(update_info)
        conn.commit()
        print("Record Updated!")

    except Exception as e:
        print("Exception Occured : ", e)
        conn.rollback()
    
    else:
        messagebox.showinfo('succeded', "Update Succeded")

    conn.close()


