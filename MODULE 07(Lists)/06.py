#list operations
n = list(map(int, input("Enter the list elements separated by commas: ").strip().split(',')))
print("the list is:",n)
#count
m=int(input("enter the element which coutn should be known:"))
print(f"the count of element ({m}) in the list is:",n.count(m))
#index
o=int(input("enter the element which index should be known:"))
print(f"the index of the element {o} is:",n.index(o))
#pop
print("the last element of the list is:",n.pop())
#remove
p=int(input("enter the element which should be removed:"))
{n.remove(p)}
print(f"the element that is removed from the list is:{p}","\nthe updated list is:",n)
#sort
print(f"the sorted list is:{n.sort()}",n)
#insert
a=int(input("enter the index value where u want to insert the element:"))
b=int(input("enter the value that is to be placed in that index value:"))
{n.insert(a,b)}
print(f"the value {b} is placed at the index {a} in the list and the updated list is:",n)
#append
a=int(input("enter the value that is to be appended:"))
n.append(a)
print(f"the value {a} is appended to the list and the updated list is:",n)
#extend
c=list(map(int, input("Enter the list elements that u need to extend and they are separated by commas: ").strip().split(',')))
{n.extend(c)}
print(f"the extended list is:",n)