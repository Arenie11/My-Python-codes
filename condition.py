#CONDITION

#IF & ELSE STATEMENT
# x= 5
# y= 5
# if x==y:
#     print(f'{x} is equal to {y}')
    
# x= 10
# y= 5
# if x==y:
#     print(f'{x} is equal to {y}')
#note that this didn't print a response because x is not equal to y, because the condition given to it is that, it should print 'if' x is equal to y, which is not.


#else
# x= 10
# y= 5
# if x==y:
#     print(f'{x} is equal to {y}')
# else: 
#     print(f'{x} is not equal to {y}')

# name = input ('enter your name: ').lower()
# if name == 'zainab':    
#     print(f'allow her to take exam')
# else:
#     print(f'you are not registered for the exam')

#create a form for weather
# #rainy, sunny, harmattan 
# weather= input( 'enter weather').lower()
# if weather=='rainy':
#     print(f'hold your umbrella')
# elif weather== 'sunny':
#     print(f'hold your sunshade')
# elif weather== 'harmattan':
#     print(f'wear your sweater')
# else: 
#     print(f' weather is good')

# from age 5-30 can take immunization, run the code
# age= int(input('enter your age'))
# if age >= 5 and age <= 30:
#     print(f" yes, you are eligible for immunization ")
# elif age > 30:
#     print (f'you are too old for this immunization')
# else:
#     print (f'you should eat well ')

#nested if
# x=6
# if x > 2:
#     if x < 10: 
#         print(f'x is greater than and x is less than 10')

#logical operators
#And
# x=6
# if x > 2 and x > 10:
#     print(f'{x} is greater than 2 and less than 10')

# #or
# if x > 2 or x < 10:
#     print (f'{x} is greater than 2 and less than 10')
# else:
#     print (f'{x} is greater than 2 and less than 10')

#not
# if not( x > 2 and x < 10):
#     print(f'{x} is greater than 2 and less than 10 ')
# else:
#     print('false')

# number = [1,2,3,4,5,6]
# x=6
# if x in number: 
#     print( x in number )

## not in 
# number = [1,2,3,4,5,6]
# x=7
# if x not in number:
#     print (x in number)

#identity Operators
#is
# x=10
# y=10
# if x is y:
#     print (x is y)

# #is not
# x= 10
# y = 5
# if x is not y:
#     print(x is not y)

#Assignment
'''PART 0NE'''

# def even_odd():
#     number= int(input('enter any number'))
#     if number % 2==0:
#         print(f'({number} is an even number)')
#     else:
#         print(f'{number} is an odd number')
# even_odd()
'''QUESTION 2'''
# def vow_con():
#     Alphabet= input('enter any alphabet').lower()
#     if Alphabet is {'a,e,i,o,u'}:
#         print(f'it is a vowel letter')
#     else: 
#         print(f'it is a consonant letter')
# vow_con()

'''PART TWO'''
# def compare(num1,num2, num3):
#     num1= input('enter any number')
#     num2= input('enter any number')
#     num3= input('enter any number')
#     if num1>=num2 and num1>=num3 :
#         print(f'{num1} is greater')
#     elif num2>=num3 and num2>=num1:
#         print(f'{num2} is greater ')
#     else:
#         print(f'{num3} is greater ')
# compare('', '', '')
'''QUESTION 2'''
# def addition():
#     x+y

# print( '''Welcome to, Alugo calculator
#            please select a number to proceed:
#       1. Addition                           2. Subtraction
#       3. division                           4. Multiplication
# ''')
# number= input('select any number')
# print(number)
# def addnum(num1, num2):
#     num1= int(input('enter any number'))
#     num2= int(input('enter any number'))
#     total= num1+num2
#     return f'{total}'
# def subnum(num1, num2):
#     num1= int(input('enter any number'))
#     num2= int(input('enter any number'))
#     sub= num1-num2
#     return f'{sub}'
# print(addnum('',''))

'''QUESTION 3'''
#grading system
# number= input('enter any number')
# if {number} is 80 >= 100:
#     print('excellent')
# else:
#     print('bad')
# score= float(input('enter any number'))
# def grading_system():
#     if  (score >= 80) and (score <= 100):
#         print('excellent')
#     elif (score>= 60) and (score<= 79):
#         print('very good')
#     elif (score>= 40) and (score<=59):
#         print('good')
#     elif (score>= 20) and (score<= 39):
#         print('fair')
#     elif (score>= 0) and (score <= 19):
#         print('fail')
#     else:
#         print('invalid score')
# grading_system()
