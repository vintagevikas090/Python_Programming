'''
for n == 5
E
DE
CDE
BCDE
ABCDE
'''
n = int(input())
i = 1
p = ord('A')
k= chr(p+n-1)
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
    k = chr(s-1)