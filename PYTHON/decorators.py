# decorator => it is a higher order function that modifies or extends the behaviour of a function without changing the behaviour of that function

# why function is called first class citizen 
# because it can be store in variable, pass as argument and return as result
"""
def sum():
    print(10 + 20)

def sub():
    print(10 - 30)

def greet(fun1,fun2): 
    print("This is before call")
    fun1()
    fun2()
    print("This is after call")
greet(sum,sub)
//
def function():
    def sum():
        print(10 + 20)

    return sum

cb = function()
cb() 
"""

#using decorator in the function
#Here, no need to function call, @function_name works and it's decorator call 
"""
def my_decorator(func): #third my_decorator(greet) function pass
    def wrapper():
        print("Before function calling")
        func() #fourth greet call
        print("After function calling")
    return wrapper

@my_decorator #second call-decorator calling  
def greet():
    print("Hi Baby")
greet() #first call
//
def my_decorator(func):
    def wrapper(username,password):
        if username == "admin" and password == "admin@123":
            func(username,password)
        else:
            print("You're not an admin!")
    return wrapper

@my_decorator
def log_in(username,password):
    print("Admin! Let's dive into the system!")

username = input("Enter your username: ")
password = input("Enter your password: ")

log_in(username,password)
"""

# using three function to pass the parameter in the decorator 
"""
def my_decorator(xyz):
    def outer_function(func):
        def wrapper(name):
            if xyz == 'GET':
                print(f"argument of function ====> {name}")
                return func(name)
            else:
                print("Invalid request")
        return wrapper
    return outer_function


@my_decorator("POST")
def greet(name):
    print(f"Hello {name}")

greet("sachin")
"""
# function documentation
'''
def sum(a: int,b: int) -> int:
    """_summary_ (This function do the sum between two integar number)

    Args:
        a (int): first integer number
        b (int): second integer number

    Returns:
        int: sum of two numbers in integer
    """
    return a + b
'''





