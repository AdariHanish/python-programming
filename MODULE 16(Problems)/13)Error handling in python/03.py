#question
'''
Catch multiple exceptions
'''
#answer/code
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print("Error:", e)