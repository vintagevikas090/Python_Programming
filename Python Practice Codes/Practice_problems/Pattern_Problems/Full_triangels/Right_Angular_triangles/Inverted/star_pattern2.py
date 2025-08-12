'''
for n === 5
*****
 ****
  ***
   **
    *
    '''
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=n:
        if j<=(i-1):
            print(" ", end="")
        else:
            print("*", end="")
        j = j+1
    print()
    i = i+1