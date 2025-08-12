# Merging Between given positions of a list

def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2

        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)

        merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    # Create temporary arrays
    left_arr = [0] * n1
    right_arr = [0] * n2

    # Copy data to temporary arrays
    for i in range(n1):
        left_arr[i] = arr[l + i]

    for j in range(n2):
        right_arr[j] = arr[mid + 1 + j]

    # Merge the temporary arrays
    i = j = 0
    k = l

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
l = 1 
r = 5 

merge_sort(arr, l, r)
print("Array after sorting between positions", l, "and", r, ":", arr)
