#Write a python script to generate Fibonacci terms using generator function?

a = int(input('Give amount: '))
def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
print (list(fib(a)))