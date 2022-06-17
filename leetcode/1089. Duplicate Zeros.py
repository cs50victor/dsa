"""
Tags: Arrays, Math

Notes: In-place operations hint 'avoid using additional space or O(1) space
	- The number of zeros is the max number of duplications+shift operations we can make in the array.
	- Using the number of zeros we have left, we know what indexes should be shifted to simulate the end result of shifting the array to the right z number of times, where z is the number of zeros.
	- i+numOfZeros < arrLen , indicates where we should start shifting from
	- when solving array problems, list of the hints and tools given to you by the question.
"""


# Brute-Force O(n^2)
"""
i, end = 0 , len(arr)-1
while i < end-1:
	if arr[i]==0:
		arr.pop()
		arr.insert(i+1,0)
		i+=1
	i+=1
"""

# Using math O(n)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        numOfZeros = arr.count(0)
        arrLen = len(arr)
        # traversal from the front will overwrite unshifted numbers
        for i in range(arrLen-1, -1, -1):
            # duplicate to shifted position
            if(i+numOfZeros < arrLen):
                arr[i+numOfZeros] = arr[i]
            # reduce the number of zeros and duplicate to shifted position (which will be the next position)
            if arr[i] == 0:
                numOfZeros -=1
                if(i+numOfZeros < arrLen):
                    arr[i+numOfZeros] = 0
                
                