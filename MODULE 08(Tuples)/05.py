# tuple operations
x=tuple(map(int,input("enter the tuple elements seperated by commas:").split(",")))
print("the tuple is:",x)
#count
print("count of the element is:",x.count(int(input("enter the element which count should be known:"))))
#index
print("the index of the element is:",x.index(int(input("enter the element which index should be known:"))))
#length
print("the length of the tuple is:",len(x))
#max element
print("the maximum element is:",max(x))
#min element
print("the minimum element is:",min(x))
#sum of elements
print("the sum of the elements is:",sum(x))
#sorted elements
print("the sorted elements are:",sorted(x))
#reversed elements
print("the reversed elements are:",x[::-1])
#iteration
for i in range(len(x)):
    print(f"the {i} of the tuple is:",i)
#concatenation
print("the concatination of 2 tuples is:",x+x)
#tuple to list
print("the list of the tuple is:",list(x))
#list to tuple
print("the tuple of the list is:",tuple(x))