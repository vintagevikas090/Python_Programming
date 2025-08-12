'''
Problem statement
You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of the longest consecutive sequence.

The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ..., 'NUM' + L] 
where 'NUM' is the starting integer of the sequence and 'L' + 1 is the length of the sequence.

Note:

If there are any duplicates in the given array we will count only one of them in the consecutive sequence.
For example-
For the given 'ARR' [9,5,4,9,10,10,6].

Output = 3
The longest consecutive sequence is [4,5,6].
'''

# to get the longest cons. sequence
def LongestConsecutiveSequence(arr, n):
    # Write your code here.
    s = set(arr)
    max_len = 0
    max_seq = []
    current_seq = []
    current_len = 0

    for i in s:
        if i - 1 not in s:
            num = i
            current_seq.append(i)
            current_len = 1

            while num+1 in s:
                current_len += 1
                num += 1
                current_seq.append(num)

            if current_len > max_len:
                max_len = current_len
                max_seq = current_seq
        current_seq = [-1]
    return max_seq


# to get LENGTH of the longest consecutive seq

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    s = set(arr)
    max_len = 0
    current_len = 0

    for i in s:
        if i - 1 not in s:
            num = i
            current_len = 1

            while num+1 in s:
                current_len += 1
                num += 1

            max_len = max(max_len, current_len)
            
    return max_len


l = [9,5,4,9,10,10,6]

print(LongestConsecutiveSequence(l, 7))