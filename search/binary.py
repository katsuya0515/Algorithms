#-*- coding: utf-8 -*-
print "Welcome to Binary Search"

#26
numbers =[1,2,3,4,5,6,7,8,9,10,23,43,65,75,89,123,344,345,654,687,688,1234,2345,3457,4356,4567]



def Search(findNum):
	print type(findNum)
	first=0
	last=len(numbers)-1
	print "looking for" + str(findNum)
	while first<=last:
		mid=(first+last)/2
		print "searching between" + str(numbers[first]) +" and "+ str(numbers[last])
		print "looking at" + str(numbers[mid])
		if findNum == numbers[mid]:
			return mid
		if findNum > numbers[mid]:
			print str(findNum) +" is bigger than" + str(numbers[mid])
			first=mid+1
		elif findNum < numbers[mid]:
			print str(findNum)+" is smaller than" + str(numbers[mid])
			last=mid-1
		

	return -1


#main 
print "Which number do you want to find?"
num=raw_input()
n=Search(int(num))# avoid sending 'str' type 
if num != None:
	print "Found " + str(num) + " at index of "+ str(n)





