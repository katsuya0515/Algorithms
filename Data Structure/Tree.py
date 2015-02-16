
class Node:
	def __init__(self,val):
		self.value=val
		self.leftChild=None
		self.rightChild=None

	def insert(self,val):

		if val<self.value:

			if self.leftChild==None:
				self.leftChild=Node(val)
			else:
				self.leftChild.insert(val)

		else:

			if self.rightChild==None:
				self.rightChild=Node(val)
			else:
				self.rightChild.insert(val)

	def preorder(self):

		print self.value
		if self.leftChild!=None:
			self.leftChild.preorder()
		if self.rightChild!=None:
			self.rightChild.preorder()


	def inorder(self):
		if self.leftChild!=None:
			self.leftChild.inorder()
		print self.value
		if self.rightChild!=None:
			self.rightChild.inorder()
		


	def postorder(self):
		if self.leftChild!=None:
			self.leftChild.postorder()
		if self.rightChild!=None:
			self.rightChild.postorder()
		print self.value
	
	def breadth_first(self):
			queue=Queue()

			queue.put(self)

			while queue.empty() != True:
				temp=queue.get()
				print temp.value
				if temp.leftChild:
					queue.put(temp.leftChild)
				if temp.rightChild:
					queue.put(temp.rightChild)

	def findHeight(self):

		if self.leftChild == None and self.rightChild == None:
			return 0
		elif self.leftChild and self.rightChild:
			return max(self.leftChild.findHeight(),self.rightChild.findHeight())+1
		elif self.leftChild:
			return self.leftChild.findHeight() +1
		elif self.rightChild:
			return self.rightChild.findHeight() +1

			

class Tree:
	def __init__(self):
		self.root=None

	def insert(self,val):
	
		if self.root==None:
			newNode= Node(val)
			self.root=newNode
			return True
		else:
			self.root.insert(val)

	def preorder(self):
		if self.root==None:
			return False
		else:
			self.root.preorder()

	def inorder(self):
		if self.root==None:
			return False
		else:
			self.root.inorder()

	def postorder(self):
		if self.root==None:
			return False
		else:
			self.root.postorder()

	def breadth_first(self):
		if self.root==None:
			return False
		else:
			self.root.breadth_first()

	def findHeight(self):
		if self.root==None:
			return False
		else:
			return self.root.findHeight()

				

class Cell: 

	def __init__ (self,val):
		self.value=val
		self.next = None


class Queue:
	def __init__ (self):
		self.head=None

	def put(self,val):
		newCell=Cell(val)

		if self.head == None:
			self.head=newCell
			return True
		else: 
			newCell.next=self.head
			self.head=newCell
			return True

	def get(self):
		if self.head==None:
			return False
		else:

			if self.head.next==None:
				temp=self.head.value
				self.head=None
				return temp
			else:
				prev=self.head
				current=self.head.next
				while current.next!=None:
					#print current.value
					prev=current
					current=current.next

				prev.next=None
				return current.value


	def empty(self):
		if self.head == None:
			return True
		else:
			return False





#create Tree
bst=Tree()
bst.insert(10)
bst.insert(5)
bst.insert(7)
bst.insert(15)
bst.insert(16)
bst.insert(17)
bst.insert(18)
bst.insert(2)
bst.insert(1)

#traverse 
#bst.preorder()
#print " "
#bst.inorder()
#print " "
#bst.postorder()
#bst.breadth_first()

print bst.findHeight()



