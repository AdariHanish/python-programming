#class methods
class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("name:",self.name)
        print("roll:",self.roll)
a=student(input("enter the name:"),int(input("enter the roll no:")))#creation of object
print("-----------------this is printed without using the method--------------------")
print(a.name)
print(a.roll) 
print("\n-----------------this is printed using the method--------------------")
a.display()#object acessing the method