import mysql.connector
ocr_result='HVL-SE 162'
cnx = mysql.connector.connect(host='192.168.2.202', user='reader', database='home', password='reader')
cursor = cnx.cursor()

query = ("SELECT * FROM autokennzeichen")


cursor.execute(query)

# print the first and second columns      
for row in cursor.fetchall() :
	if ocr_result == row[1]:
		print row[1]

cursor.close()
cnx.close()
