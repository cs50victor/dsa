"""
Tags: Arrays

Notes: Traversal from the left + overwriting
     - Keep an open mind when it comes to traversal of arrays
	- we have the length and access to any index, we can move from anywhere
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxRight = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i],maxRight = maxRight, max(maxRight, arr[i])
        return arr