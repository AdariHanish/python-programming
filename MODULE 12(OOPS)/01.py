#classes and objects
print("---------------this is default values------------------")
class human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
x=human("Hanish", 20)
x1=human("Kiran",25)
x2=human("Ashika",24)
print(x.name,x.age)
print(x1.name,x1.age)
print(x2.name,x2.age)
print("\n")
print("-----------------this is user defined values------------------")
class student:#class is created with name student
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student(input("enter the name:"),int(input("enter the age:")))#object for the class
print(s1.name)#object acessing the values
print(s1.age)#object acessing the values