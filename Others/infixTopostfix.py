 
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



 

def IsOperand(C):

	if C >= '0' and C <= '9':
		return True;
	if C >= 'a' and C <= 'z':
		return True;
	if C >= 'A' and C <= 'Z':
		return True;
	return False;

 
def IsOperator(C):

	if C == '+' or C == '-' or  C == '*' or  C == '/'  :
		return True;
	
	return False;

def  IsRightAssociative(op):
	if op == '$':
		return True;
	return False;


def GetOperatorWeight(op):

	weight = -1; 
	if op== '+' or op == '-':
		weight = 1;
	if op== '*' or op =='/':
		weight = 2;
	if op == '$':
		weight = 3;
	
	return weight;

def HasHigherPrecedence(op1, op2) :
	op1Weight = GetOperatorWeight(op1);
	op2Weight = GetOperatorWeight(op2);
	if op1Weight == op2Weight:
		if IsRightAssociative(op1): 
			return False;
		else:
			return True;
	
	if op1Weight > op2Weight:
		return True
	else:
		return False

def InfixToPostfix(expression):
	S=Stack();
	postfix = ""; 

	for i in range(0,len(expression)): 
		if expression[i] == ' ' or expression[i] == ',':
			continue
 
		elif IsOperator(expression[i]):

			while S.isEmpty()==False and S.top() != '(' and HasHigherPrecedence(S.top(),expression[i]):
				postfix+= S.top()
				S.pop()
			
			S.push(expression[i])
		
		
		elif IsOperand(expression[i]):
			postfix =postfix+expression[i]
 
		elif expression[i] == '(' :
			S.push(expression[i])
 
		elif expression[i] == ')':

			while S.isEmpty()==False and S.top() !=  '(' :
				postfix = postfix+S.top()
				S.pop()
			S.pop();
	
	while S.isEmpty()==False :
		postfix = postfix+S.top()
		S.pop()
	
 
	return postfix;

	

print InfixToPostfix("A+B*C-D*E")

