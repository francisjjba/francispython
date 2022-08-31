
# _________________________________variables and numbers______________________________________________________________________
# char_age = 35.5
# char_name = "john"
# print("there is person name "+char_name)
# print("there is person age ", char_age)

# char_name = "mike"
# print("there is person name "+char_name)
# print("there is person age "+char_age)

# __________________________________working with strings____________________________________________________________________________

# print("there is ohgube\n name ") # use to end line

# print("there is ohgube\" name\" ") # use to add quatoation

# from calendar import month
# from math import *
# from unittest import result
# phrase = "Hello"

# print(phrase+" is cool")


# functions //////////////////////////////////////////////////////////////////////////
# print(phrase.lower())  #converts to lowercase
# print(phrase.upper())   #converts to uppercase
# print(phrase.islower())   #gives true or false is is uppercase or lowercase
# print(phrase.isupper())  #gives true or false is uppercase or lowercase
# print(phrase.lower().islower())  #multi fuction usage
# print(len(phrase)) /#length of the string
# print(phrase[0]) #index of the string values
# print(phrase.index("Hel")) #gives the index values
# print(phrase.replace("Hello","konichiwa")) #replace the value


# ____________________________________WORKING WITH NUMBERS_______________________________________________________________


# num = 5
# print(num) #used to print a numbers

# print(str(num)+ " fucker") #convert it numberss to string


# function in number///////////////////////////////

# numb = -5

# print(abs(numb)) # gives absolute value
# print(pow(3,2))  # power that is N^p
# print(max(3,6))  # gives the maximum value
# print(min(3,6))  # gives the minimum value
# print(round(3.2)) # gives the rounded value


# print(floor(3.6))   # choops the decimal value
# print(ceil(3.6))  # round the value
# print(sqrt(36))  # gives the square root of the value

# ________________________getting input from user_________________________

# name=input("enter your name:") # enter value
# print("hello "+ name)

# ------------------------------building a basic calculator --------------------------------

# num1=input("enter the number 1 ")
# num2=input("enter the number 2 ")
# result=int(num1)+float(num2) #convert to integer and  float
# print(result)

# -------------------mad libs game----------------------------------------

# color=input("enter the color")
# pluralnoun=input("enter the pluralnoun")
# celebrity=input("enter the celebrity")

# print("roses are "+color)
# print(pluralnoun+" are blue")
# print("i love "+ celebrity)


# --------------------working with lists --------------------------------

# friends = ["kevin", "john", "fred"]  # supports boolean,numbers,strings
# print(friends)
# print(friends[0]) #indexing using index values
# print(friends[1])
# print(friends[2])

# print(friends[-2])#used to select backward

# print(friends[1:3]) #selects range except for last

# friends[1]="mike" #useful for editing and changing values in lists

# lists functions////////////////////////
# frnum = [1, 2, 3, ]


# friends.extend(frnum) #add two lists together
# friends.append("toby") #add a value a the end of the list
# friends.insert(2, "toby") #add a value a the any where the number is position of the list
# friends.remove("john") #remove a value from the list
# friends.clear() #removes all a elements from the list
# friends.pop(2) #pop a value from the list
# friends.index("john") # tells the index value
# friends.count("john")  # counts a value from the list
# friends.sort() #sorts  the values in alphabetical order
# friends.reverse() #reverse the value from the list
# friends2=friends.copy() #copy values to other list


# print(friends)

# ------------------------------TUPLES---------------------------------------------------------------------


# tuples-data structureto store values and similiar to list
# tuples cannot be changed ------------>unmutable
# coordinates=(4,5)
# print(coordinates)

# --------------------------------FUNCTIONS---------------------------------------------------------------------

# def sayhi():  # defining a function
#     print("Hi"+name)


# sayhi() # calling a function


# def sayhello(name,age):  # passing a parameter
#     print("Hi"+name+" and u are "+age)

# sayhello("john","30")

# -----------------------------------------returns statement----------------------------------------------------------------

# returns function values


# def cube(num):
#     return num*num*num  # using return

# print(cube(3))

# result=cube(4)
# print(result)

# -----------------------------------------if statements----------------------------------------------------------------

# ismale=True
# istall=False

# ///////////////////////USING THE IF ELSE///////////////////////////

# /////////////////////////USING OR////////////////////////////////
# if ismale or istall:
#     print("you are a male  or tall or both")

# else:
#     print("you are a female ")


# ///////////////////USING AND /////////////////

# if ismale and istall:
#     print("you are a male  or tall or both")

# else:
#     print("you are a female ")

# /////////////////////using not/////////////
# if ismale and  not(istall):
#     print("you are a male  or tall or both")

# else:
#     print("you are a female ")

# //////////////////////---ELIF---//////////////////

# if ismale and istall:
#     print("you are a male  or tall or both")

# elif ismale and not(istall):
#     print("you are a short ")

# else:
#     print("you are a female ")


# ////////////////--if statements using comaparasions---////////////////

# def maxnum(n1,n2,n3):
#     if n1>=n2 and n1>=n3 :
#         return n1
#     elif n2>=n1 and n2>=n3 :
#         return n2
#     else:
#         return n3

# print(maxnum(300,50,200))


# == --->equal too
# != ---->not equal to
# >= ---->greater than equal to
# <= ---->less than equal to
# < ----->less than
# > -----> greater than

# --------------------building a calculator -----------------------------

# n1=float(input("enter the first number:"))
# op=input("enter the operator:")
# n2=float(input("enter the second number:"))


# if op=="+":
#     print(n1+n2)
# elif op=="-":
#     print(n1-n2)
# elif op=="*":
#     print(n1*n2)
# elif op=="/":
#     print(n1/n2)
# elif op=="%":
#     print(n1%n2)
# else:
#     print("error motherfucker")


# -------------------------------DICTIONARY ----------------------------------------------

# SIMILIAR TO LIST BUT HAS A KEY VALUE PAIR

# monthc={
#     "jan":"januaray",
#     "feb":"february",
#     "mar":"march",
#     "apr":"april",
#     "may":"may",
# }

# print(monthc["jan"]) #accessing a dictionary
# print(monthc.get("jan")) # getting a value from a dictionary
# print(monthc.get("bsdk","not a valid key")) # getting a value from a dictionary and adding a default value "not a valid key"

# ------------------------------WHILE LOOP --------------------------------

# i=1
# while i<=10: #defining the while loop
#     print(i)
#     i+=1

# print("done with loop")

# --------------------------------------GUESSING GAME --------------------------------

# secret = "fuck"
# guess = ""
# count = 0
# limit = 3
# outofguess = False

# while guess != secret and not(outofguess):
#     if count < limit:
#         guess = input("enter guess: ")
#         count += 1
#     else:
#         outofguess = True

# if outofguess:
#     print("you lose")
# else:
#     print("you win")

# ------------------------------------FOR LOOP---------------------------------


# for letter in "francis dsouza": #for loop initialization
#     print(letter)


# friends=["jim","vim","karen"]
# for friend in friends: #isung for loop to print array
#     print(friend)

# for index in range(10): #using rannge for loop initialization
#     print(index)


# for index in range(3,10): #using rannge for loop initialization
#     print(index)

# for index in range(len(friends)): #using rannge for loop initialization
#     print(friends[index])

# for num in range(5):
#     if num==0:
#         print("first iteration")
#     else:
#         print("other iteration")


# -----------------------exponent functions-------------------------

# def raiseToPower(base,pow):
#     result=1
#     for index in range(pow):
#         result=result*base
#     return result

# print(raiseToPower(3,4))

# ----------------------------2D lists and Nested loops--------------------------------

# 2D lists

# numberGrid=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
#     ]

# print(numberGrid[0][2])

# NESTED FOR LOOP

# for row in numberGrid:
#     for col in row:
#         print(col)

# -------------------------building a translator-------------------------

# vowels are convertes to g   i.e. dog->dgg

# def translate(phrase):
#     translation=""
#     for letter in phrase:
#         if letter in "aeiou":
#             translation=translation+"g"
#         elif letter in "AEIOU":
#             translation=translation+"G"
#         else:
#             translation=translation+letter
#     return translation

# print(translate(input("enter the phrase: ")))

# ------------------------------try / except---------------------------------------------------
# try:
#     number=int(input("number:"))
#     print(number)
# except:
#     print("Invalid number")

# ___________________________________________________________________
# value=10/0

# try:
#     value=10/0
#     number=int(input("number:"))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("Invalid number")

# --------------------------------------reading from files --------------------------------

# open("emp.txt", "r") #read the file
# open("emp.txt", "w") #write the file
# open("emp.txt", "a") #append the file add info at the end of the file
# open("emp.txt", "r+") #reading and writing the file

# empfile=open("emp.txt","r",encoding='utf-8') # used to open file
# the encoding part is added to tell python the encoding format


# print(empfile.readable()) # check if the file is readable

# print(empfile.read())# to read the whole file
# print(empfile.readline()) # to read the a single first line and then repeat line for second line
# print(empfile.readlines()) #to read in array format

# for employee in empfile.readlines():
#     print(employee)

# empfile.close() #  closing file


# -------------------------------------write to file ------------------------------------------------


# empfile=open("emp.txt","w",encoding='utf-8') #write a file
# empfile.write("hello motherfucker") #adding value to the file
# empfile.write(" \nhello fuckermother") #adding value in the next line
# empfile.close()

# empfile=open("hello.txt","w",encoding='utf-8') #creates a new file

# uses of write
# --append to the file
# --write to the file
# --create new file

# -------------------------------MODULES AND PIP-----------------------------------------------------


# import useful       #using module to get data from the other file

# print(useful.beatles) #accessing files from other file

# python modules index ---- https://docs.python.org/3/py-modindex.html

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# pip ---> used to install pyhton modules (package manaager)

# pip install --module name--
# import --module name--
# nd fuckin use it


# ------------------------------------------CLASSES AND OBJECTS----------------------------------------------

# classes--->defined that cannot be represented in datatypes

# from operator import truediv
# from student import student

# person1=student("ramesh","cs","7.0",False) #giving information to student.py
# person2=student("subhas","ca","8.0",True)

# print(person1.name) #printing info from student.py
# print(person2.gpa)


# -------------------------------------------building a multiple quiz--------------------------------------------------
# from question import question

# questionsPrompts=[
#     "what color are apples?\n(a)red/green\n   (b)purples\n  (c)orange\n\n",
#     "what color are banana?\n(a)red/teal\n   (b)magneta\n  (c)yellow\n\n",
#     "what color are strawberries?\n(a)yellow\n   (b)red\n  (c)blue\n\n"
# ]

# questions=[
#     question(questionsPrompts[0],"a"),
#     question(questionsPrompts[1],"c"),
#     question(questionsPrompts[2],"b")
# ]


# def runtest(Questions):
#     score=0
#     for questions in Questions:
#         answer=input(question.prompt)
#         if answer == question.answer:
#             score+=1

#     print("you got"+str(score)+"/"+str(len(questions))+"correct")

# runtest(questions)

# -----------------------------------object functions------------------------------

# adding functions to object or adding conditions and loops

# from student import student

# person1=student("ramesh","cs","7.0")
# person2=student("subhas","ca","8.0")

# print(person2.honor())

# -----------------------------------Inheritance-------------------------------------

# from chef import Chef
# from chinesechef import chinesechef

# mychef= Chef()
# mychinesechef= chinesechef()
# mychef.chicken()
# mychef.salad()


# mychinesechef.chicken()
# mychinesechef.special()
# mychinesechef.friedrice()

# -----------------------------------python interpreter-------------------------------------
