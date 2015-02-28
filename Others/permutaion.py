def getPerm(word):
	length=len(word)
	if length==1:
		return [word]
	else:
		perms=getPerm(word[1:])
		char=word[0]
		result=[]
		for perm in perms:
			for i in range(len(perm)+1):
				result.append(perm[:i]+char+perm[i:])
	return result



def generateParents(num):
	if num==1:
		return ["()"]
	else:
		perms=generateParents(num-1)
		result=[]
		for perm in perms:
			for i in range(len(perm)):
				if perm[i]=="(":
					#print perm[:i]+"()"+perm[i:]
					result.append(perm[:i+1]+"()"+perm[i+1:])
			result.append("()"+perm)

	return list(set(result))




print getPerm("abcf")
print generateParents(5)