import mysql.connector
from mysqlx import Column
import qrcode
import image
from mysql.connector import Error

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

    sql_select_Query = "select * from dldata"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    counter = 0
    row_count = 10
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    qr = qrcode.QRCode(
                version = 1,
                error_correction = qrcode.constants.ERROR_CORRECT_L,
                box_size = 12,
                border = 2
                )

    # for row in records:
        
        # print(row)
        #print("\n")
        #for x in range(10):
        
        # print("Id = ", row[0], )
        # print("First Name = ", row[1])
        # print("Middle Name  = ", row[2])
        # print("Last Name  = ", row[3])
        # print("Date of Birth  = ", row[4])
        # print("First Issued Date  = ", row[5])
        # print("Expiry Date  = ", row[6])
        # print("Type of License = ", row[7], "\n")
    counter = 0

    for row in records:
        print(list(row))
        qr.add_data(row)
        qr.make(fit=True)
        img=qr.make_image(fill='black',back_color='White')
        img.save("qr"+ str(row[0])+ ".png")
        qr.clear()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

