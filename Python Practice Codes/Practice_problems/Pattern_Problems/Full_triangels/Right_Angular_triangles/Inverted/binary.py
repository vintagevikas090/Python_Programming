'''
for n == 5
11111
0000
111
00
1
'''
n = int(input())
i = 1
k = 0
while i<=n:
    if i%2== 0:
        k = 0
    else:
        k = 1
    j = 1
    while j<=(n-i+1):
        print(k, end="")
        j = j+1
    print()
    i = i+1


# Using for loop

n = int(input())
k = 0
for i in range(1, n+1):
    if i%2==0:
        k = 0
    else:
        k = 1
    for j in range(1, n-i+2):
        print(k, end="")
    print()
    