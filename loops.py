#FOR LOOP
# students= ['zainab', 'daniel', 'charles']
# for i in students:
#     print(i)
# #OR
# fruits= ['apple', 'orange', 'mango', 'cashew', 'pineapple']
# for fruit in fruits:
#     print(fruit)
    #RANGE
# for i in range(10):
#     print(i)

for i in range(10+1):
    print(i)

# for i in range(1,10+1):
#     print(i)

# for i in range(1,12,2):
#     print(i)

# #range for strings
# # # for i in range(len(fruits)):
# # #     print(i)
# # #     print(fruits[i])
# for i in range(1,len(fruits),2):
#     print(i)
#     print(fruits[i])

#WHILE
# num=0
# while num<10:
#     print(num)
#     num+=1 #this means num= num+1

#break and continue
# fruits= ['apple', 'orange', 'mango', 'cashew', 'pineapple']
# for fruit in fruits:
#     if fruit=='cashew':
#         break
#     print(fruit)

# numbers = [ 1,2,3,4,5,6,7,8]
# for number in numbers:
#     if number== 4:
#         continue
#     print(number)

'''ASSIGNMENT'''
#::: PART ONE
# fruits= ['mango', 'banana', 'melon', 'pineapple', 'strawberry']
# for fruit in fruits:
#     print(fruit)

# #QUESTION 2
# name= 'zainab alugo'
# for i in range(6):
#     print(name)
# #or
# name= 'zainab alugo'
# print(name*6)

#QUESTION3
# number= int(input("enter any number: "))
# factorial=1
# if number < 0:
#     print('sorry, factorial does not exist for negative numbers' )
# elif number == 0:
#     print(' The factorial for 0 is 1')
# else:
#     for i in range(1,number + 1):
#         factorial= factorial*i
#     print('the factorial of ', number, 'is', factorial )

 #::: PART 2
#zee
# def multiply():
#     number= int(input("enter any number: "))
#     for i in range (1, 13):
#        result= number*i
#        print(result)
# multiply()
#or
# def multiply():
#     number= int(input('enter any number: '))
#     for i in range (1, 13):
#        print( number, '*' , i, '=', number*i)
# multiply()
#or
# num= int(input("enter any number: "))
# for i in range (1, 13):
#     print(num, 'x', i, '=', num*i)

#QUESTION 2

# num1= int(input("enter any number: "))
# num2= int(input("enter any number: "))
# total= num1 - num2 
# for i in range (1, 13):
#     print(num, 'x', i, '=', num*i)
# #OR

# number1= [1,2,3,4,5,6,7,8,9]
# number2= [1,2,3,4,5,6,7,8,9,10,11,12]
# for i in number1:
#     print( number2* i)

# def multitable():
#     row= int(input("enter a  number"))
#     while row <=12:
#         column= 1
#         while column<= 12:
#             result = row * column
#             print(f" {row} 'x' {column} = {result} ")
#             column += 1
#             row += 1
# multitable()
# def multitable():
#     row= int(input("enter as many number as uou want"))
#     for i in range(1, 13):
#         column= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
#         for i in range(1, 12):
#             result = row * column
#             print(f" {row} x {column} = {result} ")
# multitable()

#OR

# row = int(input("enter a number"))

# while row <= 12:
#     col = 1
#     while col <= 12:
#         result = row * col
#         print(f"{row} x {col} = {result}", end="\t")
#         col += 1
#     print()  # Move to the next line for the next row
#     row += 1
#

#QUESTION THREE
# stored_password= ('Zainab'.lower())
# maximum_attempt= 2
# password= input(" enter your password")
# if password == stored_password:
#     print('welcome')
#     'break'
# elif password!= stored_password:
#     print('incorrect password, please try again')
#     'break'
#     password= input(" enter your password")
# elif password!= stored_password:
#     print('incorrect password, please try again')
#     'break'
#     password= input(" enter your password")
# else:
#     print('No more attempt try again later')

# #or   (the correct one)
# stored_password= "zainab11"
# maximum_attempt= 2
# for attempt in range(maximum_attempt+1):
#     password= input('enter your password:')
#     if password== stored_password:
#         print('welcome')
#         break
#     elif password!= stored_password:
#         print('incorrect password try again')
#     elif attempt < maximum_attempt: 
#         print(' incorrect password try again')
#     else:
#         print(' no more attempt, Goodbye!')

