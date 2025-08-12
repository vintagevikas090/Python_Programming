# Binary Search using Recursion

def Binary_search(li, si, ei, num):
    if si>ei:
        return False
    mid = (si+ei)//2
    if li[mid]==num:
        return True
    elif li[mid]>num:
        return Binary_search(li, si, mid-1, num)
    else:
        return Binary_search(li, mid+1, ei, num)
    
    
l = [1,2,3,4,5,6,7,8,44,55,66,78]
n = int(input("Enter the number you want to search in List: "))
print(Binary_search(l, 0, len(l)-1, n))