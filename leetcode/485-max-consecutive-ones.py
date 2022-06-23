"""
Tags: Arrays

Notes: Pretty-straightforward 

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxCount = 0
        counter = 0
        for num in  nums:
            if num == 1:
                counter +=1
                maxCount = max(maxCount, counter)
            else:
                counter = 0
        return maxCount