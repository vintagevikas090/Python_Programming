'''
Sum of Every Element in a Column
'''

l = [[1,2], [3,4], [2, 4]]

n = 3
m = 2
for j in range(m):
    sum = 0
    for i in range(n):
        sum+=l[i][j]
    print(sum, end=" ")