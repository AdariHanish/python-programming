#delete operation
'''
the delete also have 2 methods
1.pop it delete the first element
2.remove it delete the element which is given
'''
s=set(map(int,input("enter the set elements seperated by commas:").split(",")))
print("the set is:",s)
print("the randomly deleted element is:",s.pop())
print("the updated set is:",s)
x=int(input("enter the element that should be removed form set:"))
s.remove(x)
print("the removed element is:",x)
print("the updates set is:",s)
