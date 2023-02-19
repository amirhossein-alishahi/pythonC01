#%% list S

myList = [23,"hi",23.233,51,23,12,1,2,3]

lenMyList = len(myList)

print(lenMyList)

#%% type
print(type(myList))
print(myList)
print(myList[2])

#%% Access Items
classList = ["amir","ali","parsa"]
classLen = len(classList)
print(classList[classLen - 1])
print(classList[-1])

print(myList[:3])
print(myList[3:6])
print(myList[2:])
print(myList[-3:])

#%% Change Items
print(myList)
myList[3] = "hello"
print(myList)

print(myList)
myList[3:5] = ["hsd",29]
print(myList)

print(myList)
myList[4] = ["hsd",29]
print(myList)

#%% Add Items

classList = ["amir","ali","parsa"]
classList.append("akbar")

classList.insert(1,"sdfd")


#%% Remove Items

classList = ["amir","ali","parsa","ali"]
print(classList)
classList.remove("ali")
classList.remove("ali")

print(classList)


classList = ["amir","ali","parsa","ali"]
classList.pop()
classList.pop(-1)

classList.clear()
del classList
print(classList)

#%% Join Lists
classList1 = ["amir","ali","parsa","ali"]
classList2 = ["adf","sdf"]

classList1 = classList1 + classList1

list3 = classList * 2

classList1.extend(classList2)

print(classList1)
#%% List End

#%% tuple

tuple1 = (32,43,12)
tuple1.append(231)

tuple1 = list(tuple1)
tuple1.append(231)
tuple1 = tuple(tuple1)
tuple2 = (1,2,3,4,5,6,7)
(ab, bc ,*cd) = tuple2
print(ab)
print(bc)
print(cd)
print(tuple1)

#%% set

set1 = {1,2,3,4,5,6}
set2 = {8,9,10,2,3,4,5,6}
set1.symmetric_difference_update(set2)
print(set1)
list1 = [1,2,3,3,3,2,4,5,6]
list1 = set(list1)
list1 = list(list1)
print(list1)

#%% dictionarie

sla = {"name":"amir", "age": 23}

print(sla["name"])






#%% split
txt1 = "hi how are"
txt2 = "sdkjfhks"
txt3 = "ljk,sfjld,sjldfi,fjsl"

list1 = [*txt3]
list2 = txt3.split("j")

print(list1)
print(list2)


