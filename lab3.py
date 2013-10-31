n = 42
series = '0,1,1,2,3,5,8,13'
import math

def fib(n):
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b
    
fib(n)

if series == fib:
    fib()

