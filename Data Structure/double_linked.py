class Cell:
	def __init__(self,val):
		self.data=val
		self.next=None
		self.prev=None


class Double_List(self):
	def __init__(self):
		self.head=None

	def insert(self,val):
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




d_list=Double_List()
d_list.insert(10)
d_list.insert(5)
d_list.insert(6)
