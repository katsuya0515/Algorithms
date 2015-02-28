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

                 
    def getDepth(self,val,count):
       # print "now looking at " +str(self.value) +" trying to find " + str(val) + "at level " + str(count)
        left=0
        right=0
        if self.value == val:
           # print "found at " + str(count) 
            return count
        else:
            if self.leftChild :
                 left=self.leftChild.getDepth(val,count+1)
            if self.rightChild:
                 right=self.rightChild.getDepth(val,count+1)
            return max(left,right)
    
        
       
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



    def level_order_traverse(self):
        if self.root==None:
            return False
        else:
         queue = Queue()
         queue.put(self.root)
         prev=0

         while queue.empty()==False:
            temp=queue.get()
            depth=self.root.getDepth(temp.value,0)
         
            if(depth!=prev): 
                print "\n",
                prev=depth
            #print depth,
            print temp.value,
            if temp.leftChild != None:
                queue.put(temp.leftChild)
            if temp.rightChild !=None:
                 queue.put(temp.rightChild)
                 
   


from Queue import Queue
bst=Tree()
bst.insert(10)
bst.insert(5)
bst.insert(7)
bst.insert(15)
bst.insert(16)
bst.insert(17)
bst.insert(2)


#print bst.isBST()
bst.level_order_traverse()
