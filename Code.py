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
    if n<=1:
        return 1
    a = 0
    for i in range(0,n):
        a += 1
    return  a + func1(n-2)

print(factorial(3))


