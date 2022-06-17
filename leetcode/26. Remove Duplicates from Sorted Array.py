"""
Tags: Arrays
Pattern: Two-pointer

Notes: We use overwriting and the two-pointer pattern
	- the first pointer is just traversing linearly without interruptions (the i variable ).
	- the second pointer starts outside the bounds of our constraint and is only assigned a valid index, when we find the first  duplicate in the array.
	- the second pointer is subsequently incremented after a non duplicate number is seen and used to overwrite the value at the second pointer
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        currIndex = -101
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and currIndex == -101:
                currIndex = i
            elif nums[i] != nums[i-1] and currIndex != -101:
                nums[currIndex] = nums[i]
                currIndex +=1
        return currIndex if currIndex != -101 else len(nums)
            
        