#question
'''
Handle file not found
'''
#answer/code
try:
    with open("nonexistent.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")