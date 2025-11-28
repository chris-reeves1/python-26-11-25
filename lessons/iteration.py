# for loops/ while loops
# saves time + reduces code duplication. 

# while loops

# need a condition to get started
# need a condition to stop the loop
# Otherwise would never end. 

# count = 0 
# while count < 101:
#     print(count)
#     count += 1

# break and continue

# i = 0
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# k = 0
# while k < 6:
#     k += 1 
#     if k == 3:
#         continue
#     print(k)

# for loops
# for iterating through iterables (strings, listss, dictionaries etc)

# fruits = ["apple", "oranges", "pears", "kiwi"]

# # for item in iterable:
# #     block of code.

# for fruit in fruits:
#     print(fruit)

# l = 0
# while l < len(fruits):
#     print(fruits[l])
#     l += 1

# Strings

# for word in "hello world".split():
#     print(word)

# # range

# for a in range(1, 10, 2):
#     print(a)

# # Dictionaries
# for i in {"drink": "cola"}:
#     print(i)

# for k, v in {"drink":"cola"}.items():
#     print(k, v)


# nested for loop
# for i in range(3):
#     for k in range(2):
#         print(i, "x", k, "=", i * k)

# list comp
# to make or change lists

    #        expression        item      iterable
# result = [x**2             for x in       range(5)]
# print(result)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_squared = [x**2 for x in numbers if x % 2 == 0]
# print(even_squared)



# TASK:
# loop to get 5 names as inputs + prints with "is awesome" added to it. 

# while loop
# for loop
# list comp
# STRETCH GOAL: list comp one line only! 

# inner 
# [input("enter name") for n in range(5)]

# outer
# [print(f"y is awesome") for y in iterable]

# x = [print(f"{y} is awesome") for y in [input("enter name") for n in range(5)]]

# print(x)
