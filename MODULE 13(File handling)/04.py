#writing a file
f=open("file.txt","w")
f.write("hello world")
f.close()
#using with open method
with open("file.txt","w") as f:
    f.write("hello world")
