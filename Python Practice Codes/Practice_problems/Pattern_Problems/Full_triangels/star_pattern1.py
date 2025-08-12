'''
for n == 7
   *
  ***
 *****
*******
 *****
  ***
   *
   '''
n = int(input())
k = (n+1)//2
#upper triangle
for  i in range(1, n+1):
    if i<=k:
        #spaces
        for j in range(1, k-i+1):
            print(" ", end="")
        #numbers
        for j in range(1, 2*i): 
            print("*", end="")
    else:
        temp = i
        i = 2*k-i
        #spaces
        for j in range(1, k-i+1):
            print(" ", end="")
        #numbers
        for j in range(1, 2*i):
            print("*", )
    print()