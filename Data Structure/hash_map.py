
class HashTable :
	def __init__(self,size):
		self.size=size
		self.table=[0]*size


	def insert(self,val):
		ascii=0
		for c in list(val):
			ascii+=ord(c)
		key=ascii%self.size
		
		while self.table[key]!=0:
			print	"Collision Occured"
			key+=1
			key%=self.size

		#print str(val) + " is stored in " + str(key)
		self.table[key]=val

	def find(self,val):
		ascii=0
		for c in list(val):
			ascii+=ord(c)
		key=ascii%self.size
		print str(key)
		count=0
		while  True:
			if self.table[key]== val:
				return self.table[key]
			key+=1
			key%=self.size	
			count+=1
			if count>self.size:
				break	
		return False
		



hash=HashTable(20)
hash.insert("aaa")
hash.insert("aaa")
hash.insert("bbb")
hash.insert("ccc")

print str(hash.find("ddd"))
