# #CLASS
# class BlueprintDogs:
#     #instance of a class
#     #property
#     def __init__(self, name, height, color, leg):
#         self.name= name
#         self.height= height
#         self.color= color
#         self.leg= leg
# #method
#     def bark(self):
#         return f'my name is {self.name} and i can bark'
#     def run(self):
#         return f' i saw {self.name} run with it {self.leg} legs' 

# #create objects
# # d1= BlueprintDogs('bingo', 2.5, 'brown', 4)
# # print(d1)
# # print(d1.bark())
# d2= BlueprintDogs('speedy', 3.2, 'cream', 3)
# print(d2.name)
# print(d2)
# print(d2.run())

#  # inheritance
# class Person:
#     def __init__(self, name, email, age):
#         self.name= name
#         self.email= email
#         self.age= age
#     def greeting(self):
#         return f' my name is {self.name} and i am {self.age}, you can mail me {self.email}'
# class user(Person):
#     def __init__(self, name, email, age):
#         self.name= name
#         self.email= email
#         self.age= age
#         self.sex= 'male'
#     def gender(self,sex):
#         self.sex = sex
# john= user('zainab', 'zainab@gmail.com', 23)
# john.gender('male')
# print(john.sex)

#class of class
# class Circle:
#     pi= 3.142
#     def __init__(self,radius):
#         self.radius = radius
#     @classmethod
#     def value(cls):
#         return f' a circle has a default pie value = {cls.pi}'
# #initialize a circle object
# c1= Circle(5)

# print (c1.pi)
# print (c1.value())

#class of class and instance of class
# class Planet:
#     shape= 'round'
#     def __init__(self, name, radius):
#         self.name= name
#         self.radius= radius
#     def orbit(self):
#         return f' {self.name} is a good planet'
#     @classmethod
#     def common(cls):
#         return f' all the planet are {cls.shape} due to gravity'
    
#     #initializing the object
# venus= Planet( 'venus', 3)
# print(venus.name)
# print(venus.radius)
# print(venus. shape)
# print(venus.orbit())
# print(venus.common())
# print(Planet.shape)
# print(Planet.common)

