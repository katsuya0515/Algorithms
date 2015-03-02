class Cell:
	def __init__(self,val):
		self.data=val
		self.next=None

	def show_recursive(self):
			print self.data
			if self.next!=None:
				self.next.show_recursive()

	def show_recursive_reverse(self):
		if self.next!=None:
			self.next.show_recursive_reverse()
		print self.data
			
	
class List:
	def __init__(self):
		self.header=None

	def show(self):
		if self.header==None:
			return False
		else:
			current=self.header
			while True:
				print current.data
				if current.next==None:
					break
				else:
					current=current.next

	def get_length(self):

		if self.header==None:
			print 0
		else:
			current=self.header
			count=0;
			while True:
				count=count+1
				if current.next==None:
					break
				else:
					current=current.next
			return count


	def appendTop(self,val):
		newCell=Cell(val)

		if self.header==None:
			self.header=newCell
		else:	
			newCell.next=self.header
			self.header=newCell
			
	def apeendLast(self,val):
		newCell=Cell(val)

		if self.header==None:
			self.header=newCell
		else:
			current=self.header
			while current.next!=None:
				current=current.next
			current.next=newCell

	def insert(self,pos,val):
		if pos>self.get_length():
			print "Error"
			return False

		newCell=Cell(val)

		if pos == 1: 
			newCell.next=self.header
			self.header=newCell

		else:	
			current=self.header
			prev=None

			for i in range(0,pos-1):
					prev=current
					current=current.next
			prev.next=newCell
			newCell.next=current


	def delete(self,pos):
		if self.get_length()<pos:
			print "Error"
			return False
		
		if pos == 1:
			self.header=self.header.next
		else:
			current=self.header
			prev=None
			for i in range(0,pos-1):
				prev=current
				current=current.next
			prev.next=current.next

	def reverse(self):
		if self.header==None:
			return False
		elif self.get_length==1:
			return False
		else:
			current=self.header
			prev=None
			while current!=None:
				next=current.next
				current.next=prev
				prev=current
				current=next
			#current.next=prev
			self.header=prev

	def show_recursive(self):
		if self.header==None:
			return False
		else:
			self.header.show_recursive()


	def show_recursive_reverse(self):
		if self.header==None:
			return False
		else:
			self.header.show_recursive_reverse()
			

myList=List()
#myList.apeendLast(30)
myList.appendTop(20)
myList.appendTop(10)
#myList.delete(2)

myList.insert(1,32)
myList.insert(2,42)
myList.insert(2,52)
myList.insert(4,62)
#myList.get_length()

myList.delete(1)
myList.delete(5)

myList.show()

#myList.show_recursive_reverse()
#myList.show()