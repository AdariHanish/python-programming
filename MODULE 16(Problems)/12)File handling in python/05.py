#question
'''
 Count words in a file
'''
#answer/code
with open("demo.txt", "r") as f:
    words = f.read().split()
    print("Total words:", len(words))