'''
for n == 11
* 
 * * 
  * * * 
   * * * * 
    * * * * * 
     * * * * * * 
    * * * * * 
   * * * * 
  * * * 
 * * 
* 
'''

n = int(input())
i = 1
k = (n+1)/2
while i<=n:
    temp = i
    if i<=k:
        j =1
        while j<=i-1:
            print(" ", end="")
            j = j+1
        j = 1
        while j<=i:
            print("* ", end="")
            j = j+1
        
    else:
        i = 2*k-i
        j =1
        while j<=i-1:
            print(" ", end="")
            j = j+1
        i = temp
        
        i = 2*k-i
        j =1
        while j<=i:
            print("* ", end="")
            j = j+1
        i = temp
        
        
    print()
    i = i + 1