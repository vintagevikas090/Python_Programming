'''
Sum of the elements of list
'''

def sumoflist(a, si, s = 0):
    length = len(a)
    if si==length:
        return s
    s = s+a[si]
    temp = sumoflist(a, si+1, s)
    return temp
    
l = [1,2,3,4,5,6,7]
ans = sumoflist(l,0)
print(ans)