def getPerm(data):

	if len(data)==0:
		return 
	elif len(data)==1:
		if data[0]=="0":
			print "0 returned"
			return ["0"]
		else:
			return ["a","b"]
	else:
		perms=getPerm(data[1:len(data)])

	result=[]

	for perm in perms:
		if data[0]=="0":
			result.append("0"+perm)
		else:
			result.append("a"+perm)
			result.append("b"+perm)
	return result


print getPerm("101")