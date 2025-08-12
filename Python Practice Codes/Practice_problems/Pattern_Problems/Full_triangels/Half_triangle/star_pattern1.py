'''
for n == 4
   *
  ***
 *****
*******
'''
n = int(input())
i = 1
while i<=n:
    j = 1
    #spaces
    while j<=(n-i):
        print(" ", end="")
        j = j+1
    
    j = 1
    while j<=i:
        print("*", end="")
        j = j+1

    j = 1
    k = i-1
    while k>0:
        print("*", end="")
        k = k-1
    
    print()
    i = i+1