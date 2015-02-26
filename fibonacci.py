
def Fib_recursive(n):

	if n < 2 :
		return n
	else:
		return Fib_recursive(n-2) + Fib_recursive(n-1)
		

def Fib_recursive2(n):
	
	if n<2:
		return 
	else:
		result=[]
		result.append(Fib_recursive(n-2) + Fib_recursive(n-1))
	return result



def Fib(n):
	number=1
	last=0
	before_last=0

	print number-1
	print number

	for i in range(0,n-3):
		before_last=last
		last=number
		number=last+before_last
		print number



result=[]

#Fib(10)

##	print Fib_recursive(i)

print Fib_recursive2(10)