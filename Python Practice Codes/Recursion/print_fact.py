'''print factorial of number using recursion instead of returning it'''
'''Hit: use Top to Down approach'''

def print_fact(n, ans = 1):
    if n == 0:
        print(ans)
        return 
    ans = ans * n
    print_fact(n-1, ans)

N = int(input('Enter the number: '))
print_fact(N)