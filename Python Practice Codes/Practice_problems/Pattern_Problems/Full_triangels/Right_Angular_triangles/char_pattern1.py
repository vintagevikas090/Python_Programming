'''
for n == 4
A
BC
CDE
DEFG
'''
n = int(input())
i = 1
k= 'A'
while i<=n:
    j = 1
    s = ord(k)
    while j<=i:
        print(k, end="")
        temp = ord(k)
        k = chr(temp+1)
        j = j+1
    print()
    i = i+1
    k = chr(s+1)