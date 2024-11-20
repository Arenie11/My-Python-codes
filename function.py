#function is a block of code that only run when it's being called upon
#basic 
# def sayHello():
#     print(f'hello how are you')
# sayHello()
# def listofpeople():
#     people= ['zainab', 'charles', 'daniel']
#     print(people)
# listofpeople()

## functions with argument
# def saymyname(name,age):
#     print(f'hello my name is {name}, and i am {age} years old')
# saymyname('zainab', '23')

# def sayhello(name='nathaniel'):
#     print(f'hello my name is {name}')
# sayhello()
#return value 
# def sayhello():
#     return(f'hello how are you ')
# print(sayhello())
# 
# def getsum(num1, num2):
#     num1= float(input('enter num one: '))
#     num2= float(input('enter num two:'))
#     total= num1 + num2
#     return f'{total}'
# print(getsum('2', '4'))

#lambda
# getsum= lambda num1, num2 : num1+num2
# print(getsum(2,3))
#Assignment
#''''''part ONE''''

# def getsum(num1, num2):
#     num1= float(input('enter mum one'))
#     num2= float(input('enter num two'))
#     total= num1+ num2
#     return(f"{total}")
# print(getsum('',''))
#''''''PART 2''''

# def getsum(num1, num2= 7):
#     num1= float(input('enter number one'))
#     # num2= 7
#     total= num1+num2
#     return f'{total}'
# print(getsum(2))

# def getsum(num1, num2, num3):
#     num1= float(5.6)
#     num2= float(10.6)
#     num3= float(input('enter num three'))
#     total= num1+num2+num3
#     return f"{total}"
# print(getsum('','',''))

# def getsumsub(num1, num2, num3):
#     num1= float(5.6)
#     num2= float(10.6)
#     num3= float(5)
#     total= num1+num2-num3
#     return f"{total}"
# print(getsumsub('','',''))
