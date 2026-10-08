#update operation in sets
'''
the update operation is of 2 methods
1.using the add() method
2.using the update method (iteratable)
'''
print("-------------add method-----------------")
s=set(map(int,input("enter the elements of the set:").split(",")))
print("the set is:",s)
s.add(int(input("enter the element to be added:")))
print("this is the add method and the updated set is:",s)
print("-------------update method-----------------")
a=set(map(int,input("enter the elements of the set:").split(",")))
a.update(map(int,input("enter the elements to be added:").split(",")))
print("this is the update method and the updated set is:",a)
print("----------update method with iteration--------------")
b=set(map(int,input("enter the elements of the set:").split(",")))
b1=input("enter the string to be added:")
b.update(b1)
print("this is the update method and the updated set is:",b)