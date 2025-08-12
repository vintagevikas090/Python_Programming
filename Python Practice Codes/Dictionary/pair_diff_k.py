'''You are given with an array of integers and an integer K. 
You have to find and print the count of all such pairs which have difference K.

Note: Take absolute difference between the elements of the array.'''

def printPairDiffK(arr, k):
    freq = dict()
    ans = 0

    for num in arr:
        expect1 = (num - k)
        expect2 = (num + k)

        if expect1 in freq:
            ans+=freq.get(expect1, 0)
        if expect1 !=expect2 and expect2 in freq:
            ans+=freq.get(expect2, 0)
        
        if freq.get(num, 0):
            freq[num] += 1
        else:
            freq[num] = 1

    return ans