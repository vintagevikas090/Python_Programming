'''
for n == 4
   1
  12
 123
1234
'''
n = int(input())
i = 1
while i<=n:
    j, k=1,1
    while j<=n:
        if j<=(n-i):
            print(" ", end="")
        else:
            print(k, end="")
            k = k+1
        j = j+1
    print()
    i =i+1