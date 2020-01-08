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

ocr_result='HVL-SE 162'
cnx = mysql.connector.connect(host=%s, user=%s, database=db, password=%s) %(hostname, login, pwd) 
cursor = cnx.cursor()

query = ("SELECT * FROM autokennzeichen")


cursor.execute(query)

# print the first and second columns      
for row in cursor.fetchall() :
	if ocr_result == row[1]:
		print(row[1])

cursor.close()
cnx.close()
