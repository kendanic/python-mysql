import mysql.connector

demodb = mysql.connector.connect(
  host = "192.168.1.10",
  port = 3310,
  user ="ken",
  password="Ken@123"
  #database="kendanic"
)

mycursor = demodb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)