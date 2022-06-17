"""
Tags: Arrays
Pattern: Two-pointers

Notes: We're making use of the two-pointer pattern and overwriting (swapping).
	- We use two pointers to swap the even numbers with odd numbers, hence gradually pushing the odd numbers towards the end of the array.
	- The right pointer traverses the array without stopping, when it gets to an odd number, it sets the left pointer to that position. 
	- As the right pointer moves on, if it encounters an even number, we swap the values of the two pointers and increment the left pointer by one.
	- 
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        left = -1
        for right, num in enumerate(nums):
            if left == -1 and num % 2 != 0:
                left = right
            elif left != -1 and num % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
        return nums