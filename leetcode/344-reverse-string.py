"""
Tags: Arrays
Pattern: Two-pointer

*  two-pointer technique is commonly used in a sorted array

Notes: Just using two pointers at the extreme ends of the array, swaping both values, then moving the pointer closer.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0, len(s)-1
        
        while l<r:
            s[l],s[r] = s[r], s[l]
            l+=1
            r-=1