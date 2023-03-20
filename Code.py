def factorial(n):
    if n<0:
        return ':D'
    if n==0:
        return 1
    return factorial(n-1)*n

def fibonacci(n):
    if n <=1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def func1(n):
    if n<=2:
        return n
    else
        return 5*func1(n-1) - 8*func1(n-2) + 4*func1(n-3)

print(factorial(3))


