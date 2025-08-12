'''
for n == 4
ABCD
ABCD
ABCD
ABCD
'''
n = int(input())
i = 1
while i<=n:
    j = 1
    k = 'A'
    while j<=n:
        print(k, end="")
        temp = ord(k)
        k = chr(temp+1)
        j = j+1
    print()
    i = i+1