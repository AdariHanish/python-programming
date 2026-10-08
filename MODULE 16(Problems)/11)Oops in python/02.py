#question
'''
Inheritance — Create Animal class and derive Dog
'''
#answer/code
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof!")

d = Dog()
d.sound()