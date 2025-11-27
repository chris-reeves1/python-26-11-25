# if, else, else if (elif).

# basic_syntax
# if condition is True:
#     block of code to Run
# else:
#     block of code if the if was false. 

# on_holiday = True
# is_admin = False
# is_verified = True

# if (is_admin or is_verified) and not on_holiday:
#     print("access allowed")
# else:
#     print("no access!!")

# import dis

# def example():
#     x = 0
#     while x < 3:
#         print("something...")
#         x += 1

#dis.dis(example)


#temp = 37

# if temp >= 30:
#     print("too hot")
# if temp > 25 and temp < 30:
#     print("nice")
# if temp > 10 and temp < 25:
#     print("ok")

# if temp != 30:
#     print("too hot")
# elif temp > 25:
#     print("nice")
# elif temp > 10:
#     print("ok")


# deposit = 100
# password = "password"

# if 0 < deposit < 1000 and password == "password":
#     print("deposited!")
# else:
#     print("could not deposit. ")

# if not 0 < deposit < 1000 and password != "password":
#     print("could not deposit. ")
# else:
#     print("deposited")


# user = "root"

# if user not in ("root", "admin", "user"):
#     print("accepted")
# else:
#     print("not accepted username")

# Exercise:
#     - weight converter
#     - user to input weight
#     - user to select either Kgs or Lbs
#     - logic: check the unit entered
#     - logic: calculate the conversion
#     - print out the result nicely!!
#     - Stretch: Error handling for incorrect unit type (upper/lower, else/while loop) 
#     - Optional: Error handling for non-numeric inputs for weight. 

# Try catch 

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print(f"exception caught: {str(e)}")
# except Exception as e:
#     print(f"exception caught: {str(e)}")
# finally:
#     print("optional clean up actions go here. ")


import sys

while True:
    try:
        weight = int(input("enter numeric weight: ")) # if error raised here no further code is run
        break
    except ValueError as e:
        print("[ERROR] - Must be numeric input!")
        sys.exit()

while True:
    unit = input("enter the unit K or L: ").lower()
    if unit == "k":
        convert = weight * 2.2
        print(convert)
        break
    elif unit == "l":
        convert = weight / 2.2
        print(convert)
        break
    else:
        print("PLS enter a K or L !!")



