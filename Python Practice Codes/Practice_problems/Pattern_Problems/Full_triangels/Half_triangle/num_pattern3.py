'''
for n == 4
   1
  232
 34543
4567654
'''
n = int(input())
i = 1
while i<=n:
    j = 1
    while j <=(n-i):
        print(" ", end="")
        j = j+1
        
    #increasing no
    j = 1
    k = i
    while j<=i:
        print(k, end="")
        k = k+1
        j = j+1
    
    #decreasing no
    j = 1
    p = 2*(i-1)
    while j<=(i-1):
        print(p, end="")
        j = j+1
        p = p-1
        
    print()
    i = i+1