

#Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    sum=0
    for x in numbers:
        sum=x*x+sum
    return sum

numbers=eval(input("Enter list: "))
print(square_sum(numbers))