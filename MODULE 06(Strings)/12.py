#check wether the string is palindrome or not

n=input("enter the string:")
x=n[::-1]
if n==x:
    print("palindrome")
else:
    print("not palindrome")