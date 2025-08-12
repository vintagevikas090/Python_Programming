def merge(a1,a2,a): 
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if(a1[i]<a2[j]):
            a[k]=a1[i]
            k=k+1
            i=i+1
        else:
            a[k]=a2[j]
            k=k+1
            j=j+1
    while i<len(a1):
        a[k]=a1[i]
        k=k+1
        i=i+1
    while j<len(a2):
        a[k]=a2[j]
        k=k+1
        j=j+1


def merge_sort(a):
    if len(a)==0 or len(a)==1:
        return
    mid=len(a)//2
    a1=a[0:mid]
    a2=a[mid:]
    
    merge_sort(a1)
    merge_sort(a2)
    merge(a1,a2,a)

def pair_sum(arr, n, num):
    low, high = 0, n-1
    count= 0
    while low<high:
        if arr[low]+arr[high] < num:
            low+=1
        elif arr[low]+arr[high] >num:
            high-=1
        else:
            if arr[low]==arr[high]:
                m = arr.count(arr[low])
                count = count + m*(m-1)/2
                low +=1
                high-=1
            else:
                c1 = arr.count(arr[low])
                c2 = arr.count(arr[high])
                count = count+(c1*c2)
                low+=c1
    return count

a = [1, 3, 6, 2, 5, 4, 3, 2, 4]
merge_sort(a)
print(a)
print(pair_sum(a, 9, 7))
