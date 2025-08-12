# First index of an element in list

def firstindex(arr, n, si=0):
    l = len(arr)
    if si == l:
        return -1
    if arr[si]==n:
        return si
    return firstindex(arr, n, si+1)
    
li = [1,2,3,5,6,4,7, 4]
print(firstindex(li, 4))


# method 2

def firstIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    smallerList=a[1:]
    smallerListOutput=firstIndex(smallerList,x)
    
    if smallerListOutput==-1:
        return -1
    else:
        return smallerListOutput+1
