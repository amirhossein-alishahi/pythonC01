class Person:
    def __init__(self,name, fname,h,w):
        self.name = name
        self.fname = fname
        self.h = h
        self.w = w
    
    def __str__(self):
        return f"{self.name} {self.fname}"
    
    def __abc(self):
        print("abc")

    def bmi(self) -> int:
        return self.w / self.h**2
    

class Student(Person):

    def __init__(self,name,fname,h,w,sID):
        Person.__init__(self,name, fname,h,w)
        self.sID = sID

class Math:
    def p(x,y):
        return x+y
    
    def m(x,y):
        return x*y
    
x = 5

def myFunction():
    print("hi")




