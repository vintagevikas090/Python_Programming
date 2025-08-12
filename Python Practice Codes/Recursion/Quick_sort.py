def partition(arr, si, ei):
    pivot = arr[si]
    pivot_index = si
    # finding number smaller than pivot
    cnt = 0
    for i in range(si, ei+1):
        if arr[i]<pivot:
            cnt+=1
    pivot_index += cnt
    # putting pivot at correct position
    arr[si], arr[pivot_index]=arr[pivot_index], arr[si]
    
    # Making smaller and larger part around pivot
    i,j = si,ei
    while i<j:
        if arr[i]<pivot:
            i+=1
        elif arr[j]>=pivot:
            j-=1
        else:
            arr[i], arr[j]= arr[j], arr[i]
            i+=1
            j-=1
    return pivot_index

def QuickSort(arr, si, ei):
    if si>=ei:
        return
    i = partition(arr, si,ei)
    QuickSort(arr, si, i-1)
    QuickSort(arr, i+1, ei)
    return arr
    
a = [7,4,3,7,9,2,4,6,8,5]
QuickSort(a, 0,len(a)-1)