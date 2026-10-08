#indexing
x=("Hanish","Kiran","Ashika",1,2,4)
for i in range(len(x)):
    print(f"this is the {i} element of the tuple and the element is:",x[i])

#slicing
x=tuple(map(int,input("enter the elements of the tuple separated by commas: ").split(",")))
a=int(input("enter the starting index for the strip:"))
b=int(input("enter the ending index for the strip:"))
c=int(input("enter the step value:"))
print("the sliced tuple is:",x[a:b:c])

#hetrogenous tuple
p=("hanish",2,3.2,True)
for i in range(len(p)):
    print(f"this is the {i} element of the tuple and the element is:{p[i]} and the type of the element is:{type(p[i])}")