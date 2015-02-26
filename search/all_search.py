

numbers =[1,2,3,4,5,6,7,8,9,10,23,43,65,75,89,123,344,345,654,687,688,1234,2345,3457,4356,4567]
arrays= [43,342,1,231,35,23,52342,3241,4234,54,2342,43,532,2412,531,122]


def binary_search(num):
	first=0
	last=len(numbers)-1

	while first<=last:
		min=(first+last)/2
		if num == numbers[min]:
			return min
		elif num > numbers[min]:
			first=min+1
		elif num<numbers[min]:
			last=min-1
	return False


def quick_sort(arr,l,r):
	if(l>=r):
		return
	v=parition(arr,l,r)
	quick_sort(arr,l,v-1`	quick_sort(arr,v+1,r)
	
	return arr


def parition(arr,l,r):
	pivot=arr[r]
	pivotIndex=r
	r=pivotIndex-1
	
	while True:
		while arr[l]<pivot:
			l+=1
		while arr[r]>pivot:
			r-=1
		if l >= r:
			break
		temp=arr[l]
		arr[l]=arr[r]
		arr[r]=temp

	temp=arr[l]
	arr[l]=arr[pivotIndex]
	arr[pivotIndex]=temp

	return l

def bubble_sort(arr):
	for i in range(0,len(arr)-1,+1):
		for j in range(len(arr)-1,i,-1):
			if arr[j-1]>arr[j]:
				temp=arr[j]
				arr[j]=arr[j-1]
				arr[j-1]=temp
	return arr



class Node:
	def __init__(self,val):
		self.data=val
		self.leftChild=None
		self.righChild=None

	def insert(self,val):
		if val>self.data:
			if self.righChild==None:
				self.righChild=Node(val)
				return True
			else:
				return self.righChild.insert(val)

		elif val<self.data:
			if self.leftChild==None:
				self.leftChild=Node(val)
				return True
			else:
				return self.leftChild.insert(val)

	def search(self,val):
		if self.data==val:
			return True
		else:
			if val>self.data:
				if self.righChild:
					return self.righChild.search(val)
				else:
					return False
			elif val<self.data:
				if self.leftChild:
					return self.leftChild.search(val)
				else:
					return False





class Tree:
	def __init__(self):
		self.root=None

	def insert(self,val):
		if self.root==None:
			self.root=Node(10)
			return True
		else:
			return self.root.insert(val)

	def search(self,val):
		if self.root==None:
			return False
		else:
			return self.root.search(val)




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


#bst=Tree()
#print bst.insert(10)
#print bst.insert(5)
#print bst.insert(8)
#print bst.insert(6)
#print bst.search(2)


#print arrays
#sorted=quick_sort(arrays,0,len(arrays)-1)
#sorted=bubble_sort(arrays)
#print sorted

#main 
#print "Which number do you want to find?"
#num=raw_input()
##n=binary_search(int(num))
#if num != None:
#	print "Found " + str(num) + " at index of "+ str(n)
