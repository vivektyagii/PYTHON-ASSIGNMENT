import mysql.connector

# Function to create a MySQL connection
def create_connection():
    try:
        # Replace 'your_username', 'your_password', and 'your_database' with your actual MySQL credentials
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to create a table
def create_table(connection):
    try:
        cursor = connection.cursor()

        # Create 'students' table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                age INT,
                grade FLOAT
            )
        """)

        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to insert a new student record
def insert_student(connection, first_name, last_name, age, grade):
    try:
        cursor = connection.cursor()

        # Insert a new student record
        cursor.execute("""
            INSERT INTO students (first_name, last_name, age, grade)
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, age, grade))

        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to update the grade of a student
def update_grade(connection, first_name, new_grade):
    try:
        cursor = connection.cursor()

        # Update the grade of the student with the given first name
        cursor.execute("""
            UPDATE students
            SET grade = %s
            WHERE first_name = %s
        """, (new_grade, first_name))

        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to delete a student by last name
def delete_student(connection, last_name):
    try:
        cursor = connection.cursor()

        # Delete the student with the given last name
        cursor.execute("""
            DELETE FROM students
            WHERE last_name = %s
        """, (last_name,))

        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to fetch and display all student records
def fetch_students(connection):
    try:
        cursor = connection.cursor()

        # Fetch all student records
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        # Display student records
        print("Student Records:")
        for student in students:
            print(student)

        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Main program
if __name__ == "__main__":
    # Create a MySQL connection
    connection = create_connection()

    if connection:
        # Create the 'students' table
        create_table(connection)

        # Insert a new student record
        insert_student(connection, "Alice", "Smith", 18, 95.5)

        # Update the grade of the student with the first name "Alice"
        update_grade(connection, "Alice", 97.0)

        # Delete the student with the last name "Smith"
        delete_student(connection, "Smith")

        # Fetch and display all student records
        fetch_students(connection)

        # Close the connection
        connection.close()
