#mutability in tuple
t=([1,2,3,4,5],"Kiran")
print(t[0])
print(f"the first element of the tuple is:",t[0][0])
t[0][0]=6
print(t)