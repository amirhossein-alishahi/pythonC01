# def myFunction(num, num1):
#     num2 = num * num1
#     return num2,num,num1


#%% Lambda

# p10 = lambda num : num + 10 
# print(p10(12))

# def p10 (num):
#     return num + 10


# def myFunction(num):
#     return lambda num1 : num1 * num

# m2 = myFunction(2)
# m3 = myFunction(3)

# print(m2(8))

# def myFunction(num, num1):
#     return num*num1

# myFunction(2,8)

#%% String

# age = 24 
# name = "amir"
# fname = "ali"
# txt = "my name is {0} {0} and I am {1}!!"
# # print(txt)
# print(txt.format(name,age))

# age = 24 
# name = "amir"
# fname = "ali"
# txt = "my name is {name1} {name1} and I am {age1}!!"
# # print(txt)
# print(txt.format(name1 = name,age1 = age))

#%% RegEx

import re

txt = "I'm amir"
x = re.search("^i",txt)

print("Hello")