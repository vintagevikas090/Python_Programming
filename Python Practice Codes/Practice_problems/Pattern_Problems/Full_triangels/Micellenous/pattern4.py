'''
for n == 4
4444444
4333334
4333334
4333334
4333334
4333334
4444444
'''
n = int(input())
for i in range(1, 2*n):
    for j in range(1, 2*n):
        if i ==1 or i == 2*n-1 or j == 1 or j==2*n-1:
            print(n, end="")
        else:
            print(n-1, end="")
    print()