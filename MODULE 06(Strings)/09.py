#string formatting
name=input("enter the name:")
age=int(input("enter the age:"))
print(" myname is:",name,"and my age is:",age)
print(" myname is:%s and my age is:%d"%(name,age))
print(" myname is:{} and my age is:{}".format(name,age))
print(" myname is:{1} and my age is:{0}".format(age,name))
print(" myname is:{name} and my age is:{age}".format(name=name,age=age))
print(f" myname is:{name} and my age is:{age}")