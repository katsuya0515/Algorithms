class Node:
	def __init__(self,val):
		self.data=val
		self.leftChild=None
		self.rightChild=None

	def insert(self,val):

		if val <self.data:
			if self.leftChild:
				self.leftChild.insert(val)
			else:
				self.leftChild=Node(val)
		elif val >= self.data:
			if self.rightChild:
				self.rightChild.insert(val)
			else:
				self.rightChild=Node(val)

	def search(self,val):
		if self.data==val:
			return True
		else:
			if val <self.data:
				if self.leftChild:
					return self.leftChild.search(val)
				else:
					return False
			elif val >= self.data:
				if self.rightChild:
					return self.rightChild.search(val)
				else:
					return False

	def preorder(self):
		print self.data,
		if self.leftChild:
			self.leftChild.preorder()
		if self.rightChild:
			self.rightChild.preorder()

	def inorder(self):
	
		if self.leftChild:
			self.leftChild.inorder()

		print self.data,

		if self.rightChild:
			self.rightChild.inorder()
		
	def postorder(self):
	
		if self.leftChild:
			self.leftChild.postorder()
		if self.rightChild:
			self.rightChild.postorder()
		print self.data,


	def breadth_traverse(self):
		queue=Queue()
		queue.put(self)
		while queue.empty()==False:
			temp=queue.get()
			print temp.data,
			if temp.leftChild:
				queue.put(temp.leftChild)
			if temp.rightChild:
				queue.put(temp.rightChild)

	def findMin(self):
		if self.leftChild==None:
			return self.data
		else:
			return self.leftChild.findMin()

	def getHeight(self,count):
		if self.leftChild == None and self.rightChild == None:
			return count
		elif self.leftChild and self.rightChild:
			return max(self.leftChild.getHeight(count+1),self.rightChild.getHeight(count+1))
		elif self.leftChild:
			return self.leftChild.getHeight(count+1)
		elif self.rightChild:
			return self.rightChild.getHeight(count+1)

	def getDepth(self,val,count):
		if self.data==val:
			return count
		else:
			if val<self.data:
				if self.leftChild:
					return self.leftChild.getDepth(val,count+1)
			else:
				if self.rightChild:
					return self.rightChild.getDepth(val,count+1)

	

	def check_bst(self,minVal,maxVal):
		if self.leftChild==None and self.rightChild==None:
			if self.data>minVal and self.data<maxVal:
				return True
			else:
				return False
		else:
			if self.leftChild and self.rightChild:
			 	left=self.leftChild.check_bst(minVal,self.data)
			 	right=self.rightChild.check_bst(self.data,maxVal)
			 	if left and right:
			 		return True
			 	else:
			 		return False
			elif self.leftChild:
				return self.leftChild.check_bst(minVal,self.data)
			elif self.rightChild:
				return self.rightChild.check_bst(self.data,maxVal)

			 


class BST:
	def __init__(self):
		self.root=None

	def insert(self,val):
		if self.root==None:
			self.root=Node(val)
		else:
			self.root.insert(val)

	def search(self,val):
		if self.root==None:
			return False
		else:
			return self.root.search(val)

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

	def findMin(self):
		if self.root==None:
			return False
		else:
			print self.root.findMin()

	def getHeight(self):
		if self.root==None:
			return False
		else:
			print self.root.getHeight(1)

	def getDepth(self,val):
		if self.root==None:
			return False
		else:
			print self.root.getDepth(val,1)

	def breadth_traverse(self):
		if self.root==None:
			return False
		else:
			self.root.breadth_traverse()

	def check_bst(self):
		if self.root==None:
			return False
		else:
			print self.root.check_bst(-100,100)





from Queue import Queue

bst=BST()
bst.insert(10)
bst.insert(5)
bst.insert(7)
bst.insert(15)
bst.insert(16)
bst.insert(17)
bst.insert(18)
bst.insert(2)
bst.insert(1)



#bst.getHeight()
#bst.getDepth(18)
bst.preorder()
print ""
bst.inorder()
print ""
bst.postorder()
#bst.breadth_traverse()
#bst.check_bst()
