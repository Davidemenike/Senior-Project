from distutils.util import execute
import pymysql
import config as cf
from tkinter import messagebox



def DeleteData(ID):
    conn, cur = None, None
    table = None
    data1, data2, data3 = "", "", ""
    sql = ""
    table = "filament"  # table name

    conn = pymysql.connect(host=cf.host, user=cf.user,
                           password=cf.password, db=cf.database, charset='utf8')
    cur = conn.cursor()

    data1 = ID


    sql ="delete FROM filament where Filament_ID = "+str(data1)+ ";"
    
    cur.execute(sql)
    conn.commit()
    messagebox.showinfo("Successfully deleted")