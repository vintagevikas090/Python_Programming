# printing N natural Numbers

def print_dec_n(n):
    if n>0:
        print(n, end=" ")
        print_dec_n(n-1)

def print_inc_n(n):
    if n==0:
        return
    print_inc_n(n-1)
    print(n, end=" ")
    return

num = int(input())
print_dec_n(num)
print()
print_inc_n(num)