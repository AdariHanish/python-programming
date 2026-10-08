#question
'''
Use finally block
'''
#answer/code
try:
    f = open("demo.txt", "r")
    print(f.read())
finally:
    f.close()
    print("File closed.")