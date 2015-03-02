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

		else: 
			newCell.next=self.head
			self.head=newCell
		

	def pop(self):
		if self.head==None:
			return "Empty"
		else:
			if self.head.next==None:
				temp=self.head
				self.head=None
			else :
				temp=self.head
				self.head=self.head.next
			return temp.value

	def top(self):
		if self.head==None:
			return False
		else:
			return self.head.value

	def isEmpty(self):
		if self.head==None:
			return True
		else:
			return False

def reverse_stack(val):
	stack=Stack()
	length=len(val)
	for i in range(0,length):
		print val[i]
		stack.push(val[i])

	for i in val:
		print stack.pop(),


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

chars="Hello"

reverse_stack(chars)
print stack.push(10)
print stack.push(5)
stack.push(7)
#print stack.top()
#print stack.isEmpty()
print stack.pop()
print stack.pop()
#print stack.isEmpty()

queue=Queue()
#print queue.enqueue(10)
#print queue.enqueue(5)
#print queue.enqueue(7)

#print queue.dequeue()
#print queue.dequeue()






