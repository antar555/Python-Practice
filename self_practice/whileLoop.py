#Sum Until Zero
#reading numbers until the user enters 0. Output the sum of all entered numbers.

def sumUntilzero():

    number=int(input("Enter the number: "))
    sum=0
    while not number==0:
        sum=sum+number
        number=int(input("Enter the number: "))
    print(f"Sum = {sum}")


sumUntilzero()