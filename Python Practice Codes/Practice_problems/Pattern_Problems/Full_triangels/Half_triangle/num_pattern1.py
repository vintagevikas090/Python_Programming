'''
for n == 5
    1
   212
  32123
 4321234
543212345
'''
n = int(input())
i = 1
while i<=n:
    #spaces
    j = 1
    while j<=(n-i):
        print(" ", end="")
        j = j+1
    
    #decreasing no
    j = 1
    k = i
    while j<=i:
        print(k, end="")
        k = k-1
        j = j+1
    
    #increasing no
    k = 2
    j = 1
    while j<=i-1:
        print(k, end="")
        k = k+1
        j = j+1
        
    print()
    i = i+1