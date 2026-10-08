#keyword arguments
def add(**kwargs):
    print("\nIn the key word arguments the keys and the values are:",kwargs)
    print("\n-----------the individual key:values are------------")
    for key,value in kwargs.items():
        print(f"{key}={value}")
add(name="Hanish",age=20,city="Bangalore\n")