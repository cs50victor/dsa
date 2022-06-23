"""
Tags: Arrays
Pattern: Two-pointers

Notes: We're making use of the two-pointer pattern and overwriting (swapping).
	- We use two pointers to swap the zeros with non-zero numbers, hence gradually pushing the zeros towards the end of the array.
	- The right pointer traverses the array without stopping, when it gets to an value equal to 0, it sets the left pointer to that position. 
	- As the right pointer moves on, if it encoounters a number not equal to zero, we swap the values of the two pointers and increment the left pointer by one.
	- 
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        negInf = float("-inf")
        left = negInf
        for right, num in enumerate(nums):
            if left == negInf and num == 0:
                left = right
            elif num != 0 and left != negInf:
                nums[right], nums[left] = nums[left], nums[right]
                left +=1
                
                