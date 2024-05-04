'''write a function fib(n) that takes in a number
as an argument. The function should return the n-th number
of the Fibonacci sequence.

The first and second number of the sequence is 1.
To generate the next number of the sequence, we sum the previous two.'''

def fib(n):
    if (n<=2): return 1
    return fib(n-1) + fib(n-2)

print(fib(6))
print(fib(7))
print(fib(8))

'''Time complexity is 2^n. Using a tree structure...'''

