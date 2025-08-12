'''
for n == 5
1 2 3 4 5 
11 12 13 14 15 
21 22 23 24 25 
16 17 18 19 20 
6 7 8 9 10 
'''

n = int(input())
#increasing triangle
p = 1 
if n%2==0:   
    l = (n+2)//2
else:
    l = (n+1)//2

temp = 0
r = 0

for i in range(1, l+1):
    k =p
    for j in range(1, n+1):
        print(k, end=" ")
        if i == l-1 and j ==n:
            temp = k
        k = k+1
    p = p+n*2
    print()
    
#decreasing triangle
p = temp+1

for i in range(1, l):
    k = p
    for j in range(1, n+1):
        print(k, end=" ")
        k = k+1
    p = p-2*n
    print()