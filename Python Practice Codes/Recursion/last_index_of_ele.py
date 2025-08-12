# Method 1

def lastIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    smallerList=a[1:]
    smallerListOutput=lastIndex(smallerList,x)
    if smallerListOutput!=-1:
        return smallerListOutput+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1

# Method 2        
        
def lastIndexB(a,x,si):
    l=len(a)
    if si==l:
        return -1
    smallerListOutput=lastIndexB(a,x,si+1)
    if smallerListOutput!=-1:
        return smallerListOutput
    else:
        if a[si]==x:
            return si
        else:
            return -1

a = [1,4,5,4,8]
x=4
print(lastIndex(a,x))
print(lastIndexB(a,x,0))