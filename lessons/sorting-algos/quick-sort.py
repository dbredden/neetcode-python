#Implementation of QuickSort
def quickSort(arr: list[int], s: int, e: int) -> list[int]:
	if e - s + 1 <= 1:
		return arr
		
	pivot = arr[e] # setting the pivot to the last element
	left = s # left side pointer
	
	# partition elements small than pivot on the left side
	for i in range(s, e):
		if arr[i] < pivot:
			tmp = arr[left]
			arr[left] = arr[i]
			arr[i] = tmp
			left += 1
	
	# move pivot in between left and right sides
	arr[e] = arr[left]
	arr[left] = pivot
	
	# quick sort left side
	quickSort(arr, s, left - 1)
	
	# quick sort right side
	quickSort(arr, left + 1, e)
	
	return arr