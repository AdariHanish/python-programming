#syntax error
print("----------syntax error----------")
print("hello world"
#name error
print("----------name error----------")
print(a)
#type error
print("----------type error----------")
print("hello world"+10)
#file not found error
print("----------file not found error----------")
print(open("hello.txt"))
#indendation error
print("----------indendation error----------")
if True:
print("hello world")
print("this is a indendation error")
#zero division error
print(10/0)
#logical error
print("----------logical error----------")
print(10/0)
#runtime error
print("----------runtime error----------")
print("hello world"[10])
#value error
print("----------value error----------")
print(int("hello world"))