"""
Tags: Arrays
Pattern: Two-pointers

Notes: The general idea is to use two pointers to put the ABSOLUTE LARGER NUMBERS at the end of the array.
We focus on ABSOLUTE LARGER NUMBERS because we want to do this in linear time and for an array as such [-10, 0, 5], the smallest number might not be at either of the ends but we are sure that the largest number in the array must be at one of those ends.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        low, high = 0, len(nums)-1
        
        while low<=high:
            if abs(nums[low]) > abs(nums[high]):
                res[high-low] = nums[low] ** 2
                low +=1
            else:
                res[high-low] = nums[high] ** 2
                high -=1
        return res







 