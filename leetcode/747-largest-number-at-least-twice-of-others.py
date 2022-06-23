"""
Tags: Arrays

Notes: Very similar to the thrid max number questions but in this question we are told that the max number is unique in the array so we don't need to check/account for duplicates
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        top2  = [[float("-inf"),None]] * 2
        
        for i, num in enumerate(nums):
            if num > top2[0][0]:
                top2[1] = top2[0]
                top2[0] = [num, i]
            elif num > top2[1][0]:
                top2[1] = [num, i]
        
        return top2[0][1] if top2[0][0] >= top2[1][0]*2 else -1