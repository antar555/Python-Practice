#Printing Pattern 1

def pattern1(number):
    for i in range(0, number,1):
        for j in range(0,number,1):
            print("*", end=" ")
        print()

number=int(input("Enter the number of line: "))
pattern1(number)

#Printing Pattern 2

def pattern2(number):
    for i in range(0,number,1):
        for j in range(1,number+1,1):
            print(j, end=" ")
        print()

number=int(input("Enter the number: "))
pattern2(number)

#pattern 3

def pattern3(number):
    for i in range(0,number+1,1):
        for j in range(1,i+1,1):
            print("*", end=" ")
        print()

number=int(input("Enter the number: "))
pattern3(number)