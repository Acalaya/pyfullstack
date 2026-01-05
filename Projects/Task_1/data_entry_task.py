# Data Entry Software for Employees

def save_employee_data(name, age, designation, salary):
    with open("employee.txt", "a") as file:
        file.write(f"Name of employee: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Designation: {designation}\n")
        file.write(f"Salary: Rs {salary}\n\n")


print("=== Employee Data Entry Software ===")

while True:
    name = input("Enter employee name: ")
    age = input("Enter age: ")
    designation = input("Enter designation: ")
    salary = input("Enter salary: ")

    save_employee_data(name, age, designation, salary)

    print("\nEmployee data saved successfully!\n")

    choice = input("Do you want to add another employee? (yes/no): ").lower()
    if choice != "yes":
        print("\nExiting program. Data saved in employee.txt")
        break