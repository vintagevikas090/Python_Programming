'''
for n == 4
****
***
**
*
'''
n = int(input())
i = 1
while i<=n:
    j = n-i+1
    while j>0:
        print("*", end="")
        j = j-1
    print()
    i = i+1