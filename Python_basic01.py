#Author:Nirmeet_Pansuriya
#Date:27 September 2023
#########################################################################################################################################################################
# Day:1

# Python is a object orianted, high level orianted language. 
# Use to create web application, handle big data and can performance high complex math problems 

# Starting from "Varabials" it can be: letter or the under_score.
#                                      cannot start with a number.
#                                      They are case-Sensitive
#                                      They Cannot be python keyword
#                                      Eg.(A-a;_;0-9) 

# Camel Case:- myNameVariable:(First letter small and rest all are Capital)
# Pascal Case:-MyNameVariable:(All First letter are Capital)
# Snake Case:- my_name_variable:(All letter are small and are seprated by under_score)

# Assign Multipal Value:  X=Y=Z="orange"(many variables one value)
#                             or
#                         X=Y=Z="orange","banana","apple"(many valur to many variables)
#                             or 
#                         fruit=["apple","banana","orange"](Unpacking a collection)
#                         x,y,z=fruit
#########################################################################################################################################################################
# Day:2

x=[3.4,5,7,8,'Paper']

y=[3.4,'Paper',5,7,8]

print(x==y)

students=['Rina',112,'Russia']

course1 = ['Data Analysis',109]

course2 = ['Machine Learning',111]

faculty=[18,'Mr.Shane']



print('Printing the data of students..')

print('Name is: %s, Id is: %d, Country is: %s' %(students[0],students[1],students[2]))

lst=[4,5,6,7,9,90,45,78,56]

print(lst[1:8:3])

list=[1,2,3,4,5,6]

print(list[-1])

print(list[-4:])

print(list[:-2])

print(list[-3:-1])

list1=[4,5,6,3,2,2]

list1[-2]=10

print(list1)

list1[1:3]=[44,55]

print(list1)
