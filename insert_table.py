from db_connection import get_connection

# Get the database connection
mydb = get_connection()

if mydb:
    print("Connection successful")
    mycursor = mydb.cursor()

    try:
        # Insert sample data
        insert_data_query = """
        INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date)
        VALUES 
            ('1990-01-01', 'John', 'Doe', 'M', '2020-01-15'),
            ('1985-02-15', 'Jane', 'Smith', 'F', '2019-03-01');
        """
        mycursor.execute(insert_data_query)
        mydb.commit()
        print("Sample data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    finally:
        # Don't forget to close the connection
        mycursor.close()
        mydb.close()
else:
    print("Failed to connect to the database.")
