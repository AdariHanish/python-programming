#class variable and instance variable
class Student:
    # Class variable
    school_name = "ABC Public School"
    def __init__(self, name, grade):
        # Instance variables(object variables)
        self.name = name
        self.grade = grade
    def display(self):
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("School:", Student.school_name)
# Create instances(objects) of the Student class
s2 = Student("Riya", "9")
s1 = Student(input("Enter name:"), input("Enter grade:"))
s1.display()
print("-------------------------------------------------------")
s2.display()
# Change the class variable for all instances
Student.school_name = "XYZ International School"
print("-------------- After changing school_name -------------------")
s1.display()
print("-------------------------------------------------------")
s2.display()