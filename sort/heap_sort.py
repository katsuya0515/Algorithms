arrays= [43,342,1,231,35,23,52342,3241,4234,54,2342,47,532,2412,531,122]

def show_array(arrays):
	for a in arrays:
		print a,
	print "\n"

def heap_sort(arr):
	l=len(arr)-1

	for i in range(l/2,-1,-1):
		build_heap(arr, i,l)

	for i in range(l , 0, -1):
		if arr[0] > arr[i]:
			temp = arr[0]
			arr[0] = arr[i]
			arr[i] = temp
			build_heap(arr, 0, i - 1)
	return arr


def build_heap(arr,root,bottom):
	while (root*2)<=bottom:
		
		if (root*2)==bottom:
			maxChild=root*2
		elif(arr[(root*2)+1]>arr[root*2]):
			maxChild=root*2+1
		else:
			maxChild=root*2

		if(arr[root]<arr[maxChild]):
			temp=arr[root]
			arr[root]=arr[maxChild]
			arr[maxChild]=temp
			root=maxChild
		else:
			return



show_array(arrays)
sorted=heap_sort(arrays)
show_array(sorted)