'''
for n == 4
1
23
345
4567
'''
n = int(input())
for i in range(1, n+1):
    k = i
    for j in range(1, i+1):
        print(k, end="")
        k = k+1
    print()