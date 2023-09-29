import random # used for rendom 
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
# Data Type 
# Number
#Conversion Type
x = 1
y = 1.52
z = 1j

a = float(x)      #  Converting int to float
print(a)
print(type(a))

b = int(y)         # converting float to int
print(b)
print(type(b))

c = complex(x)      # conerting int to complex
print(c)
print(type(c))


print(random. randrange(1,10))  # Random Number

# String(str): eg x="Hello World!"
print("Hello")  #just normal stringb

d= "Hello"       # assign string to Variable
print(a)     


e= """ Hi my name is nirmeet I am polishin my                           
skills and working hard to get jobs  and all that stuff"""              # or you can use for ''' 0fgnjo0njo''' single quote(Multiline Strings)
print(d)

print(e[2])                                                             # String are Arrays


for f in "banana":                                                      #Looping Through String
    print(f)
    
g= """ Hi my name is nirmeet I am polishin my                           
skills and working hard to get jobs  and all that stuff"""              # String Length
print(len(g))


txt = "Hi my name is Nirmeet"
print("Nirmeet" in txt)                                                 #Check String

txt = "Hi my name is Nirmeet"
if "Nirmeet" in txt:
    print("There is nirmeet in txt")                                      # if statemen

txt = "Hi my name is Nirmeet"                                            # Check if Not
print("yash" not in txt)

txt = "Hi my name is Nirmeet"                                            # if statement for checking if Not
if "yash" not in txt:
    print("it is not in text")

#>>>>>>> slicing String
a="Hi my name is Nirmeet"
print(len(a))
print(a[2:])              # 2 will skip first 2 index and print rest of the stuff :: my name is Nirmeet
print(a[2:7])
print(a[-5:-2])          # - will start from back like -5 (rmeet), -2 (rme)


#>>>>>>> Python -modify string
a = "Hello Word!"
print(a.upper())  # upper Case letter

print(a.lower())  # lower Case letter

print(a.strip()) # The strip() method removes any whitespace from the beginning or the end


#>>>>>>> Replace String
a = "Hello World!"
print(a.replace("H","J"))

print(a.split(","))  #returns['hello','World!']

a="Hello"
b="World"  # String Concatenation
c = a+b
print(c)



# >>Integer(int): eg x=22



#  >>Float(float): eg x=1.22



# >> Complex(complex): eg x=4j2j



#  >>List(list): eg  ["orange","banana","apple"]



#  >>Tuple(())



# >>Range(6)


# >>Dictonery(dict{}): eg {"name":"nirmeet","age":36}  



# >>Set({}): eg {"orange","banana","apple"}


# >>Frozenset(frozenset({})): eg x=frozenset({"orange","banana","apple"})


# >>Booleans(bool): eg True,False


# >>Bytes(b): eg b"hello"


# >>Bytearray(bytearray): eg x=bytearray


# >>Memoryview(memoryview): eg x=memoryview(bytes(5))




