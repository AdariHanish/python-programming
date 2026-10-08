#problem 
"""
find the frequency of the character in a string
"""
s=input("enter the string:")
d={}
for i in s:
    print(i)
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
