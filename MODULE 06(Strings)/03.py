#ord and char
print("enter 1 to choose ord to char")
print("enter 2 to choose char to ord")
ch=int(input("enter your choice:"))
if ch==1:
    a=input("enter the character:")
    print(ord(a))
elif ch==2:
    a=int(input("enter the ascii value:"))
    print(chr(a))
else:
    print("invalid choice")