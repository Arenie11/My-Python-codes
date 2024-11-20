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

# for i in range(10+1):
#     print(i)

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

numbers = [ 1,2,3,4,5,6,7,8]
for number in numbers:
    if number== 4:
        continue
    print(number)