'''
for n === 7 
1            1
12          21
123        321
1234      4321
12345    54321
123456  654321
12345677654321
'''
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=2*n:
        if j<=i:
            print(j, end="")
            j = j+1
        else: 
            print(" ", end= "")
            j = j+1
            
        if j>n and j<2*n:
            k = 1
            while k<=n-i:
                print(" ", end="")
                k = k+1
            k = i
            while k >0:
                print(k, end="")
                k = k-1
            j = j+1
            break
    print()
    i = i+1