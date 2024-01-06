import mysql.connector

database = mysql.connector.connect(
    host="localhost", user="root", passwd="123456", database="test"
)

cursorObject = database.cursor()

cursorObject.execute("select * from website_record")
result = cursorObject.fetchall()

for main in result:
    print(main)
