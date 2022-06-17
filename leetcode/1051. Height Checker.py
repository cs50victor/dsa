"""
Tags: Arrays, Sorting

Notes: this question is easily solved by implementing a sorting algorithm like bucket or count sort.
	- an  optimal solution to this questions uses a hashtable

"""

"""
Brute force: Time: O(nlogn), space: O(n), where n = len(heights), space includes the returning array h.
	expected = sorted(heights)
	mismatches = 0
	
	for i, num in enumerate(heights):
		if num != expected[i]:
			mismatches+=1
	return mismatches
"""
from collections import defaultdict

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        heightCount = defaultdict(int)

		# get all heights and their occurence
        for height in heights:
            heightCount[height] +=1
        
        # minH is the minimum height in a sorted array of heights
		mismatches, minH = 0,1
        
        for height in heights:
			# we start from the minimum possible number in an array
			# but a sorted height array might start from a different number
			# we get to that number using our hashtable, since we have all the
			# height occurences.
			# subsequently, we skip to the next minimum possible height 
			# in the height array. if the currheight != minHeight. 
			# we have a mismatch
            while heightCount[minH] == 0:
                minH +=1
            if minH != height:
                mismatches+=1
            heightCount[minH] -= 1  # remove the height that has been seen from the hashtable - (keeps track of duplicates).
        return mismatches