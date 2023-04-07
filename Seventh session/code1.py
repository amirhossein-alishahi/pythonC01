#%% Function 

# defining a funciton
def myFunction():
    print("hi")

# Calling a function
myFunction()


#Arguments
def myFunction(name):
    print(name)

myFunction("amir")

#_______________

def myFunction(fname,name):
    print(f"Hi, my name is {name} {fname}")

myFunction("amir","ali")


#_________________
def myFunction(*names):
    print(f"Hi, my name is {names[0]} and he is {names[1]}")

myFunction("amir","ali")

#__________________

def myfunction(**names):
    print(names["fname"])

myfunction(fname = "ali", name = "amir")



def myfunction1(var,*vars):
    print(vars)

myfunction1(1,2,3,4,5)

# Default parameter value

def myfunction(name = "amir"):
    print(name)

myfunction("ali")
myfunction()
myfunction("hossein")



