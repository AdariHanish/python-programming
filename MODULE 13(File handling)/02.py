# file operations
'''
Modes:
r  = read
w  = write
a  = append
x  = exclusive creation
wt = write text
rt = read text
wb = write binary
rb = read binary
'''
# read mode
print("-------read mode-------")
with open("requirements.txt") as f:
    print(f.read())
# write mode
print("-------write mode-------")
with open("requirements.txt", "w") as f:
    f.write("hello\n")
# append mode
print("-------append mode-------")
with open("requirements.txt", "a") as f:
    f.write("appended text\n")
# write text mode
print("-------write text mode-------")
with open("requirements.txt", "wt") as f:
    f.write("text mode write\n")
# read text mode
print("-------read text mode-------")
with open("requirements.txt", "rt") as f:
    print(f.read())
# write binary mode (bytes)
print("-------write binary mode (bytes)-------")
with open("requirements.txt", "wb") as f:
    data = "Hello world"
    binary_data = data.encode()  # converts to bytes
    f.write(binary_data)
    print(f"Binary data written (bytes): {binary_data}")
# read binary mode (bytes)
print("-------read binary mode (bytes)-------")
with open("requirements.txt", "rb") as f:
    binary_content = f.read()
    print(f"Binary data: {binary_content}")
    print(f"Human-readable: {binary_content.decode()}")
# exclusive creation mode
print("-------exclusive mode-------")
try:
    with open("requirements_exclusive.txt", "x") as f:
        f.write("Created with exclusive mode.\n")
        print("file created with exclusive mode")
except FileExistsError:
    print("File already exists. 'x' mode failed as expected.")
'''
note:-
The exclusive("x") mode in Python is used to create a new file for writing.
If the file already exists, it will raise a FileExistsError, instead of overwriting it.

🔒 Purpose:
Prevents accidental overwriting of existing files.

Ensures safe file creation, especially useful in:

Logging systems

Unique report/export generation

Config/script auto-generation
'''