'''
 Largest of sum of each columns's sum in a 2D Lists
 '''

l = [[1,2], [3,4], [2, 4]]
sum, col = 0, 0
n = 3
m = 2
for j in range(m):
    temp = 0
    for i in range(n):
        temp += l[i][j]
    if temp>sum:
        sum = temp
        col = j
print("Column", j, "have Largest sum = ", sum)