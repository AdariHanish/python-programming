#question
'''
Prime finder
Write a function to return True when the given function is a Prime number else False.

Input format

An Integer is given
Output format

True: if Prime
False: if not
Input sample

5
Input format

True
'''
#answer/code
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n == 2:
        return True   # 2 is the only even prime number
    if n % 2 == 0:
        return False  # eliminate even numbers
    for i in range(3, int(n**0.5) + 1, 2):  # check only odd divisors
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
print(is_prime(n))
