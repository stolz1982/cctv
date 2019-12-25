import mysql.connector
ocr_result='HVL-KB 808'
cnx = mysql.connector.connect(host='192.168.2.202', user='reader', database='home', password='reader')
cursor = cnx.cursor()

sql = "Insert into verkehrsdaten (autokennzeichen, description) values (%s, %s)"

val = (ocr_result, "Test am 25.12.2019")
cursor.execute(sql, val)

#important to write to DB
cnx.commit()

print(cursor.rowcount, "record inserted.")

cursor.close()
cnx.close()
