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

def sumUntilzero(number):
    sum=0
    while not number==0:
        sum=sum+number
        number=int(input("Enter the number: "))
    return sum

number=int(input("Enter the number: "))
result=sumUntilzero(number)
print(f"Sum = {result}")