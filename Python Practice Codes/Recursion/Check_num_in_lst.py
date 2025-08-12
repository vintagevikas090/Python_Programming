# Check Number in list or not

def checknum(arr, n):
    l = len(arr)
    if l == 0:
        return False
    if arr[0]==n:
        return True
    smallarray = checknum(arr[1:], n)
    return smallarray


def checknum2(arr, n, index = 0):
    l = len(arr)

    if index == l:
        return False
    if arr[index] == n:
        return True
    return checknum2(arr,n,index+1)

li = [1,2,3,4,5,6,7]
print(checknum(li, 4))