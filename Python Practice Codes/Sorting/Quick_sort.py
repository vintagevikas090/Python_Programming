'''
It works along the lines
of choosing one element as a pivot element and partitioning the array around it
such that:
● The left side of the pivot contains all the elements that are less than the pivot
element
● The right side contains all elements greater than the pivot.
'''

def partition(a,si,ei):
    pivot=a[si]
    #find number of elements smaller than pivot
    c=0
    for i in range(si,ei+1):
        if a[i]<pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c]
    
    #correct position of pivot
    pivot_index=si+c
    
    i=si
    j=ei
    while i<j:
        #in smaller array part, if num is smaller than pivot --> no problem
        if a[i]<pivot:
            i=i+1
        #in Larger array part, if num is bigger than pivot --> no problem
        elif a[j]>=pivot:
            j=j-1
        # otherwise swap the elements
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return pivot_index

def quick_sort(a,si,ei):
    if si>=ei:
        return
    
    pivot_index=partition(a,si,ei)
    quick_sort(a,si,pivot_index-1)
    quick_sort(a,pivot_index+1,ei)

a=[6,10,9,8,7,1,3,5,4,2]
print(partition(a,0,len(a)-1))


a=[6,10,9,8,7,1,3,5,4,2]
print(quick_sort(a,0,len(a)-1))
a