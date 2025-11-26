# basic structures:                                           
# list - [] - store any data type. mutable, indexed/ordered, [1, "1", True, ["1"]]
# dictionaries - {} (unique)key value pairs, mutable, unordered {"1": "Value", "2":"value"}
# tuples - () or nothing. read only lists.                                                   
# sets - unique values. (maths). 

# x = hash("hello")
# y = x % (16-1)
# print(x)


# import sys

# d = {}

# for i in range(80):
#     d[i] = i
#     print(sys.getsizeof(d))


# import time


# large_list = list(range(100_000_000))
# large_dict = {num : True for num in range(100_000_000)}

# target = 99_000_000

# start = time.time()
# list_result = target in large_list
# finish = time.time()
# print(f"result for list: {finish - start:.8f}")

# start = time.time()
# dict_result = target in large_dict
# finish = time.time()
# print(f"result for dictionary: {finish - start:.8f}")

# Methods

# colours = ["blue", "red", "yellow", "green"]

# colours[0] = "orange"
# print(colours[0:2])
# print(colours)

# colours.sort()
# print(colours)
# colours.sort(key=len)
# print(colours)

# x = ", ".join(colours)
# print(x)

# dictionaries

drinks = {"still": "water", "fizzy": "cola", "juice": "orange"}

#print(drinks["fizzy"])

# print(drinks.items())
# print(drinks.values())


print(drinks.get("fizzzy")) 

exercise:
    - Make a dictionary, with keys as authors(2-3) and books(2-3) as values.
    - input asking for an author name.
    - print a string of the books.
    - Error handling for incorrect keys must be implemented.
    - Try to only use things we've covered. 





