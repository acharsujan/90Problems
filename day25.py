#find a pair with the given difference
def findpair(arr,n):
	size = len(arr)
	#Initialize positions of two elements
	i,j = 0,1
	#search for a pair
	while i < size and j < size:
		if i != j and arr[j] - arr[i] == n:
			print ("pair found (",arr[i],",",arr[j],")")
			return True
		elif arr[j] - arr[i] < n:
			j+=1
		else:
			i+=1
	print ("No pair found")
	return False

#Driver function
arr = [1, 8, 30, 40, 100]
n = 60
findpair(arr,n)