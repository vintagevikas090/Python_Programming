'''
for n == 4
4444
333
22
1
'''
n = int(input())
i = 1
while i<=n:
    j = n+1-i
    while j>0:
        print(n-i+1, end="")
        j = j-1
    print()
    i = i+1