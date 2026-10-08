#class with more than one method
class Human:
    species = "Homo sapiens"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"\nHi, I'm {self.name}. I'm {self.age} years old and I'm {self.gender}.")

    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult.")
        else:
            print(f"{self.name} is not an adult.")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

# ---------- User Input ----------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

# ---------- Create Human object ----------
person = Human(name, age, gender)

# ---------- Call Methods ----------
person.introduce()
person.is_adult()
person.birthday()
person.is_adult()
