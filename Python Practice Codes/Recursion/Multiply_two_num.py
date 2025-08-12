'''Multiplication (Recursive)....
Given two integers M & N, calculate and return their multiplication using recursion.
You can only use subtraction and addition for your calculation. No other operators are allowed.'''

def multiply(m, n):
    if n==0 or m ==0:
        return 0
    if n<0:
        m = -m
        n = -n    
    return m + multiply(m, n-1)

a = int(input())
b = int(input())
print(multiply(a,b))