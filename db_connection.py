import mysql.connector
from mysql.connector import errorcode

def get_connection():
    config = {
        'user': 'ken',
        'password': 'Ken@123',
        'host': '192.168.1.10', 
        'port': 3310, 
        'database': 'kendanic', 
        'raise_on_warnings': True
    }
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Errors as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
            print("Something is wrong with your user name or password") 
        elif err.errno == errorcode.ER_BAD_DB_ERROR: 
            print("Database does not exist")
        else: 
            print(err)
        return None        

