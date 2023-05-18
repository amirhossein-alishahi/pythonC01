class MyClass:
    name = ""
    fname = ""
    age = None

print(MyClass.x)


ob1 = MyClass()
ob1.x = 3
ob2 = MyClass()
ob2.x = 4
print(ob1.x)
print(ob2.x)


class Person:
    name = ""
    fname = ""
    age = None


p1 = Person()
p1.name = "amir"
p1.fname = "ali"
p1.age = 23

p2 = Person()
p2.name = "amir1"
p2.fname = "ali1"
p2.age = 24

print(p1.name)
print(p2.name)

class Person:

    nCode = None
    weight = None
    h= None

    def __init__ (self,name,fname,age,h,w):
        self.name = name
        self.fname = fname
        self.age = age
        self.h = h
        self.weight = w
        print("hi")
    
    def __str__(x) -> str:
       return f"{x.name} {x.age}"
    
    def f1(self):
        print("a")

    def bmi(self):
        return self.weight / self.h**2

    

    


p1 = Person("amir","ali",23,1.92,75)
p1.f1()

del p1.name


print(p1.bmi())


class Person:

    nCode = None
    weight = None
    h= None

    def __init__ (self,name,fname,age,h,w):
        self.name = name
        self.fname = fname
        self.age = age
        self.h = h
        self.weight = w
        # print("hi")
    
    def __str__(x) -> str:
       return f"{x.name} {x.age}"
    
    def f1(self):
        print("a")

    def bmi(self):
        return self.weight / self.h**2


class Student(Person):
    def __init__(self, name, fname, age, h, w,sID):
        super().__init__(name, fname, age, h, w)
        self.sID = sID
        


s1 = Student("na", "bb", 22, 1.92, 75,33)
print(s1.sID)

class Car:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model 

    def move(self):
        print(f"Drive {self.brand}")

car1 = Car("x","y")
car2 = Car("x1","y1")

class Boat:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model 

    def move(self):
        print("Sail")

class Plane:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model 

    def move(self):
        print("Fly")

car = Car("a","b")
boat = Boat("a","b")
plane = Plane("a","b")

car.move()
boat.move()

class Vehicle:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model 

    def move(self):
        print("")

class Car(Vehicle):
    def move(self):
        print("drive")

myList = [2,3,4,5,6,7]

for i in myList:
    print(i)



class MyNumber:

    x = 0
    z = 1

    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        self.a = self.x
        return self

    def __next__(self):
        if self.a < self.y:
            x = self.a
            self.a +=1*self.z
            return x
        else:
            raise StopIteration
    
for i in MyNumber(5):
    print(i)
print("____________")
for i in MyNumber(4,13):
    print(i)
print("____________")
for i in MyNumber(0,20,2):
    print(i)
print("____________")


for i in range(20):
    print(i)


x = "hi"

def f1():
    print("h")

class MyClass:
    a = 3