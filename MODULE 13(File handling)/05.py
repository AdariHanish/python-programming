#reading a file
f=open("file.txt","r")
print(f.read())
f.close()
#using with open method
with open("file.txt","r") as f:
    print(f.read())
#reading a file line by line
with open("file.txt","r") as f:
    for line in f:
        print(line)
#reading a file character by character
with open("file.txt","r") as f:
    for char in f.read():
        print(char)