import mysql.connector

cnx = mysql.connector.connect(host='192.168.2.202', user='reader', database='home', password='reader')
cursor = cnx.cursor()

query = ("SELECT * FROM autokennzeichen")


cursor.execute(query)

# print the first and second columns      
for row in cursor.fetchall() :
    print row[1]

cursor.close()
cnx.close()
