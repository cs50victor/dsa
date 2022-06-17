"""
Tags: Arrays

Notes: Uses marking of index values, REALLY important technique for in-place operations (usually hinted by 'could you do it without extra space')
	- we technically can't change the value of the indexed but we can mark the values at that index 
"""

"""
Brute Force: time: O(n), space O(n+k) where k is all numbers disappeared in the array
-----------
allNums = set(range(1, len(nums)+1))
        
for num in nums:
	if num in allNums:
		allNums.remove(num)

return list(allNums)
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        # mark indexes
        missingNums = []
        
        for num in nums:
            index = abs(num) - 1
            if nums[index]>0:
                nums[index] *= -1
            
        for i,num in enumerate(nums):
            if num > 0:
                missingNums.append(i+1)
                
        return missingNums
        