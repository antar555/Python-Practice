# my_list=[5,10,15,20]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# print(my_list[-4])

# chat_history=[
#     "Antar: Hi, how is it going",
#     "Mahady: Hey, whats up!"
# ]
# print(f"The last message is: {chat_history[-1]}")

# my_list=[[1,2,3],"Antar",[4,5,6]]
# print(my_list[0])
# print(my_list[0][0])
# print(my_list[0][1])
# print(my_list[0][2])
# print(my_list[1])
# print(my_list[2])
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])

# my_list=[
#     [1,2,3],
#     [["a","b","c"],5,6]
# ]
# print(my_list[1][0][1])

# colors=["red", "green", "blue", "yellow", "purple"]
# print(colors[0])
# print(colors[-1])

# def colors_name(colors):
#     print(colors[0])
#     print(colors[-1])
#
# colors=["red","blue","yellow","orange","green"]
# colors_name(colors)

# def matrix_number(matrix):
#     print(matrix[1][1])
#     print(matrix[2][-1])
#
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# matrix_number(matrix)

# def students_name_score(students):
#     students[2][1]=88
#     print(students[2][1])
#     print(students[1][0],students[1][1])
#
# students=[
#     ["Alice", 85],
#     ["Bob", 90],
#     ["Charlie", 78]
# ]
# students_name_score(students)

# def menu_items(menu):
#     print(menu[1])
#     print(menu[1][1])
# menu=[
#     ["Burger","Fries","Soda"],
#     ["Pizza","Wings","Juice"]
# ]
# menu_items(menu)

#Adding elements to a list
#Append Method

#Add items to end of the list using append method
# lang=["C","Cpp","Java"]
# lang.append("python")
# lang.append("php")
# print(lang)

#A list can be also added using append

# device=["Apple"]
# device.append(["Google","Sony"])
# print(device)

#insert() method
#This method allows to add items to the list at a specific position

# lang=["C","Cpp","Java"]
# lang.insert(0,"python")
# print(lang)

#extend() Method
#add all items of one list in another list

# web_dev=["Django","Next JS","React JS"]
# lang=["Python","JS"]
# web_dev.extend(lang)
# print(web_dev)

# numbers=[]
# for i in range(5):
#     x=int(input("Enter the number: "))
#     numbers.append(x)
# print(numbers)

#split Method to input a list

#input a list using split() method
# n=int(input("Enter the number of elements: "))
# numbers=input("Enter the numbers: ").split()
#
# for i in range(0,n):
#     numbers[i]=int(numbers[i])
# print(numbers)
# print(type(numbers))

# numbers=list(map(int, input("Enter the numbers: ").split()))
# numbers=list(map(int, input("Enter the number: ").split()))
# print(numbers)

#Changing item of list

# list=["Rob","Jeniffer","Bob",1,2]
# list[2]="Michael"
# print(list)

#Changing Multiple items using slicing operator
# list=["Rob","Jeniffer","Bob",1,2]
# list[2:4]=["Michael","Anderson","Emma"]
# print(list)
# list[2:4]=["Antar"]
# print(list)

#inserting a new item by insert method

# list=["Rob","Jeniffer","Bob",1,2]
# list.insert(2,"Mike")
# print(list)




