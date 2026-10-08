#mutability of list
l=[1,2,3,4,5,6,7,8,9,10]
print("the list is:",l)
x=int(input("enter the index number of the element that is to be changed:"))
print("the value u want to change is:",l[x])
y=int(input("enter the new value:"))
l[x]=y
print("the list after changing the value is:",l)