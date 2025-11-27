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

# drinks = {"still": "water", "fizzy": "cola", "juice": "orange"}

#print(drinks["fizzy"])

# print(drinks.items())
# print(drinks.values())


# print(drinks.get("fizzzy")) 

# exercise:
#     - Make a dictionary, with keys as authors(2-3) and books(2-3) as values.
#     - input asking for an author name.
#     - print a string of the books.
#     - Error handling for incorrect keys must be implemented.
#     - Try to only use things we've covered. 


# book_dictionary = {
# 	"N.T. Wright": ["The Bible for Everyone: A New Translation", "Surprised by Hope: Rethinking heaven, the resurrection and the mission of the Church"],
# 	"Martin Luther": ["95 Theses", "The Bondage of the Will", "Table Talk"],
# 	"Karl Barth": ["Church Dogmatics", "The Epistle to the Romans"]
# }

# author = input("Enter the name of the author: ")

# if author in book_dictionary:
# 	print("Books by " + author + ": ")
# 	books = ", ".join(book_dictionary[author])
# 	print(books)
# else:
# 	print("Cannot find any book by the author.")

# booklist = {

#     "J.K. Rowling": [
#         "Harry Potter and the Sorcerer's Stone",
#         "Harry Potter and the Chamber of Secrets",
#         "Harry Potter and the Prisoner of Azkaban"
#     ],
#     "Roald Dahl": [
#         "Charlie and the Chocolate Factory",
#         "Matilda",
#         "James and the Giant Peach"
#     ],
#     "Sheila McCullagh": [
#         "The Land of the Blue Flower",
#         "Tim and the Hidden People",
#         "The Village with Three Corners"
#     ]
# }

# print("Availible authors:")
# print(", ".join(booklist.keys()))

# author = input("please enter an authors name " )

# books = booklist.get(author, []) #or ["sorry no books found"] "sorry no books found"

# print(", ".join(books) or "no books found")

# JacksBookshop = {
#   "author1": {
#   "name": "Rick Riordan",
#   "book1": "The Lightning Thief", 
#   "book2": "The Sea of Monsters", 
#   "book3": "The Last Olympian",
# },
#   "author2": {
#   "name": "Jonathan Haidt",
#   "book1": "The Happiness Hypothesis", 
#   "book2": "The Righteous Mind",
#   "book3": "The Anxious Generation",  
# },
#   "author3": {
#   "name": "Colleen Hoover", 
#   "book1": "It Ends With Us",
#   "book2": "Verity",
#   "book3": "Hopeless",    
# }
# }
# y = JacksBookshop.get("author2").get("name")
# print(y)

# record  = JacksBookshop.get("author2")

# list_to_print = []

# for a, b in record.items():
#     if "book" in a:
#         list_to_print.append(b)

# print(", ".join(list_to_print))


- think about structure, add book details into 
    the dictionary (publisher, date, genre, isbn, type)


- Attempt look up logic for author name (case, (partial matches - just think about))