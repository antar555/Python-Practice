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

def check_for_factor(base,factor):
    if base%factor==0:
        return True
    else:
        return False

base=int(input("Enter the base: "))
while True:
    if base<0:
        base=int(input("Enter the base: "))
    else:
        break
factor=int(input("Enter the factor: "))
while True:
    if factor<0:
        factor=int(input("Enter the factor: "))
    else:
        break
print(check_for_factor(base,factor))