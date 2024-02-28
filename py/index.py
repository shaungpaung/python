# print ("Hello", end=" ")
# print ("Hello!")
# print ("123")  
# a = 10
# print (type(a))
# print ('i need %a' %1)
# print ('i need {1}'.format('water', 'cola'))

# name = 'shaung'
# age = 22
# print (f"i am {name} and i am {age} years old")

# name = 'unknown'
# first_letter = name[0:6:1]
# print (first_letter)

# i = 9
# if i < 10:
#     print ("i is less than 10")
# else:
#     print ("i is greater than 10")

# i = 11
# if i < 10:
#     print ("i is less than 10")
# elif i == 10:
#     print ("i is equal to 10")
# else:
#     print ("i is greater than 10")

# for i in range(10-5, 10+5):
#     print (i)

# x = 5
# while x < 10:
#     print ("i is less than 10")
#     x -= 10

# def name(customer):
#     print ("Hello, " + customer)  

# name("shaung")

# my_list = [1, 2, 3, 78, 1527]
# print (my_list[2])
# print (my_list[4])
# my_list.append("shaung")
# my_list.remove(78)
# print (my_list)

# User = {"name": "shaung", "age": 22, "address": "Yangon"}
# print (User["name"])
# User["age"] = 33
# print (User["age"])
# User["phone"] = "09251618319"
# print (User["phone"])
# del User["name"]
# print (User)


''' Class and Object, Functions and methods'''

# class Dog: // this is the class
#     def __init__(self, name ,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print (f"{self.name} is barking!")
# dog = Dog("alice", "5") // this is the object
# dog.bark()

""" This is Method"""
# class Dog:
#     def __init__(self, name ,age): // This is the function
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}, {self.age} years old"
# mydog = Dog("Aung", 24)
# print(mydog)