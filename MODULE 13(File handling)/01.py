#opening a file
f=open("requriments.txt")
print("the file type is:",type(f))
#reading the file
print("-------the contents of the file is:--------")
print(f.read())
print("---------end of the file---------")
#closing the file
f.close()
print("the status of the file is closed is:",f.closed)