# data entry software:
# requirements
# suppose a company needed a data entry software. The manager of company request you to make a data entry software. where he can enter a data of employee with:
# employee_name,
# age,
# designation,
# salary,

# you have to build in such a way that every data is saved to the file name as employee.txt
# note: once you run the program the terminal must not close

# output(employee.txt):

# Name of employee: sachin barali
# Age: 23
# Designation: Manager
# Salary: Rs 200000

# Name of employee: Kosish Pariyar
# Age: 21
# Designation: CTO
# Salary: Rs 100000

# and so on.... 
data_entry = [ ]
with open("data.txt", "w") as file:
    data = file.write(input("Employee Name: "))
    print(data)

