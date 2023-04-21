from distutils.util import execute
import pymysql
import config as cf

def gooday():
    return True

def ReadData():
    
    material_name = []
    color_name = []
    addetive_name = []
    brand_name = []
    remaining_name = []
    filament_id = []
    conn, curr = None, None

    data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
    row = None


    conn = pymysql.connectconn = pymysql.connect(host = cf.host, user = cf.user,
                           password = cf.password, db = cf.database)
    
    curr = conn.cursor()

    curr.execute("SELECT * FROM filament")

    while(True):
        row = curr.fetchone()
        if row == None:
            break
        data1, data2, data3, data4, data5, data6 = row

        filament_id.append(data1)
        material_name.append(data2)
        color_name.append(data3)
        addetive_name.append(data4)
        brand_name.append(data5)
        remaining_name.append(data6)
    return material_name, color_name, addetive_name, brand_name,remaining_name,filament_id
    curr.close()