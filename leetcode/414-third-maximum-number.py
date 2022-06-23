"""
Tags : Arrays

Notes: Uses math(-ish)
	This is an interesting problem. It can seem a bit challenging trying to find an O(n) solution, but it becomes easier when you think/visualise the problem as a race.
	- also think about the arrangement of the if statements
	-  if a num is bigger the the least number, it could still be bigger all  other numbers
	-  if a number if bigger the first/max number, then there are no other numbers in the array bigger than it
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top3 = [float("-inf")] * 3
#         [1,2,2,5,3,5]
        
        for num in nums:
            if num in top3:
                continue
            if num > top3[0]:
                top3[2] = top3[1]
                top3[1] = top3[0]
                top3[0] = num
            elif num > top3[1]:
                top3[2] = top3[1]
                top3[1] = num
            elif num > top3[2]:
                top3[2] = num
        return top3[2] if top3[2] != float("-inf") else top3[0]