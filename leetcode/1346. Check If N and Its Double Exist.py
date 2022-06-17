"""
Tags: Array

Notes: linear search with a hashmap
"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
                
        seenNums = set()
        for num in arr:
            N, M = num * 2, num/2
            if N in seenNums or M in seenNums:
                return True
            seenNums.add(num)
        return False
        