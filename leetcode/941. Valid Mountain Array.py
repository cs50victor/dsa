"""
Tags: Array

Notes: careful understanding of the question
	 - decreasing should only be true if all other stages have been 
	- think through all the stages of the question/problem
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        increasing , decreasing  = False, False
        
        for i in range(len(arr)-1):
            if not increasing and not decreasing:
                if arr[i] < arr[i+1]:
                    increasing = True
                else:
                    return False
            elif increasing:
                if arr[i] == arr[i+1]:
                    return False
                if arr[i] > arr[i+1]:
                    decreasing = True
                    increasing = False
            elif decreasing and arr[i] <= arr[i+1]:
                return False
        return decreasing