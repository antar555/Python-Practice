#Printing Pattern 1

# def pattern1(number):
#     for i in range(0,number,1):
#         for j in range(1,number+1,1):
#             print(f"{j}",end=" ")
#         print()

def pattern1(number):
    for i in range(0,number,1):
        for j in range(0,number,1):
            print("*",end=" ")
        print()




number=int(input("Enter the number of lines: "))
pattern1(number)