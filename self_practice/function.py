# def add(number1,number2):
#     result=number1+number2
#     get_result(result)
#
# def get_result(result):
#     print(result)
#
# def validate_numbers(number1,number2):
#     while True:
#         if number1 and number2<0:
#             number1=int(input("Enter the number 1: "))
#             number2=int(input("Enter the number 2: "))
#         else:
#             break
#
#
# number1=int(input("Enter the number 1: "))
# number2=int(input("Enter the number 2: "))
#
# add(number1,number2)

# def check_for_factor(base,factor):
#     if base%factor==0:
#         return True
#     else:
#         return False
#
# base=int(input("Enter the base: "))
# while True:
#     if base<0:
#         base=int(input("Enter the base: "))
#     else:
#         break
# factor=int(input("Enter the factor: "))
# while True:
#     if factor<0:
#         factor=int(input("Enter the factor: "))
#     else:
#         break
# print(check_for_factor(base,factor))

# def add(number1, number2):
#     print(number1+number2)
#
# def input_number():
#     number1=int(input("Enter the number1: "))
#     while number1<0:
#         number1=int(input("Enter the number1: "))
#
#     number2=int(input("Enter the number2: "))
#     while number2<0:
#         number2=int(input("Enter the number2: "))
#
#     add(number1,number2)
#
#
# input_number()

# def enough(cap,on,wait):
#     x=cap-on
#
#     if wait<=x:
#         return 0
#     else:
#         return max(0,wait-x)
# cap=int(input("Enter the capacity: "))
# on=int(input("Enter onboard: "))
# wait=int(input("Enter the waiting people number: "))
# print(enough(cap,on,wait))

def descending_order(num):
    if num==0:
        return 0
    numbers=[]
    while num!=0:
        temp=num%10
        num=num//10
        numbers.append(temp)
    numbers.sort(reverse=True)


    return (int(''.join(str(i) for i in numbers)))


num=int(input("Enter the number: "))

print(descending_order(num))
