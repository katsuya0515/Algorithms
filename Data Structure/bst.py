class Node :
	def __init__(self,val):
		self.value=val
		self.leftChild=None
		self.rightChild=None

	def insert(self,data):
		if data == self.value:
			return False

		elif data<self.value:
			#print "Node is insert to leftChild"
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild=Node(data)
				return True
		elif data>self.value:
			#print "Node is insert to rightChild"
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild=Node(data)
				return True


	def search(self,data):
		if (self.value==data):
			return True
		if data<self.value:
			if self.leftChild:
				return self.leftChild.search(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.search(data)
			else:
				return False

	def preorder(self):
		if self:
			print str(self.value)

			if self.rightChild:
				#print "Go to rightChild"
				self.rightChild.preorder()

			if self.leftChild:
				#print "Go to leftChild"
				self.leftChild.preorder()
		

class Tree:
	def __init__(self):
		self.root=None

	def insert(self,data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root=Node(data)
			return True

	def search(self,data):
		if self.root:
			return self.root.search(data)
		else:
			return False

	def preorder(self):
		print "preorder: "
		self.root.preorder();


bst=Tree()
print bst.insert(10)
print bst.insert(15)
print bst.insert(6)
print bst.insert(20)

bst.preorder()
#print bst.search(15)