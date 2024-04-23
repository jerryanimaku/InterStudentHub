import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password1234'
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE animaku")

print("All Done!")