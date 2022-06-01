"""
  GENERALLY ONLY WORKS ON ARRAYS BECAUSE OF IT'S REANDOM ACCESS

 - Dividing search in halves
 - search a 1,000,000 array in like 22 steps
 - cutting in halves gives 0(log n) -> base 2
 - Efficiency
    -   Time complexity
        - Best-case performance	      O(1)
        - Average performance	      O(log n)
        - Worst-case space complexity O(1)

 Example:
    sorted array = [1,2,3,4,5,7,8,11,15,22]
    target = 11
    search(arr, target) = should return the index of the target value (if it exits) or -1 if it doesnn't
        - get pointers for the first and last values in the array
        - check the number in the middle of L and R
        - check if target is less than or greater than the middle number and move L and R to
            the new region(either left or right)
        - repeat the previous step, until the target is found or region closes
"""

arr =  [1,2,3,4,5,7,8,11,15,22]
# list must be sorted if not
# Big O of sorting algorithm * Big O of binary search

"""  
 - you need a 
 - top
 - middle (top+bottom/2)
 - and bottom variable
 - using arr positions
 
 - keep moving the top and bottom
"""

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((left + right)/2)
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
             right = mid - 1
        else:
            left = mid +1
    return -1

print("index - ", binarySearch(arr, 11))