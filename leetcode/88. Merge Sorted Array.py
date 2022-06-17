"""
Tags: Arrays
Pattern: Two-pointers

Notes: We're making use of the two-pointer pattern and overwriting.
	- Overwriting is a huge strategy used with array and sorting-like/merge questions.
	- like in a lot of other questions focused on merging multiple sorted arrays, we focus on the biggest number in these arrays and place them at the end of our final array.
	- We use two pointers to get the larget number between the two arrays and overwrite the last index (first pointer) of the nums1 array with that value. We push the biggest number of both arrays to the end of nums1 by overwriting the value at the first pointer (cursor), then decrementing the pointer.
	- We keep overwriting and decrementing the first pointer until the second pointer (j), get to 0.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, cursor = m-1, n-1, m+n-1
        
        while j >= 0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[cursor] = nums1[i]
                i-=1
            else:
                nums1[cursor] = nums2[j]
                j-= 1
            cursor -=1