#Sum Until Zero
#reading numbers until the user enters 0. Output the sum of all entered numbers.

# def sumUntilzero():
#
#     number=int(input("Enter the number: "))
#     sum=0
#     while not number==0:
#         sum=sum+number
#         number=int(input("Enter the number: "))
#     print(f"Sum = {sum}")
#
#
# sumUntilzero()

# def sumUntilzero(number):
#     sum=0
#     while not number==0:
#         sum=sum+number
#         number=int(input("Enter the number: "))
#     return sum
#
# number=int(input("Enter the number: "))
# result=sumUntilzero(number)
# print(f"Sum = {result}")

# def sumUntilzero(number):
#     sum=0
#
#     while True:
#         if number!=0:
#             sum=sum+number
#             number=int(input("Enter the number: "))
#         else:
#             break
#     return sum
#
#
# number=int(input("Enter the number: "))
# result=sumUntilzero(number)
# print(f"Sum = {result}")

# def passCheck(password):
#     while not password=="secret123":
#         password=input("Enter the valid password: ")
#     print("Access Granted")
#
# password=input("Enter the password: ")
#
# passCheck(password)

# def passCheck(password):
#     while True:
#         if password!="secret123":
#             password=input("Enter the valid password: ")
#         else:
#             break
#     print("Access Granted")
#
# password=input("Enter the valid password: ")
# passCheck(password)

#print digits of a number

def print_digit(digit):
    while digit!=0:
        number=digit%10
        print(number)
        digit=digit//10

digit=int(input("Enter the digit: "))
print_digit(digit)