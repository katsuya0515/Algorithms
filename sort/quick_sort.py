arrays= [43,342,1,231,35,23,52342,3241,4234,54,2342,47,532,2412,531,122]
#arrays= [43,342,1]

def show_array(arrays):
	for a in arrays:
		print a,
	print "\n"

def partition(arr,l,r):
	pivot=arr[r]
	print "current pivot is " + str(pivot)
	i=l
	j=r-1
	while True:
		while arr[i]<=pivot:
			i=i+1
		while arr[j]>=pivot:
			j=j-1
		if(i>=j):
			break
		print "swapping "+ str(arr[i]) +" and " +str(arr[j])
		temp=arr[i]
		arr[i]=arr[j]
		arr[j]=temp

	temp=arr[i]
	arr[i]=arr[r]
	arr[r]=temp



	return i




def quick_sort(arr,l,r):
	if(l>=r):
		return
	v=partition(arr,l,r)
	show_array(arr)
	print "now looking at " + str(l)
	quick_sort(arr,l,v-1)
	quick_sort(arr,v+1,r)
	return arr


	



show_array(arrays)
sorted=quick_sort(arrays,0, len(arrays)-1)
show_array(sorted)


