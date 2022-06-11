"""
The insertion sort is used when:
- the array is has a small number of elements
- there are only a few elements left to be sorted

an array sorting algorithm

- general idea: - put min
				- swap i with id of minimum number in the subarray


Run-Time: 
	Best    - O(n) - if array is already sorted
	Average - O(n^2)
	Worst   - O(n^2)

Space - O(1)
"""

# Insertion sort in Python
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
		# Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)