'''
for n == 4
ABCD
BCDE
CDEF
DEFG
'''
n = int(input())
i = 1
k = 'A'
while i<=n:
    j = 1
    p = ord(k)
    while j<=n:
        print(k, end="")
        temp = ord(k)
        k = chr(temp+1)
        j = j+1
    print()
    k = chr(p+1)
    i = i+1