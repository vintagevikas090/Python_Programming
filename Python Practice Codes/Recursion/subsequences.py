'''Problem statement
Given a string (let's say of length n), return all the subsequences of the given string.

Subsequences contain all the strings of length varying from 0 to n. 
But the order of characters should remain the same as in the input string.
 Note: The order of subsequences are not important.'''

'''
Sample Input:
abc
Sample Output:
"" (the double quotes just signifies an empty string, don't worry about the quotes)
c 
b 
bc 
a 
ac 
ab 
abc 
'''

import copy
def subsequences(string, li = ['']):
    #Implement Your Code Here
    if len(string) == 0:
        return li
    if len(string)==1:
        li.append(string[0])
        return li
    smallerOutput = subsequences(string[1:], li)
    output_len = len(smallerOutput)*2
    output = copy.copy(smallerOutput)
    for i in smallerOutput:
        char = string[0]+i
        output.append(char)
    return output

string = input('Enter a string:\n')
ans = subsequences(string)
for ele in ans:
    print(ele)
