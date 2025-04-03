# name=input("Enter your name: ")

# if name=="":
#     print("You did not enter your name: ")
# else:
#     print(f"Hello {name}")

# while name=="":
#     print("You did not enter your name: ")
#     name=input("Enter your name: ")
# print(f"Hello {name}")

# while name=="":
#     print("You did not enter your name: ")
#     name=input("Enter your name: ")
# print(f"Hello {name}")

# while name=="":
#     print("You did not enter your name: ")
#     name=input("Enter your name: ")
# print(name)

# age=int(input("Enter your age: "))
#
# while age<0:
#     print("You did not enter the valid age: ")
#     age=int(input("Enter your age: "))
# print(f"your age is: {age}")

# food=input("Enter the food you like (q to quit): ")
#
# while not food=="q":
#     print(f"You like {food}")
#     food=input("Enter another food you like: ")
# print("bye")

# food=input("Enter your favourite food: ")
#
# while not food=="q":
#     print(f"This is your favourite {food}")
#     food=input("Enter your another favorite food: ")
#
# print("Bye")

# principle=0
# rate=0
# time =0
#
# while principle<=0:
#     principle=float(input("Enter the principle amount: "))
#     if principle<=0:
#         print("Principle can't be less than or equal to zero")
#
#
#
# while rate<=0:
#     rate=float(input("Enter the interest rate: "))
#     if rate<=0:
#         print("Interest Rate can't be less than or equal to zero")
#
#
#
# while time<=0:
#     time=int(input("Enter the Time in years: "))
#     if time<=0:
#         print("Time can't be less than or equal to zero")
#
#
# total=principle*pow((1+rate/100),time)
# print(f"Balance after {time} year/s: ${total:.2f}")


principle=0
rate=0
time =0

while True:
    principle=float(input("Enter the principle amount: "))
    if principle<0:
        print("Principle can't be less than  zero")
    else:
        break



while True:
    rate=float(input("Enter the interest rate: "))
    if rate<0:
        print("Interest Rate can't be less than  zero")
    else:
        break



while True:
    time=int(input("Enter the Time in years: "))
    if time<0:
        print("Time can't be less than  zero")
    else:
        break


total=principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s: ${total:.2f}")

#While True will continue forever, need if for condition and else for break