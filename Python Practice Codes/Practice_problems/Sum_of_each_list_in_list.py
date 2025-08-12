l = [[1,2], [3,4], [2, 4]]

# Method 1(for all kind of lists)
for i in l:
    sum = 0
    for j in i:
        sum+=j
    print(sum, end=" ")
    
#method 2
# For fixed column size
n = 3
m = 2
for i in range(n):
    sum = 0
    for j in range(m):
        sum+=l[i][j]
    print(sum, end=" ")