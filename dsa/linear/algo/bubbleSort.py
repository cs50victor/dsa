"""
an array sorting algorithm

- general idea : push bigger/smaller number towards the end of the array
				- swap i <--> i+1


Run-Time: 
	Best    - O(n) - if array is already sorted
	Average - O(n^2)
	Worst   - O(n^2)
	(n-1) + (n-2) + (n-3) +.....+ 1 = n(n-1)/2 | approx. n^2
Space - O(1)
"""

# Optimized Bubble sort 
def bubbleSort(arr):
  # loop through each element of array
  for i in range(len(arr)):
    # keep track of swapping
    swapped = False
    # loop to compare array elements
    for j in range(0, len(arr) - i - 1):
      # compare two adjacent elements
      # change > to < to sort in descending order
      if arr[j] > arr[j + 1]:
        # swapping occurs if elements
        # are not in the intended order
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break

data = [-2, 45, 0, 11, -9] * 2
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)