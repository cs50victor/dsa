"""
Tags: Arrays
Pattern: Two-pointer

Notes: We use overwriting and the two-pointer pattern
	- the first pointer is just traversing linearly without interruptions (the i variable ).
	- the second pointer starts outside the bounds of our constraint and is only assigned a valid index, when we find a number that is equal to the target value.
	- the second pointer is subsequently incremented after we encounter a number!=value_we_want_to_remove and we use this new number to overwrite the value at the second pointer
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        currIndex = -1
        for i,num in enumerate(nums):
            if num == val and currIndex == -1:
                currIndex = i
            elif num != val and currIndex != -1:
                nums[currIndex] = nums[i]
                currIndex += 1      
        return currIndex if currIndex!=-1 else len(nums)
            
            
        