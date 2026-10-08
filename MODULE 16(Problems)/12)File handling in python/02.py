#question
'''
Read from a file
'''
#answer/code
with open("demo.txt", "r") as f:
    content = f.read()
    print(content)