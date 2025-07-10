import mysql.connector

# Define the connection details
host = "172.17.0.2"  # Use container's IP or "localhost" if exposed on port 3306
port = 3310  # Default MySQL port
user = "ken"  # MySQL username
password = "Ken@123"  # MySQL password (set when running the container)
database = "kendanic"  # The database you want to connect to (optional)

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")
        cursor = connection.cursor()
        
        # Run your queries here
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record}")
        
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
