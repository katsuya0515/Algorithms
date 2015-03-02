adjacent=((1,2),(0,2,3),(0,1,4),(1,4,5),(2,3,6),(3,),(4,))

def search_dst(goal,path):
	n=path[len(path)-1]
	if n==goal:
		print path
	else:
		for x in adjacent[n]:
			if x not in path:
				path.append(x)
				search_dst(goal,path)
				path.pop()

def search_bst(start,goal):
	q=Queue()
	q.put(start)
	while q.empty()==False:
		path=q.get()
		n=path[len(path)-1]
		if n==goal:
			print path
		else:
			for x in adjacent[n]:
				if x not in path:
					new_path = path[:]
					new_path.append(x)
					q.put(new_path)

def id_search(limit,goal,path):
	l=len(path)
	n=path[len(path)-1]
	if l == limit:
		if n==goal:
			print path
	else:
		for x in adjacent[n]:
			if x not in path:
				path.append(x)
				id_search(limit,goal,path)
				path.pop()





from Queue import Queue

#search_dst(6,[0])
#search_bst([0],6)
for x in range(1, 8):
    print x, 'moves'
    id_search(x, 6, [0])