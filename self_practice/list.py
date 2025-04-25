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


def find_difference(a,b):
    mul_a=1
    mul_b=1
    for i in a:
        mul_a=i*mul_a
    for j in b:
        mul_b=j*mul_b
    return abs(mul_a-mul_b)

a=list(map(int, input("Enter the list a: ").split()))
b=list(map(int,input("Enter the list b: ").split()))
print(find_difference(a,b))










