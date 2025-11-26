# vars + data types:

# Simple data types:
#     strings: "text..." words.. no limits
#     int: 10
#     floats: 10.52
#     booleans: True/False, 1/0, something or nothing. 


# Design:

# efficiancy: (ram, cpu), speed.
# maintainability: modularity, decoupling, removing state, readability. 
# scalability: features, users, data

#var(reference)

# a reference - set a value with "=", data obj is stored in memory. 

# Interning. -256 to + 256 loaded automatically into memory. 

# x = 256
# y = 256

# print(id(x))
# print(id(y))

# Caching example (over 256)

# x = 3257
# y = 3257

# print(id(x))
# print(id(y))

# print(x is y) # checks object is the smae not liuke ""=="" which checks the value. 

# def test():
#     a = int(str(257))
#     return a

# def test1():
#     b = int(str(257))
#     return b

# print(test() is test1())

# naming convention: descriptive, consistant, simple, good use of comments. 

# comments example for a function:
# top line comments
# def test1():
#     """
#     decription:
#     inputs:
#     outputs:
#     """
#      b = int(str(257))
#      return b

# Scope (global vs local, shadowing, global - binding vs mutating.)

# global_variable = "accessible everywhere"

# def test():
#     local_variable = "accessible only inside this function"
#     global global_variable
#     global_variable = "what will this do?" # shadowing
#     # print(global_variable)
#     # print(local_variable)


# test()
# print(global_variable)


# mutation: change but dont rebuild:

# obj_list = []

# def test1(x):
#      obj_list.append(x) # mutation - x changes but nothing is rebuilt.

# test1("obj1")
# test1("obj2")

# print(obj_list)

# # Rebinding:

# def rebind_list():
#     global obj_list
#     obj_list = ["obj3"] # rebinding not mutating

# rebind_list()
# print(obj_list)

# # nonlocal

# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x += 5
#     inner()
#     print(x)



# outer()

# inspect + traceback

# import inspect
# import traceback

# def function_a():
#     return function_b()

# def function_b():
#     return function_c()

# def function_c():
#     print("the call stack was: ")
#     traceback.print_stack()

# function_a()

# THis probably wont be picked up. 


# this will be retrived as the immediate preceeding comment
# def example(x, y):
#     """
#     Description: Adds togeather 2 integers
#     Input: both integers
#     Output: x + y 
#     """
#     return num1 + num2


# print(inspect.getdoc(example))
# print(inspect.getcomments(example))
# print(inspect.signature(example))
# print(inspect.getsource(example))


# concat/BODMAS/string methods

name = input("Enter your name: ")
age = int(input("enter an age: "))

# print("name is " + name + " and age is " + age)
# print("name is ", name, "age is ", age)
print(f"name is {name.upper()} and age is {age**2}")

pi = 3.142548

print(f"{pi:.2f}")
print(f"{"String":^10}")

print("Person1: \thello, how are you?\nPerson2: \tGood!\U0001f604")

AI breakdown:

Strings, ints, floats, booleans
Efficiency, maintainability, scalability
Variables store references
Integer interning (-256 to +256)
is checks identity, == checks value
Naming conventions matter
Comments + docstrings for functions
Scope: global vs local
Shadowing, mutation, rebinding
global and nonlocal keywords
Mutation modifies, rebinding replaces
inspect and traceback for introspection
Concatenation, f-strings, formatting
String methods (upper, etc.)
BODMAS operator ordering
x = (3 + ((5 * 9) / 5)) steps: multiply → divide → add → assign