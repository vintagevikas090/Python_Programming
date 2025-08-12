'''
Selection sort is an algorithm that selects the smallest element from an unsorted list in
each iteration and places that element at the beginning of the unsorted list.
'''

def selection_sort(A):
    for i in range(len(A)):
        min_index=i
        for j in range(i+1,len(A)):
            if A[j]<A[min_index]:
                min_index=j
        A[i],A[min_index]=A[min_index],A[i]
    return A

selection_sort([13,4,9,5,3])