# creating database 

import sqlite3;

DATABASE_NAME = "database.db"

connection = sqlite3.connect(DATABASE_NAME) #connecting database to the main 
print("Database connected successfully")

with connection as conn:
    c = conn.cursor()
#creating table
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS Students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(22),
            last_name VARCHAR(22),
            age INTEGER,
            status VARCHAR(10)
        )
        '''

    )

#creating functions for different operations:
def add_student(first_name,last_name,age,status):
    with connection as conn:
        c = conn.cursor()
        c.execute(
            '''
            INSERT INTO Students (first_name, last_name, age, status)
            VALUES(?,?,?,?)
            ''',
            (first_name,last_name,age,status)
        )
        conn.commit()

def update_data(student_id,value,field_name):
    with connection as conn:
    
        c = conn.cursor()
        c.execute(f"UPDATE Students SET {field_name} = ? WHERE id ={student_id}",(value,))

def read_data():
    with connection as conn:
        c = conn.cursor()
        row = c.execute("SELECT * FROM Students")
    return row

def delete_data(id):
    with connection as conn:
        c = conn.cursor()
        c.execute(f"DELETE FROM Students WHERE id={id}")

while True:  #doesn't close the terminal 
    choice = int(input(
        '''
        Enter your choice :
        1.Add new student
        2.Update student info
        3.Delete customer
        4.Read all students info
        5. Exit
        '''
    ))

    if choice == 1:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name : ")
        age = input("Enter your age: ")
        status = input("Enter your status: ")
        add_student(first_name=first_name,last_name=last_name,age=age,status=status)

    elif choice == 2:
        student_id = int(input("Enter the student id to update"))
        update_choice = int(input(
            '''
            Enter the following update choice:
            1. first name
            2. last name
            3. age
            4. status
            5. return back
            '''
        ))
        if update_choice == 1:
            first_name = input("Enter your first name: ")
            update_data(student_id,first_name,'first_name')
        elif update_choice == 2:
            last_name = input("Enter your last name: ")
            update_data(student_id,last_name,'last_name')
        elif update_choice == 3:
            age = input("Enter your age: ")
            update_data(student_id,age,'age')
        elif update_choice == 4:
            status = input("Enter your status: ")
            update_data(student_id,status,'status')
        
        else:
            print("Invalid choice!!")

    elif choice == 3:
        student_id = int(input("Enter students id: "))
        delete_data(student_id)
        print(f"Student with id {student_id} deleted successfully! ")

    elif choice == 4:
        data = read_data()
        for students in data:
            print(

                f'''
                Name: {students[1]} {students[2]} | Age: {students[3]} | Status: {students[4]}
                '''
            )
    elif choice == 5:
        break

    else:
        print("Invalid choice! ")