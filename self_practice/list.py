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

def try_or_stay(hand, next_card):
    sum=0
    if next_card in ['K','Q','T','J']:
        next_card=10
    elif next_card=='A':
        next_card=11
    else:
        next_card=int(next_card)
    for val in hand:
        if val in ['K','Q','T','J']:
            sum=sum+10
        elif val=='A':
            sum=sum+11
        else:
            sum=sum+int(val)
    if sum<17:
        sum=sum+next_card
        return ['hit',sum]
    elif sum>17:
        return ['stay',sum]
    elif sum==17:
        sum=sum+next_card
        if 'A' in hand:
            sum=sum-10
            return['hit',sum]



hand=['A',6]
next_card='A'
print(try_or_stay(hand,next_card))












