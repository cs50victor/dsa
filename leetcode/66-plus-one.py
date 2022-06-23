"""
Tags: Arrays

Notes: This looks easy. It is, but it also has a trick	
	- We only have a problem if the last or first digit is a 9
	- If the first digit is a 9, we have 10^n value
	- if the current digit is a 9, the for loop continues (the concept of carrying a 1 to the next digit)
	- We also have to add 1 to digits in the array, in reverse
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

		for i, digit in range(len(digits)-1, -1, -1):
			if digit != 9:
				digits[i] += 1
				return digits
			digits[i] = 0
		return [1] + digits