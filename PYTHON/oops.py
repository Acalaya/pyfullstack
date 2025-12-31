# class = blueprint of an instance that contain property and method
# object = instance of a class which may be physical entity
"""
class Animal:  #PascalCase
    # constructor = method similar to the class that is called whenever an object is created for the first time, dunder method
    def __init__(self,name):
        print(f"{name}, call me whenever an object is created")

    #method
    def speak(self,name):
        return(f"{name} speak")

    def walk(self):
        print("Animal Walk")

dog = Animal(name= "Darling")
speak_character = dog.speak("Baby")
dog.walk()
print(speak_character) """

class Math:

    PI = 3.14
    
    def __init__(self,name = None,length=None,breadth=None):
        self.length = length
        self.breadth = breadth

    def area_of_circle(self):
        return Math.PI * (self.length ** 2)
    
    def area_of_rectangle(self):
        return self.length * self.breadth
    
    def area_of_square(self):
        return self.length ** 2


    def double(self):
        inner_function = lambda x: x**2 #firstclass citizen function, cause it can be passed as an assignment and also a variable
        return inner_function

    
circle = Math(name="Ac")
calc = circle.double()
print(calc(2))

area = Math(length=5,breadth=10)
print(area.area_of_circle())
print(area.area_of_rectangle())
print(area.area_of_square())




