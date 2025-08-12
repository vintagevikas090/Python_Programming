def findGcd(x, y):
    p = min(x,y)
    gcd = 0
    for i in range(1, p+1):
        if x%i ==0 and y%i == 0:
            gcd = i
    return(gcd)

x = int(input())
y = int(input())
print(findGcd(x,y))