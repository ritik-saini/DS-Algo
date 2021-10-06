#factorial using recursion
n = int(input('Enter a Number : '))
def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)

print(factorial(n))