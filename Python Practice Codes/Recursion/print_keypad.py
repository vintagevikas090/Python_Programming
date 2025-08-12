'''
Problem statement
Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.

Note : The order of strings are not important. Just print different strings in new lines.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= n <= 10^6

Sample Input:
23
Sample Output:
ad
ae
af
bd
be
bf
cd
ce
cf
'''

n = int(input())

def print_keypad(num, outputSoFar):
    key_values = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    if num == 0:
        print(outputSoFar)
        return
    N = num//10
    lastDigit = num % 10
    options = key_values[lastDigit]
    for i in options:
        newOutput = i + outputSoFar
        print_keypad(N, newOutput)

print_keypad(n, '')