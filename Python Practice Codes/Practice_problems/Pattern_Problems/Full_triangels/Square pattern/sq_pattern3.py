'''
for n == 4
1111
2222
3333
4444
'''
#method 1

n = int(input())
i = 1
while i <= n:
    j = 1
    while j<=n:
        print(i, end="")
        j= j+1
    print()
    i = i+1

#method 2

n = int(input())
for i in range(1, n+1):
    for j in range(n):
        print(i, end= "")
    print()