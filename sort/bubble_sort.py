arrays= [43,342,1,231,35,23,52342,3241,4234,54,2342,43,532,2412,531,122]
#arrays= [43,342,1]

def show_array(arrays):
	for a in arrays:
		print a,
	print "\n"

def bubble_sort(arr):
	i=0
	l=len(arr)
	
	for a in range(0,l-1):
		
		j=l-1
		for b in range(i,l-1) :
			#print "now looking at" + str(arr[j])
			if arr[j]<arr[j-1]:
				#print str(arr[j]) + " is swapped with "+ str(arr[j-1]) 
				t=arr[j]
				arr[j]=arr[j-1]
				arr[j-1]=t
			j=j-1
		i=i+1
	return arr



show_array(arrays)
sorted=bubble_sort(arrays)
show_array(sorted)


