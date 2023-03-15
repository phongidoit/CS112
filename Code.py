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

print(factorial(3))


