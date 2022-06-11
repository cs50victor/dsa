"""
an array sorting algorithm

- general idea: - put min at the start 
				- swap i with id of minimum number in the subarray


Run-Time: O(n^2)
	      (n-1) + (n-2) + (n-3) +.....+ 1 = n(n-1)/2 | approx. n^2

Space - O(1)
"""

# Selection sort in Python


def selectionSort(array):
	
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array)):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[j] < array[minIdx]:
                minIdx = j
        # put min at the correct position
		if(minIdx != i):
        	array[i], array[minIdx] = array[minIdx], array[i]

data = [-2, 45, 0, 11, -9]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

