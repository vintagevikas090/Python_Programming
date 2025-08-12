'''
Wave Print

For a given two-dimensional integer array/list of size (N x M), 
print the array/list in a sine wave order, i.e, print the first column top to bottom, 
next column bottom to top and so on.
'''

l = [[1,  2,  3,  4], [5,  6,  7,  8], [9, 10, 11, 12]]
n = 3
m = 4
for j in range(m):
    if j%2==0:
        for i in l:
            print(i[j], end=' ')
    else:
        for i in range(n-1, -1, -1):
            print(l[i][j], end=' ')