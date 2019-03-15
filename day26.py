# Kth closest element to a given value
#Function to find the crossover point
def findcrossover(arr,low,high,x):
	if (arr[high] <= x):
		return high
	if (arr[low] > x):
		return low
	mid = (low + high) // 2
	
 	if (arr[mid] <= x and arr[mid+1] > x):
 		return mid
 	if (arr[mid] < x):
 		return findcrossover(arr, mid+1,high ,x)
 	return findcrossover(arr, low, mid-1, x)

 #This fuction prints k closest elements to x in arr[] , n is the number of elements in arr[]
 def printkclosest(arr,x,k,n):
 	l = crossover(arr, 0, n-1, x)
 	r = l+1
 	count = 0

 	if (arr[l] == x):
 		l -= 1

 	while (l >= 0 and r < n and count < k):
 		if (x - arr[l] < arr[r] - x):
 			print (arr[l], end = " ")
 			l -= 1
 		else:
 			print (arr[r], end = " ")
 			r += 1
 			count +=1

 	while (count < k and l >= 0):
 		print (arr[l], end = " ")
 		l -= 1
 		count += 1

 	while (count < k and r < n):
 		print (arr[r], end = " ")
 		r += 1
 		count += 1


#Driver code
if __name__ == "__main__":
	arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
	n = len(arr)
	x = 35
	k = 4
	printkclosest(arr, x, 4, n)

 	




