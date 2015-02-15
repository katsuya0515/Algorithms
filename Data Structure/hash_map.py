
class HashTable :
	def __init__(self,size):
		self.size=size
		self.table=[0]*size


	def insert(self,val):
		ascii=0
		for c in list(val):
			ascii+=ord(c)
		key=ascii%self.size
		print str(val) + " is stored in " + str(key)
		self.table[key]=val

	def find(self,val):
		ascii=0
		for c in list(val):
			ascii+=ord(c)
		key=ascii%self.size
		return self.table[key]



hash=HashTable(20)
hash.insert("aaa")
hash.insert("bbb")
hash.insert("ccc")

print hash.find("aaa")
