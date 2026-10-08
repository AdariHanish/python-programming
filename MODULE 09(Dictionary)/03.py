#updating dictionary
print("------------general method------------------")
d={"name":"Hanish","age":20,"rollno":504}
print("the original dictionary is:",d)
print("now change the values of the dictionary")
d["name"]=input("enter the new name:")
d["rollno"]=int(input("enter the new rollno:"))
d["age"]=int(input("enter the new age:"))
print("the updated dictionary is:",d)
#using new method
print("-------------new method--------------")
d={"name":"Hanish","age":20,"rollno":504}
print("the original dictionary is:",d)
d["gender"]="male"
print("the updated dictionary is:",d)
#using update method
print("-------------update method--------------")
d={"name":"Hanish","age":20,"rollno":504}
print("the original dictionary is:",d)
print("now change the values of the dictionary")
d.update(name=input("enter the new name:"),rollno=int(input("enter the new rollno:")),age=int(input("enter the new age:")))
print("the updated dictionary is:",d)