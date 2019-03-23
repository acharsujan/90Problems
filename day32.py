#Code to find largest 3 elements in an array 
import sys
def printthreelargest(arr, arr_size):
	if (arr_size < 3):
		print ("Invalid input")
		return

	third = first = second = -sys.maximize

	for i in range(0, arr_size):
		if (arr[i] > first):
			third = second
			second = first
			first = arr[i]

		elif (arr[i] > second):
			third = second
			second = arr[i]

		elif (arr[i] > third):
			third = arr[i]

	print("Three largest elements are", first, second, third)


#Driver program
arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
printthreelargest(arr,n)