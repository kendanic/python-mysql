from db_connection import get_connection

# Establish a connection to the database
mydb = get_connection()

if mydb:
    mycursor = mydb.cursor()

    # Define your table creation query
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        emp_no INT AUTO_INCREMENT PRIMARY KEY,
        birth_date DATE NOT NULL,
        first_name VARCHAR(14) NOT NULL,
        last_name VARCHAR(16) NOT NULL,
        gender ENUM('M','F') NOT NULL,
        hire_date DATE NOT NULL
    ) ENGINE=InnoDB;
    """

    # Execute the query
    mycursor.execute(create_table_query)
    print("Table 'employees' created successfully.")

    # Close the cursor and the connection
    mycursor.close()
    mydb.close()
else:
    print("Failed to connect to the database.")
