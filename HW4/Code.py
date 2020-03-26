import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
plt.ion()
figure=input()
if figure=='polygon':
	X=list(map(int,input().split()))
	Y=list(map(int,input().split()))
	X.append(X[0])
	Y.append(Y[0])
	plt.plot(X,Y)
	X.pop()
	Y.pop()
if figure=='disc':
	#print('true')
	si=list(map(int,input().split()))
	a=si[0]
	b=si[1]
	r=si[2]
	r1=r2=r
	#print('si=',si)
	rot=0
	plt.axes()
	ell=Ellipse((a,b),r1,r2,rot,fc='b')
	plt.gca().add_patch(ell)
	plt.axis('scaled')
	plt.show()
while(True):
	oper=list(map(str,input().split()))
	#print('oper=',oper)
	if (oper[0]=='quit'):
		break
	if figure =='disc':
		if oper[0]=='S':
			x=float(oper[1])
			y=float(oper[2])
			#print('x=',x)
			#print('y=',y)
			A=[]
			for i in range(3):
				A.append([])
				#print('A=',A)
				for j in range(3):
					if i==0:
						if j==0:
							#print('x=',x)
							A[i].append(x)
							#print('A=',A,i,j)
						else:
							A[i].append(0)
					if i==1:
						if j==1:
							A[i].append(y)
						else:
							A[i].append(0)
					if i==2:
						if j==2:
							A[i].append(1)
						else:	
							A[i].append(0)
							
			#print('A=',A)
			B=[]
			for i in range(3):
				if i==0:
					B.append(r1)
				elif i==1:
					B.append(r2)	
				else:
					B.append(1)
			#print('B=',B)
			C=[]
			for i in range(3):
				s=0
				for j in range(3):
					s=s+A[i][j]*B[j]
				C.append(s)
			#print('C=',C)
			r1=C[0]
			r2=C[1]
			print(a,b,r1,r2,rot)
			plt.clf()	
			plt.axes()
			ell=Ellipse((a,b),r1,r2,rot,fc='b')
			plt.gca().add_patch(ell)
			plt.axis('scaled')
			plt.show()
		if oper[0]=='T':
			dx=float(oper[1])
			dy=float(oper[2])
			A=[]
			for i in range(3):
				A.append([])
				for j in range(3):
					if i==0:
						if j==0:
							A[i].append(1)
						elif j==2:
							A[i].append(dx)
						else:
							A[i].append(0)
					if i==1:
						if j==1:
							A[i].append(1)
						elif j==2:
							A[i].append(dy)
						else:
							A[i].append(0)
					if i==2:
						if j==2:
							A[i].append(1)
						else:
							A[i].append(0)
			#print('A=',A)
			B=[]
			for i in range(3):
				if i==0:
					B.append(a)
				elif i==1:
					B.append(b)
				else:
					B.append(1)	
			#print('B=',B)
			C=[]
			for i in range(3):
				s=0
				for j in range(3):
					s=s+A[i][j]*B[j]
				C.append(s)
			#print('C=',C)
			a=C[0]
			b=C[1]
			print(a,b,r1,r2,rot)
			plt.clf()
			plt.axes()
			ell=Ellipse((a,b),r1,r2,rot,fc='b')
			plt.gca().add_patch(ell)
			plt.axis('scaled')
			plt.show()
		if oper[0]=='R':
			#print('oper=',oper)
			rot=rot+float(oper[1])
			print(a,b,r1,r2,rot)
			plt.clf()	
			plt.axes()
			ell=Ellipse((a,b),r1,r2,rot,fc='b')
			plt.gca().add_patch(ell)
			plt.axis('scaled')
			plt.show()
	elif figure =='polygon':
		if oper[0] =='S':
			x=float(oper[1])
			y=float(oper[2])
			#print('x=',x)
			#print('y=',y)
			A=[]
			for i in range(3):
				A.append([])
				for j in range(3):
					if i==0:
						if j==0:
							A[i].append(x)
						else:
							A[i].append(0)
					if i==1:
						if j==1:
							A[i].append(y)
						else:
							A[i].append(0)
					if i==2:
						if j==2:
							A[i].append(1)
						else:
							A[i].append(0)
			Cf=[]
			for k in range(len(X)):
				B=[]
				xv=X[k]
				yv=Y[k]
				Cf.append([])
				for i in range(3):
					if i==0:
						B.append(xv)
					elif i==1:
						B.append(yv)
					else:
						B.append(1)
				C=[]
				for i in range(3):
					s=0
					for j in range(3):
						s=s+A[i][j]*B[j]
					C.append(s)
					Cf[k].append(C[i])
			#print('Cf=',Cf)	
			X=[]
			Y=[]
			for i in range(len(Cf)):
				X.append(Cf[i][0])
				Y.append(Cf[i][1])
			#print(X)
			#print(Y)
			plt.clf()
			X.append(X[0])
			Y.append(Y[0])
			plt.plot(X,Y)
			X.pop()
			Y.pop()
			SX=''
			for i in range(len(X)):
				SX=SX+str(X[i])+' '
			print(SX)
			SY=''
			for i in range(len(Y)):
				SY=SY+str(Y[i])+' '
			print(SY)		
		if oper[0]=='T':
			dx=float(oper[1])
			dy=float(oper[2])
			A=[]
			for i in range(3):
				A.append([])
				for j in range(3):
					if i==0:
						if j==0:
							A[i].append(1)
						elif j==2:
							A[i].append(dx)
						else:
							A[i].append(0)
					if i==1:
						if j==1:
							A[i].append(1)
						elif j==2:
							A[i].append(dy)
						else:
							A[i].append(0)
					if i==2:
						if j==2:
							A[i].append(1)
						else:
							A[i].append(0)
				#print('A=',A)
			Cf=[]
			for k in range(len(X)):
				B=[]
				xv=X[k]
				yv=Y[k]
				Cf.append([])
				for i in range(3):
					if i==0:
						B.append(xv)
					elif i==1:
						B.append(yv)
					else:
						B.append(1)
				C=[]
				for i in range(3):
					s=0
					for j in range(3):
						s=s+A[i][j]*B[j]
					C.append(s)
					Cf[k].append(C[i])
			#print(Cf)
			X=[]
			Y=[]
			for i in range(len(Cf)):
				X.append(Cf[i][0])
				Y.append(Cf[i][1])
			#print(X)
			#print(Y)
			plt.clf()
			X.append(X[0])
			Y.append(Y[0])
			plt.plot(X,Y)
			X.pop()
			Y.pop()
			SX=''
			for i in range(len(X)):
				SX=SX+str(X[i])+' '
			print(SX)
			SY=''
			for i in range(len(Y)):
				SY=SY+str(Y[i])+' '
			print(SY)	
		if oper[0]=='R':
			import math			
			rad=(math.pi)*(float(oper[1])/180)
			cos=math.cos(rad)
			sin=math.sin(rad)
			A=[]
			for i in range(3):
				A.append([])
				for j in range(3):
					if i==0:
						if j==0:
							A[i].append(cos)
						elif j==1:
							A[i].append(-sin)
						else:
							A[i].append(0)
					if i==1:
						if j==0:
							A[i].append(sin)	
						elif j==1:
							A[i].append(cos)
						else:
							A[i].append(0)
					if i==2:
						if j==2:
							A[i].append(1)
						else:
							A[i].append(0)
			Cf=[]
			for k in range(len(X)):
				B=[]
				xv=X[k]
				yv=Y[k]
				Cf.append([])
				for i in range(3):
					if i==0:
						B.append(xv)
					elif i==1:
						B.append(yv)
					else:
						B.append(1)
				C=[]
				for i in range(3):
					s=0
					for j in range(3):
						s=s+A[i][j]*B[j]
					C.append(s)
					Cf[k].append(C[i])
			#print(Cf)
			X=[]
			Y=[]
			for i in range(len(Cf)):
				X.append(Cf[i][0])
				Y.append(Cf[i][1])
			#print(X)
			#print(Y)
			plt.clf()
			X.append(X[0])
			Y.append(Y[0])
			plt.plot(X,Y)
			X.pop()
			Y.pop()
			SX=''
			for i in range(len(X)):
				SX=SX+str(X[i])+' '
			print(SX)
			SY=''
			for i in range(len(Y)):
				SY=SY+str(Y[i])+' '
			print(SY)							
				
"""Documentation - Here not using functions I have created matrix multiplication operations using 3 
if else statements in each of the figures. After the required inputs, I have plotted the respective 
polygons and discs using the specified functions. I have also updated each time the operations are
done."""

"""Resources - 
1. Stack Exchange
2. Geeksforgeeks
3. Youtube video lectures.""" 								
							
		

