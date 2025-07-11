import mysql.connector
from mysql.connector import errorcode
import os

def get_connection():
    config = {
        'user': os.getenv('DB_USER', 'ken'),
        'password': os.getenv('DB_PASSWORD', 'Ken@123'),
        'host': os.getenv('DB_HOST', '192.168.1.103'),
        'port': int(os.getenv('DB_PORT', 3310)),
        'database': os.getenv('DB_NAME', 'kendanic'),
        'raise_on_warnings': True
    }

    try:
        conn = mysql.connector.connect(**config)
        print("Database connection successful")
        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: check username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"MySQL Error: {err}")
        return None



# import mysql.connector
# from mysql.connector import errorcode

# def get_connection():
#     config = {
#         'user': 'ken',
#         'password': 'Ken@123',
#         'host': '192.168.1.103', 
#         'port': 3310, 
#         'database': 'kendanic', 
#         'raise_on_warnings': True
#     }
#     try:
#         conn = mysql.connector.connect(**config)
#         return conn
#     except mysql.connector.Errors as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
#             print("Something is wrong with your user name or password") 
#         elif err.errno == errorcode.ER_BAD_DB_ERROR: 
#             print("Database does not exist")
#         else: 
#             print(err)
#         return None        

