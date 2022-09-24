import mysql.connector
import numpy as np
from mysqlx import Column
from mysql.connector import Error
import datetime


# x = list(input("Enter your id number:"))
id1 = input("Enter id:")
eid = (id1,)

tv = input("Type of vehicle[G/NG]:")
#fd=datetime.datetime.
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

    sql_select_Query = ("select * from dldata where id=%s")
    cursor = connection.cursor()
    prow = cursor.execute(sql_select_Query,eid)
    mrow = cursor.fetchone()
    print(mrow)
    diff = mrow[6]-mrow[5]
    #stdiff = int(diff.strftime("%d"))
    print(type(diff))
    #print(mrow[1])

    # records = cursor.fetchall()
    # print("Total number of rows in table: ", cursor.rowcount)
    if(mrow[7]==tv):
        #if(diff<=67305):
        print("Verification successfull!")
        #else:
            #print("License is expired!")
    
    else:
        print("Verification unsuccessfull!!")
    


    print(prow)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")