# classes

# OOP:
    # - encapsulation - privacy. 
    # - polymorphism - objects can take on traits of sub types, methods can be overridden, overloaded.
    # - inheritance: child inherits all attributes + methods from parent class.
    # - abstraction: dont need to see the code.  

# structure, object creation (custom object types), state + coupling.  

# classes:
    # - extends the language
    # - allows custom objects
    # - have its own behaviour through methods.

# class Example:
#     # attributes
#     name = "chris"

#     # methods
#     def greet(self):
#         print(f"hello {self.name}")

# ob1 = Example()

# ob1.name = "c"
# ob1.email = "..."

# ob1.greet()

# class Students:
#     def __init__(self, first_name, last_name, age=10):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full = first_name + " " + last_name


# student1 = Students("c", "B", 12)
# print(student1.full)

# class Students:

#     def __init__(self, first_name, last_name, age=10):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         # self.full = first_name + " " + last_name

#     def fullName(self):
#         return self.first_name + " " + self.last_name

# student1 = Students("c", "B", 12)
# print(student1.fullName())
# print(Students.fullName(student1))

# using external methods

# from types import MethodType
# import builtins

# def outside(self):
#     return f"{self.first_name} was the caller"

# student1.outside = MethodType(outside, student1)
# print(student1.outside())

# def outside_class(self):
#     return f"{self.first_name} was the caller"

# Students.outside_class = outside_class
# #print(Students.outside_class(student1))
# #print(student1.outside_class())

# self class variables

# class Students:
#     age_increase_amount = 1

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         # self.full = first_name + " " + last_name

#     def fullName(self):
#         return self.first_name + " " + self.last_name

#     def changeAge(self): # setters
#         self.age = self.age + self.age_increase_amount


# student1 = Students("C", "D", 12)
# student2 = Students("A", "B", 10)
# print(student1.__dict__)
# print(student2.__dict__)
# student1.changeAge()
# student2.age_increase_amount = 10
# student2.changeAge()
# student1.changeAge()
# print(student1.__dict__)
# print(student2.__dict__)
# print(Students.__dict__)

# non self class variables

# class Students:
#     age_increase_amount = 1
#     __num_of_students = 0

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         # self.full = first_name + " " + last_name

#         Students.__num_of_students += 1 # name mangling

#     def fullName(self):
#         return self.first_name + " " + self.last_name

#     def changeAge(self): # setters
#         self.age = self.age + self.age_increase_amount

#     @classmethod
#     def get_num_of_students(cls):
#         return cls.__num_of_students


# student1 = Students("C", "D", 12)
# student2 = Students("A", "B", 10)
# print(Students.get_num_of_students())
# print(Students._Students__num_of_students)

# Inheritance

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def eat(self):
#         print(f"{self.name} eats...")

#     def __str__(self):
#         return f"Animal({self.name}, {self.species})"

    # def __repr__(self):
    #     return f"Animal({self.name!r}, {self.species!r})"

# a = Animal("x", "y")

# print(a)
# b = eval(repr(a)) # runs single line python code
# print(a)


# class Cat(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

#     #@Override 
#     def eat(self):
#         print(f"{self.name} as a cat not an animal eats...")

#     def __str__(self):
#         return super().__str__() + f"{self.__class__.__name__}{self.__dict__}, {self.breed}"


# cat1 = Cat("x", "y", "z")
# print(cat1)
# cat1.eat()

# Todo:

# - Finish previous labs
# - classes lab
# - extra classes challenges
# - Research/reading/revision
# - rock paper scissor as class. 

#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account. 

#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 