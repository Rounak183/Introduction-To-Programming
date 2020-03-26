vertices=[1,2,3,4,5,6]
edges=[[1, 2], [1, 5], [2, 3], [2, 5], [3, 4],[3, 6], [4, 5], [4, 6]]
import copy
import itertools
import copy    
def mindist(start_node,end_node):
	q=[]
	glist=[]
	poplist=[]
	mlist=[]
	q.append(start_node)
	for i in range(len(edges)):
		if start_node==edges[i][0]:
			q.append(edges[i][1])
			glist.append([start_node,edges[i][1]])
		elif start_node==edges[i][1]:
			q.append(edges[i][0])
			glist.append([start_node,edges[i][0]])
	#print('glist=',glist)
	q.remove(start_node)
	#print('q=',q)
	poplist.append(start_node)
	#print('poplist=',poplist)
	while len(q)>0:
		i=0
		while(i<len(q)):
			#print(i)
			for j in range(len(edges)):
				if q[i]==edges[j][0]:
					#print('q[i]=',q[i])
					if edges[j][1] in poplist:
						pass
					elif edges[j][1] in q:
						pass
					else:
						q.append(edges[j][1])
						#print(q)
						glist.append([q[i],edges[j][1]])
						#print(glist)	
				elif q[i]==edges[j][1]:
					#print('q[i]=',q[i])
					if edges[j][0] in poplist:
						pass
					elif edges[j][0] in q:
						#glist.append([q[i],edges[j][0]])
						pass
					else:
						q.append(edges[j][0])
						glist.append([q[i],edges[j][0]])			
				#print('q=',q,i,j)
			poplist.append(q[0])	
			q.remove(q[0])
			#print(i)
			#print('poplist=',poplist)
			#print('glist=',glist)
	g1=copy.deepcopy(glist)
	#print(glist)
	g=[]		
	#g1 = [[1, 2], [1, 5], [2, 3], [5, 4], [3, 6]]
	g1=glist
	for i in range(len(glist)):
		g.append([start_node])
	#print(g)	
	count = 0
	s = []
	i=0
	while(i<len(g1)):
		if(g1[i][0]==start_node):
			s.append(g1[i][1])
			g[count].append(g1[i][1])
			g1.pop(i)
			count+=1
			i-=1	
		i+=1	
	i=0
	while(i<count):
		z = s[i]
		for k in g1:
			if(z==k[0]):
				g[i].append(k[1])
				z = k[1]
				g1.pop(g1.index(k))
		i+=1	
	#print(g)
	#print(g1)
	chup=0

	for j in g1:	
		while(chup<len(g) and chup < 10):
			if(j[0] in g[chup]):
				temp = g[chup][:g[chup].index(j[0])]
				temp.extend(j)
				g = g[:chup] + [temp] + g[chup:]
				chup+=1
			chup+=1	
		chup=0	
	#print(g)
	for i in range(len(g)):
		if g[i][0]==start_node:
			for j in range(len(g[i])):
				if g[i][j]==end_node:
					mindist=j+1	
	return(mindist)
#print('minimum distance=',mindist(start_node,end_node))	
def g():
	return g							
def func1(start_node,end_node):
	slist=[]
	milgaya = False
	glist=g()
	for i in range(len(glist)):
		if glist[i][0]==start_node:
			#print('True')
			for j in range(len(glist[i])):
				if glist[i][j]==end_node:
					#print('sadasd')
					if len(glist[0:j+1])==mindist(start_node,end_node):
						slist.append(glist[i][0:j+1])
						milgaya = True
						break
						#print('slist=',slist)
			if(milgaya):
				break
	return slist
#print(func1(1,6))	
visited=[]
for i in range(len(vertices)):
	visited.append('f')	
def allpaths(start_node,end_node,edges):
	return tallpaths(end_node,[start_node],[start_node],edges,list())
def tallpaths(end_node,currentPath,usedNodes,edges,paths):
	lastNode=currentPath[-1]
	#print('end_node=',end_node)
	#print('currentPath=',currentPath)
	if lastNode==end_node:
		paths.append(list(currentPath))
	else:
		for i in range(len(edges)):
			if lastNode==edges[i][0]:
				if edges[i][1] not in usedNodes:
					currentPath.append(edges[i][1])
					usedNodes.append(edges[i][1])
					tallpaths(end_node,currentPath,usedNodes,edges,paths)
					usedNodes.remove(edges[i][1])
					currentPath.pop()
			elif lastNode==edges[i][1]:
				if edges[i][0] not in usedNodes:
					currentPath.append(edges[i][0])
					usedNodes.append(edges[i][0])		
					tallpaths(end_node,currentPath,usedNodes,edges,paths)	
					usedNodes.remove(edges[i][0])
					currentPath.pop()
		return paths
#print('allpaths are:',allpaths(1,6,[[1, 2], [1, 5], [2, 3], [2, 5], [3, 4], [3, 6], [4, 5], [4, 6]]))	
#print('allpaths are:',allpaths(start_node,end_node,edges))
def shortestpaths(start_node,end_node):
	shortpathslist=[]
	#allpath=allpaths(1,6,[[1, 2], [1, 5], [2, 3], [2, 5], [3, 4], [3, 6], [4, 5], [4, 6]])
	allpath=allpaths(start_node,end_node,edges)
	#print('allpaths are',allpath)
	for i in range(len(allpath)):
		if len(allpath[i])==mindist(start_node,end_node):
			if allpath[i][0]==start_node and allpath[i][-1]==end_node:
				#print('allpath[i]=',allpath[i])
				shortpathslist.append(allpath[i])
	return shortpathslist			
#print('shortestpaths are:',shortestpaths(1,6))
#print('shortestpaths are:',shortestpaths(start_node,end_node))
def betweennesscentrality(node):
	for i in range(len(vertices)):
		if node==vertices[i]:
			a=i
	tvertices=copy.deepcopy(vertices)
	s=0   
	#print(tvertices)
	tvertices.remove(node)
	#print(tvertices)
	#print(tvertices)
	reqlist=list(itertools.combinations(tvertices,2))
	tvertices.insert(a,node)
	#if node==3:
		#print('reqlist=',reqlist)
	for j in range(len(reqlist)):
		#print('len(reqlist)=',len(reqlist))
		#print('j=',j)
		start_node=reqlist[j][0]
		end_node=reqlist[j][1]
		#if node==3:    
			#print('start_node=',start_node)
			#print('end_node=',end_node)
		count=0
		#if node==3:
			#print('node=',node)
		md=mindist(start_node,end_node)
		#print('md=',md)
		sp=shortestpaths(start_node,end_node)
		#if node==3:
			#print('shortestpath=',sp)
		ap=allpaths(start_node,end_node,edges)
		#print('ap=',ap)
		for k in range(len(sp)):
			if node in sp[k]:
				count=count+1
				#if node==3:
					#print('count=',count)
		minbet=count/len(sp)
		#if node==3:
			#print('minbet=',minbet)
		s=s+minbet
		#if node==3:
			#print('sum=',s)
	return s
def lbc():
	blist=[]		
	for i in range(len(vertices)):
	#print('vertices[i]=',vertices[i])
		blist.append(betweennesscentrality(vertices[i]))
	return blist
def topk():
	nodes=[]
	l=lbc()
	D={}
	for i in range(len(l)):
		D[vertices[i]]=l[i]
	#print('l=',l)
	#print('D=',D)
	D2=(sorted([[v, k] for k, v in D.items()], reverse=True))
	#print('D2=',D2)
	for i in range(len(D2)-1):
		if D2[i][0]==D2[i+1][0]:
			nodes.append(D2[i][1])
	print('Top k nodes=',nodes)
	print('Their betweennesscentrality=',D2[0][0])	
topk()	


