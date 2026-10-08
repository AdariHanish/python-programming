#creation of set
a={}
print("this is a empty set")
b=set()
print("this is also a empty set")
c={1,2,3,4,5}
print("this is a non empty set:",c)
#set of mixed data type
d={1,2,3,"Hanish",20.5}
print("this is a set of mixed data type:",d)
#string to set
e=set("Hanish")
print("this is a set of string:",e)
#set of string
f={"Hanish","Kiran","Ashika"}
print("this is a set of string:",f)
#iteration over set
g={"Hanish","Kiran","Ashika"}
for key, value in enumerate(g):
    print(f"This is the {key} element of the set: {value}")
'''
the indexing is not possible in set so the enumerate function is used to get the index of the element
'''