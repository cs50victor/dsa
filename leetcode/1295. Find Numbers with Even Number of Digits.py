"""
Tags: Arrays, Math

Note: Knowledge of logrithms if really useful
"""

from math import log10

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        noOfEvenNums = 0        
        for num in nums:
            if num == 0:
                continue
            if int(log10(num)) % 2 !=0:
                noOfEvenNums +=1
        return noOfEvenNums
        