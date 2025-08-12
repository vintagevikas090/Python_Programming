# First Occurance of element when Duplicates are present

def search(nums, target):
    l,u = 0, len(nums)-1
    mid = (l+u)//2
    while True:
        if target == nums[mid]:
            #dec mid upto one position before the first index at which target is present
            while nums[mid]==target:
                mid-=1
            return mid+1  #first occurance
        elif l>u:
            return -1
        elif target>nums[mid]:
            l = mid+1
            mid = (l+u)//2
        elif target<nums[mid]:
            u = mid-1
            mid = (l+u)//2

A = [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
n = int(input())
print(search(A, n))