'''Problem statement
Given an integer n, using phone keypad find out and return all the possible strings that can be made using digits of input n.

Note : The order of strings are not important.
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


def keypad(n):
    #Implement Your Code Here
    key_char = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    if n == 0:
        output = []
        output.append('')
        return output
    N = n // 10
    last_digit = n % 10
    smaller_output = keypad(N)
    output = []
    last_value = key_char[last_digit]
    for i in smaller_output:
        for j in last_value:
            option = i + j
            output.append(option)
    return output


n = int(input('Enter the Number: '))
ans = keypad(n)
for s in ans:
    print(s)