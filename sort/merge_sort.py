
numbers =[1,2,3,4,5,6,7,8,9,10,23,43,65,75,89,123,344,345,654,687,688,1234,2345,3457,4356,4567]
arrays= [43,342,1,231,35,23,52342,3241,4234,54,2342,43,532,2412,531,122]



def merge_sort(arr):
	n = len(arr)

	if n == 1 :
		return arr

	left =  merge_sort(arr[0:n/2])
	right = merge_sort(arr[n/2:n])

	result=[]
	while left != [] and right != []:
		if left[0] < right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))

	result.extend(left)
	result.extend(right)

	return result


	






print arrays
sorted=merge_sort(arrays)
print sorted
