# Method 1

def isSorted(a):
    l=len(a)
    if l==0 or l==1:
        return True
    if a[0]>a[1]:
        return False
    smallerList=a[1:]
    isSmallerListSorted=isSorted(smallerList)
    if isSmallerListSorted:
        return True
    else:
        return False

a=[1,2,3,4,5,6,7,8,9]
isSorted(a)


#Method 2

def isSortedBetter(a,si):
    l=len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    isSmallerPartSorted=isSortedBetter(a,si+1)
    return isSmallerPartSorted

a=[1,2,3,4,5,6,7,8,9]
isSortedBetter(a,0)