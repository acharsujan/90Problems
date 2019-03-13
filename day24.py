#python program to check fixed point in an array using binary search
def binarysearch(arr,low,high):
	if high >= low:
		mid = (low + high)//2
	if mid is arr[mid]:
		return mid
	if mid > arr[mid]:
		return binarysearch(arr,(mid + 1),high)
	else:
		return binarysearch(arr,low, (mid - 1))
	return -1


#driver program
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed point is " + str(binarysearch(arr, 0,n-1)))