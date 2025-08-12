'''
for n == 4
*000*000*
0*00*00*0
00*0*0*00
000***000
'''
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=2*n+1:
        if j<n+1:
            if j == i:
                print("*", end="")
            else:
                print('0', end="")
            j = j+1
            
        elif j>n+1:
            if j == (2*n+2-i):
                print("*", end="")
            else:
                print('0', end="")
            j = j+1
            
        else:
            print("*", end="")
            j = j+1
    print()
    i = i+1