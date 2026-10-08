print("------ Starting Error Demonstration ------")
# 1. SyntaxError
try:
    eval("if True print('Syntax error!')")
except SyntaxError as e:
    print("Caught SyntaxError:", e)
# 2. IndentationError
bad_code = """
def bad_indent():
print('Indented incorrectly')
"""
try:
    exec(bad_code)
except IndentationError as e:
    print("Caught IndentationError:", e)
# 3. NameError
try:
    print(undefined_variable) # type: ignore
except NameError as e:
    print("Caught NameError:", e)
# 4. TypeError
try:
    result = "Value: " + 5
except TypeError as e:
    print("Caught TypeError:", e)
# 5. FileNotFoundError
try:
    with open("no_such_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print("Caught FileNotFoundError:", e)
# 6. ZeroDivisionError
try:
    value = 10 / 0
except ZeroDivisionError as e:
    print("Caught ZeroDivisionError:", e)
print("------ End of Script ------")