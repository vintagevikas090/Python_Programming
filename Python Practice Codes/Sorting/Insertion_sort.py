def insertionSort(arr):
    
    length = len(arr)
    for i in range(1,length):
        j=i-1
        temp = arr[i]
        #Shifting elements till this condition holds
        while(j>=0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j = j - 1
        # j+1 is correct position for ith element
        arr[j+1] = temp

arr = [9,8,5,6,7,1,10,11]
insertionSort(arr)
print(arr)