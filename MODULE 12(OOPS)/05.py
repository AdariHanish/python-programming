#single inheritance
class Animal:  # Inheriting from Dog
    def sound(self):
        print("animal makes a sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks: Bhow!")

# Create objects and call sound method
c = Dog()
c.sound()  # Calls Cat's method (overridden)
c.bark()   #this will work as the class Dog is inheriting from class Animal