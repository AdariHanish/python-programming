#negitive indexing using for loop
s=input("enter a name:")
for i in range(len(s)-1,-1,-1):
    print(s[i],f"this is the {i+1} letter of the name")