#%% for

myList = ["a","b","c"]

v = myList[0]
print(v)


v = myList[1]
print(v)

v = myList[2]

for v in myList:
    print(v)

for char in "hi my name is amir":
    if char == 's':
        break
    print(char)

myList = ["a","b","c"]

for char in myList:
    print(char)
    continue
    print(char)

print(range(6))

myList = [0,1,2,3,4,5,6,7,8,9]

for x in range(0,10,3):
    print(x)
    # print(myList[x])

for char in "abcxslkj":
    if char == 'z':
        break
    print(char)

print("hi")
print("hello")


counter = 0
while counter < 10:
    counter+=1
    if counter == 11:
        break
    print(counter)
else:
    print("hi")

#%% Q1
# https://quera.org/problemset/3537/

n = 5

# m1
text = "W"
for i in range(n):
    text += "o"
text+= "w!"
print(text)

# m2
print("W"+("o"*n)+"w!")

print("W"+"".join(["o" for i in range(n)])+"w!")


num = int(input("number of O's: "))
pre_text = "W*w!"
final_text = pre_text.replace("*","o"*num)
print(final_text)

#%% Q2

n = 5

num = 1
for i in range(1,n):
    num *= (i+1)
print(num)

num1 = int(input())
counter = 1
for i in range(1,num1+1):
    counter = counter*i
print(counter)

import math
print(math.factorial(n))


#%% Q3
# https://quera.org/problemset/2659/

n = 3
text1 = "abC"
text2 = "aabC"

counter = 0

for i in range(n):
    if text1[i] != text2[i]:
        counter+=1

print(counter)

#%% Q4


playGround = []
n = 5
row = [1]
playGround.append(row.copy())
row =[1,1]
for i in range(n-1):
    playGround.append(row.copy())
# print(playGround)
for i in range(n):
    for j in range(i-1):
        playGround[i].insert(-1,playGround[i-1][j]+playGround[i-1][j+1])
print(playGround)

import math
n = 5
for i in range(n):
    for j in range(n-i):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)), end=" ")
 
    # for new line
    print()