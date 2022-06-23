"""
Tags: Arrays
Notes: This uses a bit of math. We use a prefix sum.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        total = sum(nums)
        currTotal = 0
        
        for i, num in enumerate(nums):
            if num + currTotal*2 == total:
                return i
            currTotal += num
        return -1
            
        