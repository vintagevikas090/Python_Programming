'''
for n == 4
   1
  121
 12321
1234321
'''
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=(n-i):
        print(" ", end="")
        j = j+1
    
    k = 1
    j = 1
    while j<=i:
        print(k, end="")
        k = k+1
        j = j+1
    
    k = i-1
    j = 1
    while k>=1:
        print(k, end="")
        k = k-1
    print()
    i = i+1