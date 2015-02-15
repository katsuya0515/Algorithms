class Cell: 

	def __init__ (self,val):
		self.value=val
		self.next = None
class Stack:
	def __init__ (self):
		self.head=None

	def push (self,val):

		newCell=Cell(val)

		if self.head == None:
			self.head=newCell
			return True
		else: 
			newCell.next=self.head.next
			self.head=newCell
			return True

	def pop(self):
		if self.head==None:
			return False
		else:
			temp=self.head
			self.head=self.head.next
			return temp.value



class Queue:
	def __init__ (self):
		self.head=None
		self.next=None


	def enqueue(self,val):
		newCell=Cell(val)

		if self.next == None:
			self.next=newCell
			return True
		else: 
			newCell.next=self.next
			self.next=newCell
			return True

	def dequeue(self):
		if self.next==None:
			return False
		else:
			current=self.head
			next=self.next
			while next.next!=None:
				current=next
				next=next.next

			current.next=None
			return next.value



stack= Stack()

#print stack.push(10)
#print stack.push(5)
#print stack.push(7)
#print stack.pop()

queue=Queue()
print queue.enqueue(10)
print queue.enqueue(5)
print queue.enqueue(7)

print queue.dequeue()
print queue.dequeue()





