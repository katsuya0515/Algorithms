print "Welcome to Linear Search"

numbers =[]


def makeArray():
	print "Please input numbers (input c to finish)"

	while 1:
		x=raw_input()
		if x == 'c' :
			break;
		if x.isdigit()== True:
			numbers.append(x)
		else :
			print "This is not number"

	#for n in numbers :
		#print n

def Search(findNum):
	count=0
	for n in numbers:
		if findNum==n:
			return count
		count=count+1
			
#main 
makeArray()

print "Which number do you want to find?"
num=raw_input()
n=Search(num)
if num != None:
	print "Found " + str(num) + " at index of "+ str(n)




