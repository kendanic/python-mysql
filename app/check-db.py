import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.10",
  port=3310,
  user="ken",
  password="Ken@123"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE demo0001")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
