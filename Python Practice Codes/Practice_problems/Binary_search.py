'''
You are given an integer array 'A' of size 'N', sorted in non-decreasing order. 
You are also given an integer 'target'.
Your task is to write a function to search for 'target' in the array 'A'.
If it exists, return its index in 0-based indexing. Otherwise, return -1.
'''

A = [1, 3, 7, 9, 11, 12, 45]

l,u = 0, len(A)-1
n = int(input())
value = 0
flag = True
while flag:
    mid = (l+u)//2
    if n == A[mid]:
        value = mid
        flag = False
    elif l>u:
        value = -1
        flag = False
    elif n>A[mid]:
        l = mid+1
    elif n<A[mid]:
        u = mid-1    
print(value)
