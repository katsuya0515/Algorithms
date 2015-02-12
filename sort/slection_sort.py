arrays= [43,342,1,231,35,23,52342,3241,4234,54,2342,43,532,2412,531,122]
#arrays= [43,342,1]

def show_array(arrays):
	for a in arrays:
		print a,
	print "\n"

def selection_sort(arr):
	i=0
	l=len(arr)
	for a in range(1,l):
		minNum=arrays[i]
		j=i+1
		for b in range(i+1,l):
			#print "now comparing" + str(minNum) +" and "+str(arr[j])
			if minNum>arr[j]:
				#print "swap occured"
				t=arr[j]
				arr[j]=minNum
				minNum=t
			j=j+1
		arrays[i]=minNum
		i=i+1

	return arr



show_array(arrays)
sorted=selection_sort(arrays)
show_array(sorted)


