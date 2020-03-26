#!/usr/bin/env python3

import re
import itertools
import copy

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "Rounak Saraf"
    email = "rounak18183@iiitd.ac.in"
    roll_num = "2018183"

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges    = ordered_edges
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))
            
    """import copy    
    #vertices=[1,2,3,4,5,6] 
    #edges=[(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]
    i=0
    tvertices=copy.deepcopy(vertices)   
    #print(tvertices)
    while (i<len(vertices)):
        tvertices.remove(tvertices[i])
        #print(tvertices)
        #print(tvertices)
        reqlist=list(itertools.combinations(tvertices,2))
        tvertices.insert(i,vertices[i])
        i=i+1
        print(reqlist)
        for j in range(len(reqlist)):
            start_node=reqlist[j][0]
            end_node=reqlist[j][1]
            #print('start_node=',start_node)
            #print('end_node=',end_node)    
        min_dist(self,start_node,end_node)
        all_shortest_paths(self,start_node,end_node)"""                   
    def min_dist(self, start_node, end_node):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from
            end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
            ''' 
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
    def g(self):
        return g                            
    def func1(start_node,end_node):
        slist=[]
        milgaya = False
        glist=self.g()
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

    def all_shortest_paths(start_node,end_node):
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
    def all_paths(start_node, end_node, edges):
        """
        Finds all paths from node to destination with length = dist

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed

        Returns:
            List of path, where each path is list ending on destination

            Returns None if there no paths
        """
        return self.tallpaths(end_node,[start_node],[start_node],edges,list())
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

    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
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
            md=self.min_dist(start_node,end_node)
            #print('md=',md)
            sp=self.all_shortest_paths(start_node,end_node)
            #if node==3:
                #print('shortestpath=',sp)
            ap=self.all_paths(start_node,end_node,edges)
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
    def lbc(self):
        blist=[]        
        for i in range(len(vertices)):
        #print('vertices[i]=',vertices[i])
            blist.append(self.betweenness_centrality(vertices[i]))
        return blist
    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        nodes=[]
        l=self.lbc()
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
        return nodes
        return D2[0][0]  

if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6]
    edges    = [[1, 2], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5], [4, 6]]

    graph = Graph(vertices, edges)
    print(graph.top_k_betweenness_centrality())