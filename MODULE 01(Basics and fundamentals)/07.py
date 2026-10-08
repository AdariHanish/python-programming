# type conversion
# implicit type conversion
print("this is implicit type conversion")
a=5
b=5.5
result=(a+b)
print(f"the datatype of a ({a}) is:",type(a))
print(f"the datatype of b ({b}) is:",type(b))
print(f"the datatype of result ({result}) is:",type(result))

#explicit type conversion

# int to float
print("\nint to float")
a = 10
b = float(a)
print(b)
print(type(b))
# float to int
print("\nfloat to int")
n = 9.8
y = int(n)
print(y)
print(type(y))
print("\nstring to int")
s = "123"
num = int(s)
print(num)
print(type(num))
print("\nint to string")
n = 123
s = str(n)
print(s)
print(type(s))