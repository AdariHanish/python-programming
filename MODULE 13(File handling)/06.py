#handling binary file using with open method
with open("file.bin","rb") as f:
    print(f.read())
with open("file.bin","wb") as f:
    f.write(b"hello")
    f.write(b"world")
    f.write(b"!")
    f.write(b"how are you?")
    f.write(b"i am fine thank you")