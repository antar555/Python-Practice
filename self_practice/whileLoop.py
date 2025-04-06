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

# def print_digit(digit):
#     while digit!=0:
#         number=digit%10
#         print(number)
#         digit=digit//10
#
# digit=int(input("Enter the digit: "))
# print_digit(digit)

#Factorial
# def factorial(number):
#     result=1
#     while number>0:
#         result=result*number
#         number=number-1
#     print(result)
#
# number=int(input("Enter the number: "))
# factorial(number)

#CountDown

# def countDown(number):
#     while number>0:
#         print(number)
#         number=number-1
#
# number=int(input("Enter the number: "))
# countDown(number)

#Reverse a number
# def reverse(number):
#     while number!=0:
#         temp=number%10
#         number=number//10
#         print(f"{temp}",end="")
#
# number=int(input("Enter the number: "))
# reverse(number)

#sum of digits

# def sum_of_digits(number):
#     sum=0
#     while number!=0:
#         temp=number%10
#         number=number//10
#         sum=sum+temp
#     return sum
#
# number=int(input("Enter the number: "))
# print(sum_of_digits(number))

#Even number sequence

# def even_number_sequence(number):
#
#     count=0
#     while True:
#         if number%2==0:
#             count=count+1
#             number=int(input("Enter the number: "))
#
#         else:
#             break
#     return count
#
# number=int(input("Enter the number: "))
# print(even_number_sequence(number))


# for i in range(110,115,1):
#     sum=0
#     while i!=0:
#         temp=i%10
#
#         i=i//10
#         sum=sum+temp
#
#     print(sum)

number=int(input("Enter a number: "))
original_number=number
get_number=[]
while number!=0:
    temp=number%10

    number=number//10
    get_number.append(temp)

    print(temp)
get_number.reverse()
print(get_number)

n=1
sum=0
for i in get_number:
    print(i**n)
    sum=sum+i**n
    n=n+1
print(sum)
if original_number==sum:
    print(f"{original_number} is a special number")
else:
    print("No")
