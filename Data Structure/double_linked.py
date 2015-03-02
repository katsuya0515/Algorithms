class Cell:
	def __init__(self,val):
		self.data=val
		self.next=None
		self.prev=None


class Double_List:
	def __init__(self):
		self.head=None

	def show(self):
		if self.head==None:
			return False
		else :
			current=self.head
			while current!=None:
				print current.data
				current=current.next


	def appendTop(self,val):
		newNode=Cell(val)
		if self.head == None:
			self.head=newNode
		else:	
			self.head.prev=newNode
			newNode.next=self.head
			self.head=newNode


	def appendLast(self,val):
		newNode=Cell(val)
		if self.head == None:
			self.head=newNode
		else:	
			current=self.head
			while current.next!=None:
				current=current.next
			current.next=newNode
			newNode.prev=current
	
	def delete(self,pos):
		if self.head==None:
			return False
		else: 
			if pos==1:
				self.head=self.head.next
			else:
				current=self.head
				for i in range(0,pos-1):
					current=current.next
				prev=current.prev
				prev.next=current.next
				
d_list=Double_List()

d_list.appendTop(10)
d_list.appendTop(5)
d_list.appendTop(6)
d_list.appendLast(23)

d_list.delete(4)

d_list.show()
