# Repeatability + abstraction 

# def greet(name, age): # params
#     return f"hello {name} aged: {age}" # use as vars

# print(greet("c", age=20))

# def greet(first, last="B", age=30):
#     print(f"hello {first}, aged: {age}")

# greet()

# *args 
# Dont know how many positional args need to be passed through. Passed as a tuple.

# def make_pizza(size, *toppings):
#     print(F"Order for {size} pizza, with the following topppings:")
#     for topping in toppings:
#         print(topping)

# make_pizza("large", "mushrooms", "peppers")

# **kwargs
# unkown number of key word args

# def order(**stuff):
#     print("Order:")
#     for k, v in stuff.items():
#         print(f"{k} + {v}")

# order(main="pasta", drink="cola", side="fries")

# def combined(*args, **kwargs):
#     print(args)
#     print(kwargs)

# combined(1, "a", 3, a=4)

# / * 
# all args before / must be positional.  
# All args after * must be keyword args. 
# Enforced!!

# def example(a, b, /, *, c, d):
#     print(f"a: {a} b: {b} c: {c} d: {d}")

# example(1, 2, 3, d=4)

# def maths_ops(a, b, /, operation="add", *, decimal_place=None):
#     if operation == "add":
#         result = a + b
#     elif operation == "subtract":
#         result = a - b
#     else:
#         raise TypeError("Only add or subtract pls!!")
#     return round(result, decimal_place)

# print(maths_ops(2, 5))
# print(maths_ops(2, 5, "add"))
# print(maths_ops(2, 5, operation="subtract"))
# print(maths_ops(2.25651155, 5.3235656887, operation="subtract", decimal_place=5))
# print(maths_ops(2, 5, 3, 5, 6, 7, operation="subtract"))


# Recursion:

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#        return n * factorial(n - 1)

# print(factorial(5))

# Frame:
#     - Stores each function call
#     - locals(), globals().
#     - code object (f_code)
#     - calling context


# stack:
#     - stack of frames, ordered from recent to oldest. 
#     - pops the functions (deletes + returns it return)


# import inspect

# def test_function():
#     print("name: ", inspect.currentframe().f_code.co_name)
#     print("stack: ", inspect.stack()[0].function)
#     x = "hello"
#     print(locals())
#     for f in inspect.stack():
#         print(f.function)

# def call():
#     test_function()

# call()
# print(locals())
# print(locals() == globals())

# lambdas:

# discrete one line unnamed(mostly) functions. 

# lambda args : expression (iterables)

# add_function = lambda x , y : x + y

# print(add_function(2, 3))

# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x**2, numbers)

# print(list(squared))


# break here till tomoro:
# todo:
# lab 5 and 6
# practice function challenges if needed
# rock, paper, scissor game user vs computer (track stats for wins/rounds/loses etc)
# or... go back through the notes (*args, **kwargs, /, * etc)


# higher-level functions

# def square(x):
#     return x * x

# def apply_func(func, value):
#     return func(value)

# print(apply_func(square, 10))

# def get_input():
#     return input("Enter something...")

# for item in iter(get_input, "quit"):
#     print(f"Entered {item}")


# wrappers:

# def simple_wrapper(func):
#     def wrapped(*args, **kwargs):
#         print("calling wrapped function")
#         return func(*args, **kwargs)
#     return wrapped


# @simple_wrapper
# def greet(name, age):
#     """
#     Greets with a name and age
#     """
#     print(f"hello {name} + {age}")


# print(greet.__name__)
# print(greet.__doc__)
# greet("c", 10)

from functools import wraps, lru_cache
import time

# def simple_wrapper(func):
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         print("calling wrapped function")
#         return func(*args, **kwargs)
#     return wrapped


# @simple_wrapper
# def greet(name, age):
#     """
#     Greets with a name and age
#     """
#     print(f"hello {name} + {age}")


# print(greet.__name__)
# print(greet.__doc__)
# greet("c", 10)


# @lru_cache(maxsize=None)
# def add(a, b):
#     print("waiting...")
#     time.sleep(10)
#     return a + b

# print(add(2, 3))
# print(add(2, 3))