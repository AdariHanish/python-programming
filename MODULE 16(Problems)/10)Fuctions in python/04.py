#question
'''
Arguments Check
Given the following function fun1()
def fun1(name, age):
    print(name, age)

Select all the syntactically correct function calls to this function.

fun1("Mohit", age=23)
fun1(age =23, name="Mohit")
fun1(name="Mohit", 23)
fun1(23, "Mohit")
'''
#answer/code
# fun1("Mohit", age=23)
# fun1(age =23, name="Mohit")
# fun1(23, "Mohit")

#check:-
def fun1(name, age):
    print(name, age)
fun1("Mohit", age=23)
fun1(age =23, name="Mohit")
fun1(23, "Mohit")