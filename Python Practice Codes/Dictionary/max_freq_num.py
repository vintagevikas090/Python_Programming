'''You are given an array of integers that contain numbers in random order.
Write a program to find and return the number which occurs the maximum times in the given input.

If two or more elements are having the maximum frequency, return the element which occurs in the array first.'''


n = int(input())
values = [int(i) for i in input().split()]

def freq_of_num(arr):
    freq = dict()
    for i in arr:
        if freq.get(i, None) == None:
            freq[i] = 1
        else:
            freq[i] += 1

    max_occ = 0
    max_occ_num = 0

    for num in freq:
        if freq[num]>max_occ:
            max_occ = freq[num]
            max_occ_num = num
        
    return max_occ_num

print(freq_of_num(values))