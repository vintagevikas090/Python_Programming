'''
Bubble sort is an algorithm that compares the adjacent elements and swaps their positions
if they are not in the intended order. The order can be ascending or descending.
'''

def bubble_sort(a):
    for i in range(len(a)):
        print("This is pass ",i+1)
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                print("The pair is",a[j],"and ",a[j+1])
                a[j],a[j+1]=a[j+1],a[j]
    return a

bubble_sort([8,5,3,1])



# Optimised Code

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):  # since each time one element is getting to it's correct position
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
bubble_sort([9,5,7,3,1,4])