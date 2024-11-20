# ''''
# Dictionary in python is just like an object in javascript & php
# An object consists of key and value, between the keY and valUE we use the column":" and end 
# with a comma to give room for the next key and value.
# to write an object we use the curly bracket'{}'

# '''
person= {
'f_name': 'John',
'l_name': 'Doe',
'age': 23,
'm_status': 'married',
'disability': False
}

#access value
#print(person['f_name'])

#add key/ value
#person['phone']= +2347081243152

# #get key
# print(person.keys())

# #get items
# print(person.items())

# # make copy
# person1=person.copy()

# #get length
# print(len(person))

# #List of Dictionary
# people= [

# { 
#     'id':1,
#  'f_name':"Alugo",
#  'l_name':'Zainab',
#  'm_status': "married",
#  'age' : 23

# },
# { 
#     'id':2,
#     'f_name':'Akata',
#     'l_name': 'Daniel',
#     'm_status': 'complicated',
#     'age':27
# },
# {
#     'id':3,
#     'f_name': 'Charles',
#     'l_name':'Eromoser',
#     'm_status': 'single',
#     'age': 26
#  }
# ]
# #print(people)
# #print(people[1])
# #print(people[2]['m_status'])

#Assignment
# ''' QUESTION 1'''
# person= {
#     'name': 'Zainab Alugo',
#     'age': 23,
#     'm_status': 'single',
#     'disability': False 
#}
'''QUESTION 2'''
# print(person['age'])
# person['hobbies']= 'reading'
# print(person)

# '''QUESTION 3'''?
# person2= person.copy()
# person2['height']= 45.2
# print('person2')
#or copy and paste
# person1= {
#     'name': 'Zainab Alugo',
#     'age': 23,
#     'm_status': 'single',
#     'disability': False 
# }
# person1['height']= 45.2
# print('person')


'''QUESTION 4'''

people= [
{    
    'name': 'Zainab Alugo',
    'age': 23,
    'm_status': 'single',
    'disability': False
},
{

    'name': 'Saidat Alugo',
    'age': 26,
    'm_status': 'married',
    'disability': False, 
},
{
    'name': 'Hassan Alugo',
    'age': 30,
    'm_status': 'single',
    'disability': False, 
},
{
    'name': 'Faruq Alugo',
    'age': 20,
    'm_status': 'complicated',
    'disability': False, 
},
{
    'name': 'Faruq Alugo',
    'age': 20,
    'm_status': 'complicated',
    'disability': False, 
}
]
# print(people[3])

