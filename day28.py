#program to find first repeating element in array
def printfirstrepeating(arr,n):
	min = -1
	myset = dict()
	for i in range(n-1,-1,-1):
		if arr[i] in myset.keys():
			min = i
		else:
			myset[arr[i]] = 1
		#Print the result
		if (min != -1):
			print("The firstrepeating element is", arr[min])
		else:
			print("There are no repeating elements")


#driver code
arr = [10, 5, 3, 4, 3, 5, 6]
n = len(arr)
printfirstrepeating(arr,n)