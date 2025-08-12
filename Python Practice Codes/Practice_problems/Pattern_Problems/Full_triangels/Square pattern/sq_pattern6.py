'''
for n == 4
000000000
000000000
000000000
000000000
'''
n = int(input())
i = 1
k = '*'
while i<=n :
    j = 1
    while j<=(2*n+1):
        if i!=1 and j!=1 or j<=(n-i):
            k = '0'
            print(k, end="")
        else:
            print(k, end="")
        j = j+1
    print()
    k = '0'
    i = i+1