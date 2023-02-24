#%% Dictionaries

myDictionary = { 
 "name": "madjid",
 "surname": "ghasemi",
 "age": 34,
  53: 35,
  23.5: "hi"
  }

print(myDictionary)

print(myDictionary["name"])
print(myDictionary[53])
print(myDictionary[23.5])
#error
# print(myDictionary[2])


# cannot have two items with the same key
myDictionary = { 
 "name": "madjid",
 "surname": "ghasemi",
 "age": 34,
 "age": 41,
  53: 35,
  23.5: "hi"
  }

print(myDictionary)
print(myDictionary["age"])

#adding an item to the dictionary
myDictionary["grade"] = 19.5
myDictionary.update({"grade":19.5})
myDictionary.update({"grade":19.5, "anotherItem": "hello"})

#changing an item in the dictionary 
myDictionary["grade"] = 20
myDictionary.update({"grade":20})

# View of Keys, Items, Values
dictKeys = myDictionary.keys()
print(dictKeys)
dictValues = myDictionary.values()
print(dictValues)
dictItems = myDictionary.items()
print(dictItems)


myDictionary["newItem"] = 947


print(dictKeys)
print(dictValues)
print(dictItems)


#Remove items from a dictionary

print(myDictionary)
theItem = myDictionary.pop("newItem")
#python 8 and above
theItem = myDictionary.popitem() #last item
#python 7 and below
theItem = myDictionary.popitem() #random item
print(theItem)
print(myDictionary)


print(myDictionary)

del myDictionary["name"]

print(myDictionary)

myDictionary.clear()

del myDictionary

# Nested Dictionaries
studentDict = {"name": "amir", "surname":"ahmadi" , "std": 97888023}
classDict = {
    97888023 : {
        "name" : "amir",
        "surname" : "ahmadi"
    },
    97888024 : {

    }
}

# Get key by value
mydict = {'ab': 16, 'cd':'hi'}
print(list(mydict.keys())[list(mydict.values()).index(16)])

#Error handling
theItem = studentDict.setdefault("name", "not defined")
theItem = studentDict.setdefault("name1", "not defined")

#%% Conditions (if and else)

num1 = 10
num2 = 12

if num1 == num2:
    #do anything
    print("is equal")

if num1 != num2:
    pass

if num1 > num2:
    pass

if num1 >= num2:
    pass

if num1 < num2:
    pass

if num1 <= num2:
    pass

#Indentation is important

#Error
# if num1 == num2:
# print("hi")



# else
if num1 == num2:
    pass
else:
    pass

# elif
if num1 == num2:
    pass
elif num1 > num2:
    pass
else:
    pass


mydict = {
    23 : {
        "name" : "amir",
        "age" : 35
    },

    24 : {
        "name" : "ali",
        "age" : 25
    }
}

if mydict[23]["age"] > mydict[24]["age"] :
    print(mydict[23]["name"])

num1 = 10
num2 = 12

if num1 > num2:
    print("num1")
elif num2 > num1:
    print("num2")
else:
    print("=")