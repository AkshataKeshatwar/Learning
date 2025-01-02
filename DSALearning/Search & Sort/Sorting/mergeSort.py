# Python program for implementation of MergeSort


def mergeSort(arr):
	print("Array before processing", arr)
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# Into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		print("before for:",arr, L, R, i, j)
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			print("...........",arr)
			k += 1

		print("1st for:",arr)
		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		print("2nd for:",arr)
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
		print("Array After Processing",arr)


# Code to print the list
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


arr = [15, 8, 13, 5, 6, 21, 3]
print("Given array is")
printList(arr)
mergeSort(arr)
print("\nSorted array is ")
printList(arr)

# This code is contributed by Mayank Khanna
