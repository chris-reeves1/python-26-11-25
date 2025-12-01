# Sam has been dumped by his girlfriend so he's gone into the local milk 
# bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
# milkshakes, 
# differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
# number corresponding 
# to the relevant flavour - this list is displayed every iteration. 
# If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
# If he orders but can't pay he's thrown out.


# budget = 20

# milkshakes = {
#     "1": (3, "Whole"),
#     "2": (4, "choc"),
#     "3": (5, "vanilla")
# }

# while True:
#     print("drinks menu:")
#     for option, (price, flavour) in milkshakes.items():
#         print(f"{option} - {flavour} - ${price}")

    
#     choice = input("enter you choice of drink? ")

#     if choice not in milkshakes:
#         print("invalid choice")
#         continue

#     if choice.upper() == "Q":
#         print("bye")
#         break

#     price, flavour = milkshakes[choice]
#     if price > budget:
#         print("kicked out!")
#         break
    
#     print(f"enjoy {flavour} drink")
#     budget -= price
#     print(f"budget is now {budget}")



# from typing import Dict
# budget = 20
# Menu = Dict[str, tuple[int, str]] # type alias - capitalised to show not a var. 
                                  # Has no affect - python doesnt enforce type ever. 
                                  # mypy is a static tool to check - best implemented in
                                  # a static code analysis pipeline.
                                  # updates to the structure propagtes though all calls. 

# milkshakes: Menu = {
#      "1": (3, "Whole"),
#      "2": (4, "choc"),
#      "3": (5, "vanilla")
#  }

# while True:
#     print("drinks menu:")
#     for option, (price, flavour) in milkshakes.items():
#         print(f"{option} - {flavour} - ${price}")

    
#     choice = input("enter you choice of drink? ")

#     if choice not in milkshakes:
#         print("invalid choice")
#         continue

#     if choice.upper() == "Q":
#         print("bye")
#         break

#     price, flavour = milkshakes[choice]
#     if price > budget:
#         print("kicked out!")
#         break
    
#     print(f"enjoy {flavour} drink")
#     budget -= price
#     print(f"budget is now {budget}")

# Above example: fails by type and expected size of the tuple. index errors are flagged.



# # typedDict example:

# from typing import TypedDict, Dict

# class Shake(TypedDict):
#     price: int
#     flavour: str

# milkshakes: Dict[str, Shake] = {
#     "1": {"price": 3, "flavour": "Milk"},
#     "2": {"price": 5, "flavour": "Choc"},
#     "3": {"price": 10, "flavour": "Strawberry"},
# }

# budget = 20

# while True:
#     print("Menu:")
#     for option, shake in milkshakes.items():
#         print(f"{option} - {shake['price']}:{shake['flavour']}")

#     choice = input("choice 1-3 pls or quit(q): ")

#     if choice.lower() == "q":
#         break
#     if choice not in milkshakes:
#         print("invalid choice")
#         continue

#     price = milkshakes[choice]["price"]
#     flavour = milkshakes[choice]["flavour"]

#     if price > budget:
#         print("get out")
#         break

#     print(f"{flavour} - milkshake served")
#     budget -= price
#     print(budget)

# namedTuples and @DataClass also available. 

# from typeguard import typechecked
# from typing import Dict, Tuple

# @typechecked
# def create_menu() -> Dict[str, Tuple[int, str]]:
#     return {
#         "1": (3, "Milk"),
#         "2": (5, "Choc"),
#         "3": (10, "Strawberry"),
#         "4": ("5", "Vanilla")   #  Runtime TypeError
#     }

# milkshakes = create_menu()

import sys, typeguard, importlib.metadata
print("Python", sys.version)
print("Typeguard:", importlib.metadata.version("typeguard"))

from typeguard import typechecked
@typechecked
def boom() -> tuple[int,str]:
    return ("5","milk")

boom()

