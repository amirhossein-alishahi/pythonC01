myDictionary = {}  

num = int(input("How many do you want to add : "))

i = 0
while i < num:
    name = input("name :(Enter E01 to exit) ")
    if name == "E01":
        break
    age = int(input("age : "))
    confirmation = input(f"name : {name} age : {age} is it correct?(y/n) ")
    if confirmation == "n":
        continue
    else:
        myDictionary[name] = age
        i+=1
else: 
    print("All names have been added")


dictItem = list(myDictionary.items())

age = 0
name = ""
for item in dictItem:
    if item[1] > age:
        age = item[1]
        name = item[0]

print(f"name : {name} - age : {age}")