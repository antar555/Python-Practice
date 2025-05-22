# fruits=['apple','banana']
# fruits.append('orange')
# print(fruits)

# numbers=[1,2,4,5]
# numbers.insert(2,3)
# print(numbers)

# colors=['red','green']
# colors.extend(['blue','yellow'])
# print(colors)

# animals=['cat','dog']
# animals.append(['lion','tiger'])
# print(animals)

# list1=[10,20]
# list2=[30,40]
# list1.extend(list2)
# print(list1)

# tasks=["wakeup","brush teeth"]
# tasks.insert(1,'open eyes')
# print(tasks)

# shopping=[]
# for i in range(1,4):
#     items=input("Enter the items: ")
#     shopping.append(items)
# print(shopping)

even_numbers=[]
# for i in range(2,11):
#     if i%2==0:
#         even_numbers.append(i)
# print(even_numbers)

# number=2
# while number%2==0 and number<=10:
#     even_numbers.append(number)
#     number=number+2
# print(even_numbers)

# def count_positives_count_negatives(arr):
#     if not arr:
#         return []
#     arr_new=[]
#     count_positives=0
#     sum_negatives=0
#     for i in arr:
#         if i>0:
#             count_positives+=1
#
#         elif i<0:
#             sum_negatives+=i
#
#
#
#     arr_new.append(count_positives)
#     arr_new.append(sum_negatives)
#     return arr_new
#
#
# #arr=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
# arr=[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
# print(count_positives_count_negatives(arr))

# def numbers(elements):
#     count=0
#
#     # for i in range(len(elements)):
#     #     for j in range(len(elements)):
#     #         if i!=j and elements[i]==elements[j]:
#     #             count+=1
#     #
#     # print(count)
#     # for i in elements:
#     #     if elements.count(i)==1:
#     #         count=count+1
#     #         print(i)
#     # print(count)
#
#     another_list=[]
#     for i in elements:
#         if elements.count(i)>1 and i not in another_list:
#             another_list.append(i)
#             count=count+1
#
#     print(another_list)
#
#
#
#
#     print(f"total number of unique duplicates: {count}")








# elements=list(map(int, input("Enter the elements: ").split()))
# numbers(elements)







# def unique_duplicates(elements):
#     count=0
#     another_list=[]
#     another_another_list=[]
#     for i in elements:
#         if elements.count(i)>1:
#             another_list.append(i)
#
#     print(another_list)
#     for i in another_list:
#         if i not in another_another_list:
#             another_another_list.append(i)
#             count+=1
#
#     print(another_another_list)
#     print(count)
#
#
# elements=list(map(int, input("Enter the numbers: ").split()))
# unique_duplicates(elements)

# def first_duplicate(elements):
#     for i in elements:
#         if elements.count(i)>1:
#             print(i)
#             break
#
#
# elements=list(map(int, input("Enter the elements: ").split()))
# first_duplicate(elements)

# def indices(elements):
#     sum=0
#
#     for i in elements:
#         sum=sum+i
#
#
#
#     print(sum)
#
# elements=list(map(int, input("Enter the elements: ").split()))
# indices(elements)


# def find_difference(a,b):
#     mul_a=1
#     mul_b=1
#     for i in a:
#         mul_a=i*mul_a
#     for j in b:
#         mul_b=j*mul_b
#     return abs(mul_a-mul_b)
#
# a=list(map(int, input("Enter the list a: ").split()))
# b=list(map(int,input("Enter the list b: ").split()))
# print(find_difference(a,b))

#Create a list of five fruits. Replace the third fruit with "Mango".
# list=["Pineapple","Orange","apple","Lemon","Pitch"]
# list[2]="Mango"
# print(list)

#Given a list of five numbers, change the last two numbers to "Ten" and "Twenty".
# list=[1,2,3,4,5]
# list[3:5]=[10,20]
# print(list)

#You have a list of countries. Replace the second and third countries with "Canada", "Brazil", and "Germany".
# list=["America","India","Singapore","Norway","Italy"]
# list[1:4]=["Canada","Brazil","Germany"]
# print(list)

#Given a list of colors, replace the first two colors with only one color "Purple".
# list=["Blue","White","Orange","Red"]
# list[0:2]=["Purple"]
# print(list)

#Create a list of your favorite movies. Insert "Inception" at the second position.
# list=["Superman","Man of steel","Batman"]
# list.insert(1,"Inception")
# print(list)





# You have a list of students.
# Remove the second and fourth students without using slicing — only using pop() or remove().

# students=["X","Y","Z","C","B"]
# students.pop(1)
# students.remove("Z")
# print(students)

#Create a list of 7 random numbers.
# Delete the third and last elements using two different methods (e.g., del for one and pop() for another).

# import random
# numbers=[]
# for i in range(0,6):
#     numbers.append(random.randint(1,100))
# print(numbers)
# del numbers[2]
# numbers.pop(4)
# print(numbers)


# Given a list of fruits, remove "Apple" by value.
# Then, remove the first item by index.
# Finally, clear the entire list but do not delete the list itself.

# fruits=["Apple","Orange","Mango","Pineapple"]
# fruits.remove("Apple")
# print(fruits)
#
# fruits.pop(0)
# print(fruits)
#
# fruits.clear()
# print(fruits)

# Create a list with mixed elements (names and numbers).
# Delete only all the number elements without using a loop (hint: you may need multiple remove() calls manually).

# list=["Antar","Keya","Garbita",1,2,3]
# updated_list=[]
# for i in list:
#     if not isinstance(i,int):
#         updated_list.append(i)
# print(updated_list)

# city=["Dhaka","Chittagong","Mumbai","London","Paris","Sydney"]
# del city[5]
# print(city)
# city.remove("Paris")
# print(city)
# del city

# def filter_list(l):
#     new_list=[]
#
#     for element in l:
#         if isinstance(element,int):
#             new_list.append(element)
#     return new_list
#
#
# l=[1,2,'a','b']
# print(filter_list(l))
# numbers=[1,2,3,4,5]
# minimum_index=numbers.index(numbers)
# print(minimum_index)

# def process_data(data):
#     multiply=1
#     for element in data:
#         multiply=multiply*(element[0]-element[1])
#     return multiply
#
# data=[[2,5],[3,4],[8,7]]
# print(process_data(data))

# your_string="24z6 1x23 y369 89a 900b"
# your_string=your_string.split()
# combined=[]
# # print(your_string)
# another_string_digit=""
# another_string_letter=""
# for word in your_string:
#     temp_digit=""
#     temp_letter=""
#     for char in word:
#         if char.isdigit():
#             temp_digit=temp_digit+char
#         elif char.isalpha():
#             temp_letter=temp_letter+char
#     combined.append((temp_letter,temp_digit))
#
#
#
#     another_string_letter=another_string_letter+temp_letter+" "
#     another_string_digit=another_string_digit+temp_digit+" "
#
# combined.sort()
#
#
#
#
# # print(another_string_digit.strip())
# # print(another_string_letter.strip())
# # print(combined)
#
# numbers=[]
# for item in combined:
#
#     numbers.append(int(item[1]))
#
# result=numbers[0]
#
# for i in range(1,len(numbers)):
#     if (i-1)%4==0:
#         result=result+numbers[i]
#     elif (i-1)%4==1:
#         result=result-numbers[i]
#     elif(i-1)%4==2:
#         result=result*numbers[i]
#     elif(i-1)%4==3:
#         result=result//numbers[i]
#
#
#
#
# print(result)
# print(numbers)

# def hit_or_stay(hand, next_card):
#     ace_next_card=False
#     sum=0
#     if next_card in ['K','Q','T','J']:
#         next_card=10
#     elif next_card=='A':
#         next_card=11
#         ace_next_card=True
#
#     else:
#         next_card=int(next_card)
#     for val in hand:
#         if val in ['K','Q','T','J']:
#             sum=sum+10
#         elif val=='A':
#             sum=sum+11
#         else:
#             sum=sum+int(val)
#
#     if sum>21 and 'A' in hand:
#         sum=sum-10
#     if sum<17:
#         sum=sum+next_card
#         if 'A' in hand and sum>21:
#             sum=sum-10
#         elif ace_next_card and sum>21:
#             sum=sum-10
#         return ['hit',sum]
#     elif sum>17:
#         if 'A' in hand and sum>21:
#             sum=sum-10
#
#         return ['stay',sum]
#     elif sum==17:
#
#         if 'A' in hand or sum>21:
#             sum=(sum+next_card)-10
#             return ['hit',sum]
#         else:
#
#             return ['stay',sum]
#
#
#
#
# hand=['J',3]
# next_card='A'
# print(hit_or_stay(hand,next_card))

# def sum_of_products(a):
#     sum=0
#     mul=1
#     if len(a)==2:
#         for val in a:
#             sum = sum + val
#
#         for val in a:
#             mul = mul * val
#
#         sum = sum + mul
#         return sum
#
#
#
#
#     else:
#         for val in a:
#             sum = sum + val
#
#         for val in a:
#             mul = mul * val
#
#         sum = sum + mul
#
#
#         for i in range(len(a)):
#             for j in range(i+1,len(a)):
#                 sum=sum+a[i]*a[j]
#
#         return sum
#
#
#
#
#
#
#
#
# a=[12,13]
# print(sum_of_products(a))

# def likes(names):
#     new_name=[]
#     if not names:
#         return "no one likes this"
#     else:
#         for name in names:
#             new_name.append(name)
#         if len(new_name)==3:
#
#             return f"{', '.join(new_name[:-1])} and {new_name[-1]} like this"
#         elif len(new_name)==2:
#             return f"{' and '.join(new_name)} like this"
#
#         elif len(new_name)==1:
#             return f"{new_name[0]} likes this"
#
#         else:
#             return f"{new_name[0]}, {new_name[1]} and {len(new_name)-2} others like this"
#
#
#
# names=["Peter","Tony","Spidey"]
# print(likes(names))

# numbers=[1,2,3]
# for num in numbers:
#     print(num,end=" ")


# numbers=[19,5,42,2,77]
# new_numbers=[]
#
# min_num=min(numbers)
#
# for num in numbers:
#     if num>min_num:
#         new_numbers.append(num)
#
# print(new_numbers)
#
# print(min(new_numbers)+min_num)

# def sum_two_smallest_numbers(numbers):
#     new_numbers=[]
#     min_num=min(numbers)
#     for num in numbers:
#         if num>min_num:
#             new_numbers.append(num)
#
#     min_new_num=min(new_numbers)
#     return min_new_num+min_num
#
# numbers=[5, 8, 12, 18, 22]
# print(sum_two_smallest_numbers(numbers))

# def square_sum(numbers):
#     sum=0
#     for num in numbers:
#         sum=num*num+sum
#     return sum
# numbers=[]
# print(square_sum(numbers))

# class SquareSum:
#     def __init__(self,numbers):
#         self.numbers=numbers
#         self.sum=0
#         for num in self.numbers:
#             self.sum=num*num+self.sum
#
#     def __str__(self):
#         return f"Square Sum: {self.sum}"
#
#
# SquareSum1=SquareSum([1,2,4])
# print(SquareSum1)


# class Volume:
#     def __init__(self,length,width,height):
#         self.length=length
#         self.width=width
#         self.height=height
#         self.result=self.length*self.width*self.height
#
#     def get_volume_of_cuboid(self):
#         return self.result
#
#
#
#
# Volume1=Volume(1,2,3)
# print(Volume1.get_volume_of_cuboid())


# def two_highest(arg1):
#     if not arg1:
#         return []
#
#     number=[]
#     max_num=float('-inf')
#     second_max=float('-inf')
#     third_max=float('-inf')
#
#     if arg1.count(arg1[0])==len(arg1):
#         number.append(arg1[0])
#
#     else:
#         for num in arg1:
#             if num==max_num or num==second_max or num==third_max:
#                 continue
#             if num>max_num:
#                 third_max=second_max
#                 second_max=max_num
#                 max_num=num
#
#             elif num>second_max:
#                 third_max=second_max
#                 second_max=num
#
#             elif num>third_max:
#                 third_max=num
#         number.append(max_num)
#         number.append(second_max)
#         number.append(third_max)
#
#     return number
#
#
#
#
#
# arg1=[4,10,10,9]
# print(two_highest(arg1))


# def two_highest(arg1):
#     if not arg1:
#         return []
#
#     number=[]
#     max_num=float('-inf')
#     second_max=float('-inf')
#
#
#     if arg1.count(arg1[0])==len(arg1):
#         number.append(arg1[0])
#
#     else:
#         for num in arg1:
#             if num==max_num or num==second_max:
#                 continue
#             if num>max_num:
#
#                 second_max=max_num
#                 max_num=num
#
#             elif num>second_max:
#                 second_max=num
#
#
#
#
#         number.append(max_num)
#         number.append(second_max)
#
#
#     return number
#
#
#
#
#
# arg1=[4,10,9]
# print(two_highest(arg1))

# def monkey_count(n):
#     return [i for i in range(1,n+1)]
# n=10
# print(monkey_count(n))

def explode(arr):
    number=[]
    sum=0
    for element in arr:
        if isinstance(element,(int,float)):
            sum=sum+element

    if all(isinstance(element,str) and len(element)==1 for element in arr):
        return "Void!"




    for _ in range(1,sum+1):
        number.append(arr)
    return number

arr=['a','b']
print(explode(arr))





