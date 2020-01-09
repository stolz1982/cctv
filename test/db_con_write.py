import mysql.connector
import json

db = home
credentials = '/home/pi/cctv/test/credentials.secret'

with open(credentials) as file:
    data = json.load(file)
    hostname = data["host"]
    pwd = data["password"]
    login = data["user"]
    file.close()

ocr_result='HVL-KB 808'

cnx = mysql.connector.connect(host=%s, user=%s, database=db, password=%s) %(hostname, login, pwd) 

cursor = cnx.cursor()

sql = "Insert into verkehrsdaten (autokennzeichen, description) values (%s, %s)"

val = (ocr_result, "Test am 25.12.2019")
cursor.execute(sql, val)

#important to write to DB
cnx.commit()

print(cursor.rowcount, "record inserted.")

cursor.close()
cnx.close()
