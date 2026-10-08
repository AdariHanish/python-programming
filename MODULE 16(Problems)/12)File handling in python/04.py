#question
'''
Read line by line
'''
#answer/code
with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())