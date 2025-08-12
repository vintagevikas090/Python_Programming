'''
for n == 6
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456
'''
n = int(input())
i = 1
k = 0
#upper triangle (5 rows for n=6)
for i in range(1, n):
    k = i
    #spaces
    for j in range(1, i):
        print(" ", end="")
    #number
    for j in range(1, n-i+2):
        print(k, end="")
        k = k+1
    print()
    
#lower triangle
for i in range(1, n+1):
    k = n-i+1
    #spaces
    for j in range(1, n-i+1):
        print(" ", end="")
    #numbers
    for j in range(1, i+1):
        print(k, end="")
        k = k+1
    print()