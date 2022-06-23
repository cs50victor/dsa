"""
Tags: Binary Search (Template 1 / Classic version)

Notes: 
	why is l = 0 and r = x ?
	--------------
	- the given constraint is 0 <= x <= 2^31 - 1, and we want to cover all edge cases
	- starting from 0 also allows us to cover the possibility that squareroot = (x-0)/2 (i.e 4)
	-  covers the case where x^2 = x like x = i
	
	why is the while loop's condition l<=r?
	---------------------------------------
	- the target could be either l==target, or r==target 
	  and one pointer could continuously move toward the other
		- l+l/2 -> l, r+r/2 -> 2
	- this is also needed as we need to cross the pointers to get the upper and lower bound of the square root
	- when we get to the condition l<=r
		- the last calculation we make is the lower bound calculation (r=mid-1).
	- we return r, because it might eventually cross the l pointer and become the lowerbound
"""
class Solution:
    def mySqrt(self, x: int) -> int:        

        l = 0
        r = x
        while l <= r:
			if l**2 == x:
				return l
			if r**2 == x:
				return r
				
            mid = (l+r)//2
			square = mid**2
            if square == x:
                return mid
            if square < x:
                l = mid+1
            else:
                r = mid -1
        return r
        