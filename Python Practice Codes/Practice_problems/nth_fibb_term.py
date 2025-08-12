# N th term of fibbonacci

n = int(input())
a = 1
b = 1
i = 2
if n ==1 or n==2:
    print(1)
elif n>2:
    while i<n:
        nxterm = a+b
        a = b
        b = nxterm
        i = i+1
    else:
        print(nxterm)
