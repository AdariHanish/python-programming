#question
'''
 Append to a file
'''
#answer/code
with open("demo.txt", "a") as f:
    f.write("\nAppended line.")