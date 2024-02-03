import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'root'
)

cursor = db.cursor();

cursor.execute("create database stalwart")

print("Successfully initiated database")


