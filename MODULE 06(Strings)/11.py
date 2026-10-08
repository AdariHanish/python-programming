#printing vowels
n=input("enter the name:")
x=[]
for i in n:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        x.append(i)
if len(x)==0:
    print("no vowels in the name")
elif len(x)==1:
    print(f"the vowels in the name ({n}) is:",x)
else:
    print(f"the vowels in the name ({n}) are:",x)