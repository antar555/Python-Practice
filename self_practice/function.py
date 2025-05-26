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

# def descending_order(num):
#     if num==0:
#         return 0
#     numbers=[]
#     while num!=0:
#         temp=num%10
#         num=num//10
#         numbers.append(temp)
#     numbers.sort(reverse=True)
#
#
#     return (int(''.join(str(i) for i in numbers)))
#
#
# num=int(input("Enter the number: "))
#
# print(descending_order(num))

# def do_math(your_string):
#     your_string = your_string.split()
#     combined = []
#     # print(your_string)
#     another_string_digit = ""
#     another_string_letter = ""
#     for word in your_string:
#         temp_digit = ""
#         temp_letter = ""
#         for char in word:
#             if char.isdigit():
#                 temp_digit = temp_digit + char
#             elif char.isalpha():
#                 temp_letter = temp_letter + char
#         combined.append((temp_letter, temp_digit))
#
#         another_string_letter = another_string_letter + temp_letter + " "
#         another_string_digit = another_string_digit + temp_digit + " "
#
#     combined.sort()
#
#     # print(another_string_digit.strip())
#     # print(another_string_letter.strip())
#     # print(combined)
#
#     numbers = []
#     for item in combined:
#         numbers.append(int(item[1]))
#
#     result = numbers[0]
#
#     for i in range(1, len(numbers)):
#         if (i - 1) % 4 == 0:
#             result = result + numbers[i]
#         elif (i - 1) % 4 == 1:
#             result = result - numbers[i]
#         elif (i - 1) % 4 == 2:
#             result = result * numbers[i]
#         elif (i - 1) % 4 == 3:
#             result = result // numbers[i]
#
#     return result
#
# your_string="24z6 1x23 y369 89a 900b"
# print(do_math(your_string))

# number=12
# for i in range(1,13,1):
#     if number%i==0:
#         print(i)
# https://www.codewars.com/kata/5e030f77cec18900322c535d/train/python



# def hit_or_stay(hand,next_card):
#     has_ace_in_hand = False
#     has_ace_next=False
#     sum=0
#     if next_card in ['K','Q','J','T']:
#         next_card=10
#
#     elif next_card=='A':
#         next_card=11
#         has_ace_next=True
#     else:
#         next_card=int(next_card)
#
#
#
#     for val in hand:
#         if val=='K' or val=='Q' or val=='J' or val=='T':
#             sum=sum+10
#
#         elif val=='A':
#             sum=sum+11
#             has_ace_in_hand=True
#
#         else:
#             sum=sum+int(val)
#
#     if sum>21 and (has_ace_in_hand or has_ace_next):
#         sum=sum-10
#
#
#     if sum<17:
#         sum=sum+next_card
#         if sum > 21 and (has_ace_in_hand or has_ace_next):
#             sum = sum - 10
#         return ['hit',sum]
#     elif sum>17:
#         if sum > 21 and (has_ace_in_hand or has_ace_next):
#             sum = sum - 10
#         return ['stay',sum]
#     elif sum==17:
#         if 'A' in hand:
#             sum=sum+next_card
#             if sum > 21 and (has_ace_in_hand or has_ace_next):
#                 sum = sum - 10
#             return ['hit',sum]
#         else:
#             return ['stay',sum]
#
#
# hand=[5,'A']
# next_card='A'
# print(hit_or_stay(hand,next_card))

def is_triangle(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        return True
    else:
        return False

a,b,c=1,2,2
print(is_triangle(a,b,c))












