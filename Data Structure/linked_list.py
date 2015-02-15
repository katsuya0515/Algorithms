class Node:
	def __init__(self,val):
		self.value=val
		self.next=None
	
class Linked_list:
	def __init__(self):
		self.head=None

	def append(self,val):
		newNode=Node(val)

		if self.head==None:
			self.head=Node(val)
			return True
		else:
			newNode.next=self.head
			self.head=newNode
			return True
	
	def delete(self,val):
		if self.head == None:
			return False

		if self.head.value == val:
			self.head=self.head.next
		else:
			prev=self.head
			current=self.head.next
			print str(current.value)
			while  True:
				if current.value==val:
					prev.next=current.next
				prev=current
				current=current.next
				if current ==None:
					break
	def insert(self,i,val):
		if self.head == None:
			return False
		newNode=Node(val)
		current=self.head
		while True:
			if current.value == i:
				newNode.next=current.next
				current.next=newNode
				return True
			current=current.next
			if current ==None :
				break
		return False


	def showAllNodes(self):
		if self.head:
			current=self.head
			while True:
				print current.value
				current=current.next
				if current ==None :
					break



array=Linked_list()
array.append(10)
array.append(5)
array.append(12)
array.append(3)
array.append(7)
array.showAllNodes()
array.insert(5,9)
array.showAllNodes()

