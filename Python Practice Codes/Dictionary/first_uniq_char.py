'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in range(len(s)):
#             if s[i] not in s[:i] and s[i] not in s[i+1:]:
#                 return i
#         return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        
        for i, c in enumerate(s):
            if hashmap[c] == 1:
                return i
        
        return -1

# Time: O(n)
# Space: O(n)