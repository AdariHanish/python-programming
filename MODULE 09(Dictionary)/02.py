#acessing the data in dictionary
d={"name":"Hanish","age":20,"rollno":504}
print("this is name:",d["name"])
print("this is age:",d["age"])
print("this isrollno:",d["rollno"])

#by using get method
print("this is name:",d.get("name"))
print("this is age:",d.get("age"))
print("this is rollno:",d.get("rollno"))
"""
the advantage of using the get method is :
if we use the get method and the key is not present in the dictionary then it will not show any error
if the key has no value or the key is not present also it wont show any error
"""