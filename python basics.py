# this is the repositary for thr all python basics and code examples where its going to be so easy to learn for others
# python variables
# a=12
# z=19
# print(a+z)
#  this above program is for the summing up of two numbers where you can change operator sing (-,*,%%)
# a=9
# a="hello" #this is a sring where its represnted ny("",'')
# print(a)
# we ar ewritting a program for gretting some one
# a=input("whats your name")
# grettings = " welecome"
# print (a+grettings)
# python data types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# The above are the the data types used in python
# if you want get the data type from the given program
# l= 45
# k="hello world"
# i=4.5
# o=45j
# h=True
# print(type(l))
# print(type(k))
# print(type(i))
# print(type(h))
# print(type(o))
# python strings
# # strings are represented in ("",'',"''")
# a="' lorem ipsum solor sit amet,consectutur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna a liqua'"
# b="45"
# print(a)
# print(type(b))

# string slicing
# string slicing is the a sring method where it it specify the start index value and end index value[:]
# a="pavan arikapudi"
# print(a[0:5])
# sring slicing can be of two types thre are from start to end where it specifiys the only start index value where end index value is not represnt  then it reprentt the whole sting and same linke viceversa from start to end where only end index value is represnted
#
# a= "hello"
# print(a.replace("hello","pavan"))
# print(len(a))
# print(a)
# print(a.split("hello"))
# print(a.split(a))
# #modification of strings  can be done in some a=ways linke upper(),lower(),strip(),split(),replace()
# b ="hello world"
# print(b.strip())
# string format
# string format is used to join the string tha variable
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# -----------------------------------------------------------------list-------------------------------------------------------------------------------------
# lists
# list are representd in the [] and seperated by [ ,]
# exampele
a = ['vamsi', 'list', 75.89, 90]
print(a)
print(type(a))
# the list can be slised based on their  index value
print(a[0:])
# list methods
# Method	Use
# '''len()	returns list length
# sort()	sorts the list
# min()	returns the minimum value from list
# max()	returns the maximum value from list
# list()	converts a sequential data type to list
# append()	adds an element at the end of the list
# clear()	removes all elements from the list
# copy()	returns the copied list
# reverse()	reverses the order of the elements of the list
# sum()	returns the sum of the elements of the list
# range()	returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# pop()	removes the element at the specified position
# remove()	removes the item with the specified value
# index()	returns the index of the first element with the specified value
# insert()	Adds an element at the specified position'''


# changing values in list by asiing new values to the by locationg the indxex number
a[1] = 'abhi'
a[2] = 'vinod'
a[3] = 'pavan'
print(a)
# ---------------------------------------------------------------------------tupel-------------------------------------------------------------
# Tupel
# tupels are represented in the form of ()
# tupels are immutable
# we can acsess tupel by sepcifing their index value
# a=(58,46,79,30,'abhi','vamsi')
# print(a)
#  one element tupel
# a1=(45)
# a2=("23")
# a3=(12,)
# print(type(a1))
# print(type(a2))
# print(type(a3))
#  Joinning tow tupels
# a = (45,67,23,89)
# b=(12,'pavan','vinod','bakoda')
# c=a+b
# print(c)

# tupel methods
# count()
# index()
# a=(1,2,34,1,1,6)
# print(a.count(1))
# print(a.index(2))
# --------------------------------------------------------------------------------------------------boolean-----------------------------------------------------------------------
# boolean is the data type wheraits used for only represnt true or false
# print(2>10)
# print(12==12)
# print(2<12)
# ---------------------------------------------------------------------------------------------------sets--------------------------------------------
#  sets are the data types which are muttable
# sets are most of the used are maths
# sets are the unodered collection where the sets are represent in {}
# set does not contain  duplicate value
# set1 ={12,456,688,3457,6,3,85,5,77}
# set2={'hi','welcome', 'where','are' ,'you'}
# print(set2)
# print(set1)
# set1.update(set2)
# print(set1)
# --------------------------------------------------------------------------------------------------dictoionary----------------------------------------
# a python dictionary is muttable data type
# dictionary is used for mapping data type
# the dictionary is the collection of key and value pairs
# dictionary  are stored in the {}
# dict={
#  "abhi":"bucchi reddy palem",
#  "pavan":"nellore",
#  "vinod":"nasik"
# }

# print(dict["abhi"])
# print(dict)
# print(type(dict))
# dict["pavan"]="guntur"
# dict["varshan"]="nellore"
# print(len(dict))
# del dict["varshan"]
# print(dict)
# adress = dict
# print(adress)
# -----------------------------------------------------python operators-------------
# Arithmetic operators
# Comparison operators
# Assignment Operators
# Logical Operators
# Bitwise Operators
# Membership Operators
# Identity Operators
