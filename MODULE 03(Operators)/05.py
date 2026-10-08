#special operators
"""
the special operators are the membership operator and the identity operator
membership operator:-this will check if the particular element is present in the sequence(list) or not
identity operator:-this will check if the two variables are pointing to the same object or not
"""
#membership operator
print("-------membership operator-------")
a=[1,2,3,4,5,6,7,8,9,10]
print(f"(in) is a membership operator:",1 in a)
print(f"(not in) is a membership operator:",1 not in a)

#identity operator
print("-------identity operator-------")
c=[10,10]
a=c
b=[10,10]
print(f"(is) is a identity operator:",c is a)
print(f"(is) is a identity operator:",c is b)
print(f"(is not) is a identity operator:",c is not b)