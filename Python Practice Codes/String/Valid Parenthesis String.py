'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1, stack2 = [], []
        for i in range(len(s)):
            if s[i] == "(": 
                stack1.append(i) 
            elif s[i] == "*": 
                stack2.append(i)
            else:
                if not stack1 and not stack2: 
                    return False
                if stack1: 
                    stack1.pop()
                elif stack2: 
                    stack2.pop()
        (***)
        while stack1 and stack2:
            if stack1.pop() > stack2.pop(): 
                return False
        return not stack1


'''
(***)
at the end, s1 may have (   and s2 may have *

so now the * can onlyyy behave as right para or empty string 
And
if the * has to behave as right para, it should have appeared after the left para in string hence its index should be more then left para index 
So at any point, the index popped from s1 is more, we return false
'''
        
        