#difference of two sets
s1=set(map(int,input("enter the set elements seperated by commas:").split(",")))
s2=set(map(int,input("enter the set elements seperated by commas:").split(",")))
print("the difference of two sets is:",s1.difference(s2))