#creation of dictionary
d={}
print("this is a empty dictionary",d)
x=dict()
print("this is also a empty dictionary",x)
#creation of dictionary with key value pairs
y={"name":"Hanish","age":20,"rollno":504}
print("this is a dictionary with key value pairs",y)
#creation of dictionary with key value pairs
z=dict(name="Hanish",age=20,rollno=504)
print("this is also a dictionary with key value pairs",z)
#creation of dictionary with key value pairs using zip
name=["Hanish","Kiran","Ashika"]
rollno=[504,80,4]
x=dict(zip(name,rollno))
print("the dictionary created using zip is:",x)