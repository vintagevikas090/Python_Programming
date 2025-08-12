'''
Problem statement
Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
0 <= N <= 10^8
Time Limit: 1 sec
Sample Input 1:
10 
 95 -97 -387 -435 -5 -70 897 127 23 284
Sample Output 1:
5
Explanation:
The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897 
Note
You don't have to print anything. Just complete the definition of the function given and return the value accordingly.
'''

def subsetSum(l):
    n = len(l)
    if n < 2:
        return n
    sum_index_dict = {0: -1}
    current_sum = 0
    max_len = 0
    current_len = 0

    for i in range(n):
        current_sum += l[i]
        #Logic: keep the track of the current_sum at every index 
        if current_sum in sum_index_dict:
            #If we have seen this sum before,  then it means there is a valid subarray ending at the current index.
            current_len = i - sum_index_dict[current_sum] 
            max_len = max(max_len, current_len)
        else:
            sum_index_dict[current_sum] = i
    return max_len


# Main
n=int(input('No of elements: '))
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))


'''
eg. list = [95 -97 -387 -435 -5 -70 897 127 23 284]
then sum_index_dict = {95:0, -2:1, -389:2, -824:3, -829:4, -899:5, -2(-899+897):6, .........}
so return { 6(end_index of subarray) - 1(starting_index of subarray) }

'''