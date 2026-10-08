#question
'''
Create a class Person with name and age attributes
'''
#answer/code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p = Person("Alice", 25)
p.display()