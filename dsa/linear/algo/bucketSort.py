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