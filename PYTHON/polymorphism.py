# polymorphism => having more than one form

# airthematic => addition
# string => concatination

# class A():
#     def display(self):
#         print("class A")


# class B():
#     def display(self):
#         print("class B")


# class C():
#     def display(self):
#         print("class C")

# #polymorphism
# def display_one(obj):
#     # c.display()
#     obj.display()


# a = A()
# b = B()
# c = C()


# display_one(a)
# display_one(b)
# display_one(c)


class Animal:
    def speak(self):
        print("Animal speak")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")


class Pug(Dog):
    def speak(self):
        super().speak()
        print("pug barks")


# d = Dog()
# d.speak()

p = Pug()
p.speak()

class NonNegativeException(Exception):
    def __init__(self, *args):
        super().__init__(*args)