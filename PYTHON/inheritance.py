# inheritance => accessing the properties and method by child class from base class 

class A:
    a_name = "Sachin"
    a_age = 21

    def displayA(self):
        print("class A")

class B(A):
    b_name ="keshab"
    b_age = 10

    def displayB(self):
        print("Class B")


a = A()
a.displayA()
b = B()
b.displayB()
print(b.a_name)

# single inheritance

class Base:

    def printBase(self):
        print("Base class")


class Child(Base):

    def printChild(self):
        print("Child class")


child = Child()


# multi level inheritance 

class A:
    def printA(self):
        print("this is class A")

class B(A):
    def printB(self):
        print("this is class B")

class C(B):
    def printC(self):
        print("this is class C")

c = C()
c.printA()


# hybrid inheritance

class A:
    def printA(self):
        print("this is class A")

class B(A):
    def printB(self):
        print("this is class B")

class C(A):
    def printC(self):
        print("this is class C")


class D(B,C):
    def printD(self):
        print("This is class D")

d = D()
d.printA()

# hierarchical inheritance

class A:
    def printA(self):
        print("this is class A")

class B(A):
    def printB(self):
        print("this is class B")

class C(A):
    def printC(self):
        print("this is class C")


b = B()
b.printA()
c = C()
c.printC()

# multiple inheritance 

class A:
    def display(self):
        print("this is class A")

class B:
    def display(self):
        print("this is class B")

class C(A,B):
    def printC(self):
        print("this is class C")

c = C()
c.display()