def intersections(arr1, n, arr2, m) :
    #Your code goes here
    for i in arr1:
        for j in arr2:
            if i == j:
                print(i, end=' ')
                arr2.remove(j)
                break

a1 = [11, 11, 12, 12, 13]
a2 = [11, 12, 12, 13, 13]
intersections(a1, 5, a2, 5)
