#%% JSON
import json

vjson = '{ "name" : "amir" , "age" : 23 }'

myValue = json.loads(vjson)

print(myValue["name"])

mydict = {
    "name" : "amir",
    "age" : 23
}

x = json.dumps(mydict)

print(x)

print(json.dumps(["a","b","c"]))
print(json.dumps(("a","b","c")))
print(json.dumps("hi my name is amir"))
print(json.dumps(23))
print(json.dumps(23.5))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


print(json.dumps(x, indent=3 , sort_keys=True))

#%% Work With File

myFile = open("myFile.txt","a")

# v = json.loads(myFile.read())
myFile.write("\nhi my name is amir")
# print(myFile.read())

myFile.close()

myFile = open("myFile.json")

x = json.loads(myFile.read())

myFile.close()

print(x["age"])
x["age"] = 34
print(x["age"])

myFile = open("myFile.json", "w")

value = json.dumps(x, indent=3)

myFile.write(value)

myFile.close()

myFile = open("myFile.csv")

print(myFile.read(5))
print(myFile.read(5))
print(myFile.read(5))
print(myFile.read(5))


x = "amir hossein hello "

import re

x = re.sub("hello", "hi", x)

print(x)


myFile = open("myFile11.txt", "x")

import os

# if os.path.exists("myFile11.txt"):
#     os.remove("myFile11.txt")
# else:
#     print("not exist")

os.rmdir("a")

import pandas as pd

x = pd.read_json("myFile.json")

print(x)



