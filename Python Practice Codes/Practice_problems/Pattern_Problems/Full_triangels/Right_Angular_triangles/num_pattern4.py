'''
for n == 4
1
23
456
78910
'''
n = int(input())
k = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(k, end="")
        k = k+1
    print()