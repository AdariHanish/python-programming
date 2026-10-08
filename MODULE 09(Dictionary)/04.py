#deletion operation in dictionary
d={"name":"Hanish","name1":"adari","age":20,"rollno":504}
print("the dictionary is:",d)
#citizenship check
print("name" in d)
#deletion
del d["name"]
print("the dictionary after deleting the name is:",d)
#pop
print("the poped age value of the dicitonary is:",d.pop("age"))
#delete entire dictionary
del(d)
print("the dictionary is entirely deleted")