# Error handling: try,except,else,finally
"""
try:
    num1 = int(input("Enter a number "))
    num2 = int(input('Enter the next number'))
    div = num1/num2 
    print(div)
except ZeroDivisionError as e: 
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Numbers must be integer.")
else:
    print("if try is succeed , I run otherwise I don't")
finally:
    print("The Acalaya")
    print("I don't care what happens, I run whatever the situation be") """

# Custom Error Handling 
"""
class Notgenz(Exception):
    pass 
try:
    age = int(input("Enter your age: "))
    if 18 < age > 28:
        raise Notgenz("You're not a genz")
except Notgenz as e:
    print(f"Error: {e}")
else:
    print(age) """

# File handling : r,w,a,x 
"""
// here, we gotta close the file
file = open("text.txt","r")
data = file.read()
print(data)
file.close()
//  
with open("text.txt", "r") as file:
    data = file.read(10)
    print(file.readline())
    print(file.readlines())
    print(file.readlines()[3])
    print(data) """




