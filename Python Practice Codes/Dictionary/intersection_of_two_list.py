'''You have been given two integer arrays/lists (ARR1 and ARR2) of size N and M, respectively. 
You need to print their intersection; An intersection for this problem can be defined when both the arrays/lists
contain a particular value or to put it in other words, 
when there is a common value that exists in both the arrays/lists.'''

def printIntersection(arr1, n1, arr2, n2) :
    #Your code goes here
    freq1 = {}
    
    for i in arr1:
        if i in freq1:
            freq1[i]+=1
        else:
            freq1[i] = 1

    result = []
    
    for ele in arr2:
        if ele in freq1 :
            result.append(ele)
            freq1[ele]-=1

    for i in result:
        print(i)
        
arr1 = [2,6,8,5,4,3]
arr2 = [2,3,4,7]

printIntersection(arr1, len(arr1), arr2, len(arr2))