#logical operators
a=10
b=20
c=30
"""
AND:-this is a logical and operator which returns true if both the conditions are true
OR:-this is a logical or operator which returns true if any one of the conditions is true
NOT:-this is a logical not operator which returns true if the condition is false
"""
print(a<b and b<c)
print(a<b and b>c)
print(a>b and b<c)
print(a>b and b>c)
print(a<b or b<c)
print(a<b or b>c)
print(a>b or b<c)
print(a>b or b>c)
print(not(a<b and b<c))
