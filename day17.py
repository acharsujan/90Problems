input1 = [1,2,3,2,0,65,21,4,2,10]
output = []
search_element = int(input("Enter search element: "))
for i in range(len(input1)):
	if input1[i] == search_element:
		output.append(i)
print(output)