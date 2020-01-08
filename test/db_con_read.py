import mysql.connector
import json

credentials = '/home/pi/cctv/test/credentials.secret'

with open(credentials) as file:
    data = json.load(file)
    hostname = data["host"]
    password = data["password"]
    user = data["user"]
    file.close()

print(hostname)
print(password)
print(user)


ocr_result='HVL-SE 162'
cnx = mysql.connector.connect(host='192.168.2.202', user='reader', database='home', password='reader')
cursor = cnx.cursor()

query = ("SELECT * FROM autokennzeichen")


cursor.execute(query)

# print the first and second columns      
for row in cursor.fetchall() :
	if ocr_result == row[1]:
		print(row[1])

cursor.close()
cnx.close()
