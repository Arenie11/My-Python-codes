'''variables
x=1
print(x)
print(type(x))
y=2.5
print(y)
print(type (y))
is_best= True
print (is_best)
print(type(is_best))'''
'''name='zainab'
print(name)
print(type(name))'''
#first_name= input("Enter your first name:")
#last_name= input("Enter your last name:")
#age= int(input("enter your age:"))
'''first_name= "zainab"
last_name= "alugo"
age= 23
print(first_name.upper())
print(last_name.upper())
print(age)'''
#strings&formatting
#concatenate  
'''name= ('zainab world')
print('Hello,welcome to' + name)
#concatenation with number
name= "zainab world"
number= str(3)
print('Hello, welcome to ' + name + ' Location ' + number)'''
'''#concatenation with number
name= 'zainab'
number= 2
print('Hello, welcome to ' + name + ' location ' + str(number)) 
#string formatting
#argument by position
print ('{1}, {0}, {2}' . format ( 'zainab', 'saidat', 'faruq'))'''
#argument by name 
#print('My name is {name} and i am number {num}' . format(name= 'zainab', num='3'))
#f-string
'''name= 'zainab'
number= 3
print(f'my name is {name} and i am number {number}')'''
#string methods
#capitalize firls letter
'''name= 'zainab'
print (name.capitalize())'''
#uppercase
#name= 'zainabalugo'
#print(name.upper())
#name= 'ZAINAB'
#print(name.lower())
#swap case
#name= 'ZAInab'
#print(name.swapcase())
#variable length
#name='zainabalugo'
#print(len(name))
#replace
#name='zainab'
#print(name.replace('zainab', 'saidat'))
#count
#name= "zainab"
#print(name.count('a'))
#list
'''numbers= [1,2,3,4,5]
fruits= ['Apples', 'oranges', 'guava','mango', 'paw paw']
print(numbers)
print(fruits)'''
#get value
'''numbers= [1,2,3,4,5]
fruits= ['Apples', 'oranges', 'guava', 'mango','paw paw']
print(fruits[3])
#get length
numbers= [1,2,3,4,5]
fruits= ['Apples', 'oranges', 'guava', 'mango','paw paw']
print(len(fruits))
#append to list
numbers= [1,2,3,4,5]
fruits= ['Apples', 'oranges', 'guava', 'mango','paw paw']
fruits.append('pears')
print(fruits)
print(len(fruits))
#remove from list
fruits.remove('pears')
print(fruits)
#inserting into position
fruits.insert(2,'guava')
print(fruits)
#remove from position
fruits.pop(3)
print(fruits)'''
#reverse list
#numbers= [1,2,3,4,5]
#fruits= ['Apples', 'oranges', 'guava', 'mango','paw paw']
#fruits.reverse()
#print(fruits)
#sort list
numbers= [1,2,3,4,5]
fruits= ['Apples', 'oranges', 'guava', 'mango','paw paw']
fruits.sort()
print(fruits)