'''
for n == 5
5432*
543*1
54*21
5*321
*4321
'''
n = int(input())
i = 1
k = 5
while i<=n:
    j = 1
    k = n
    while j<=5:
        if j == n-i+1 :
            print("*", end="")
        else:
            print(k, end="")
        k = k-1
        j = j+1
    print()
    i = i+1