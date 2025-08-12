'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
 The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=1,x
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            if mid*mid>x:
                right=mid-1
            else:
                left=mid+1
        return right
    