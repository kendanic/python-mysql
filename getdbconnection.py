# from db_connection import get_connection

# # Get the database connection
# mydb = get_connection()

# if mydb:
#     mycursor = mydb.cursor()
#     # Example query: Fetch data from a table
#     mycursor.execute("SELECT * FROM employees")
#     result = mycursor.fetchall()

#     for row in result:
#         print(row)

#     # Don't forget to close the connection
#     mydb.close()

from db_connection import get_connection

# Get the database connection
mydb = get_connection()

if mydb:
    print("Connection successful")
    mycursor = mydb.cursor()

    try:
        # Example query: Fetch data from a table
        mycursor.execute("SELECT * FROM employees")
        result = mycursor.fetchall()

        print("Query executed successfully. Number of rows fetched:", len(result))

        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
    finally:
        # Don't forget to close the connection
        mycursor.close()
        mydb.close()
else:
    print("Failed to connect to the database.")

