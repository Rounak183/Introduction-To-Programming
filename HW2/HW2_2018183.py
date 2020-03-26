# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Rounak Saraf	
# Roll Number: 2018183
# Section: A
# Group: 7
# Date: 10 October,2018

def minFunc(numVar, stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

        No need for checking of invalid inputs.
        
	Do not include any print statements in the function.
	"""
	import copy
	ans=''
	thelist=[]
	if numVar==2 : 
		a=stringIn.find(')')
		minlist=[]
		for i in range(a+1):
			if stringIn[i]=='0':
				minnumlist=[0,0]
				minlist.append(minnumlist)
			elif stringIn[i]=='1':
				minnumlist=[0,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='2':
				minnumlist=[1,0]
				minlist.append(minnumlist)
			elif stringIn[i]=='3' :
				minnumlist=[1,1]
				minlist.append(minnumlist)
		dclist=[]
		for i in range(a+1,len(stringIn)):
			if stringIn[i]=='0':
				dcnumlist=[0,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='1':
				dcnumlist=[0,1]
				dclist.append(dcnumlist)
			elif stringIn[i]=='2':
				dcnumlist=[1,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='3' :
				dcnumlist=[1,1]
				dclist.append(dcnumlist)
	elif numVar==3 :
		a=stringIn.find(')')
		minlist=[]
		for i in range(a+1):
			if stringIn[i]=='0':
				minnumlist=[0,0,0]
				minlist.append(minnumlist)	
			elif stringIn[i]=='1':
				minnumlist=[0,0,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='2':
				minnumlist=[0,1,0]
				minlist.append(minnumlist)
			elif stringIn[i]=='3':
				minnumlist=[0,1,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='4':
				minnumlist=[1,0,0]
				minlist.append(minnumlist)
			elif stringIn[i]=='5':
				minnumlist=[1,0,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='6':
				minnumlist=[1,1,0]
				minlist.append(minnumlist)
			elif stringIn[i]=='7':
				minnumlist=[1,1,1]
				minlist.append(minnumlist)
		dclist=[]
		for i in range(a+1,len(stringIn)):
			if stringIn[i]=='0':
				dcnumlist=[0,0,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='1':
				dcnumlist=[0,0,1]
				dclist.append(dcnumlist)
			elif stringIn[i]=='2':
				dcnumlist=[0,1,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='3':
				dcnumlist=[0,1,1]
				dclist.append(dcnumlist)
			elif stringIn[i]=='4':
				dcnumlist=[1,0,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='5':
				dcnumlist=[1,0,1]
				dclist.append(dcnumlist)
			elif stringIn[i]=='6':
				dcnumlist=[1,1,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='7':
				dcnumlist=[1,1,1]
				dclist.append(dcnumlist)
	else:
		a=stringIn.find(')')
		minlist=[]
		for i in range(a+1):
			if stringIn[i]=='0' and stringIn[i-1]!='1':
				minnumlist=[0,0,0,0]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='10':
				minnumlist=[1,0,1,0]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='11':
				minnumlist=[1,0,1,1]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='12':
				minnumlist=[1,1,0,0]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='13':
				minnumlist=[1,1,0,1]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='14':
				minnumlist=[1,1,1,0]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='15':
				minnumlist=[1,1,1,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='7':
				minnumlist=[0,1,1,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='8':
				minnumlist=[1,0,0,0]
				minlist.append(minnumlist)
			elif stringIn[i]=='9':
				minnumlist=[1,0,0,1]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='10':
				minnumlist=[1,0,1,0]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='11':
				minnumlist=[1,0,1,1]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='12':
				minnumlist=[1,1,0,0]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='13':
				minnumlist=[1,1,0,1]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='14':
				minnumlist=[1,1,1,0]
				minlist.append(minnumlist)
			elif stringIn[i:i+2]=='15':
				minnumlist=[1,1,1,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='1' and stringIn[i-1]!='1':
				minnumlist=[0,0,0,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='2' and stringIn[i-1]!='1':
				minnumlist=[0,0,1,0]
				minlist.append(minnumlist)
			elif stringIn[i]=='3' and stringIn[i-1]!='1':
				minnumlist=[0,0,1,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='4' and stringIn[i-1]!='1':
				minnumlist=[0,1,0,0]
				minlist.append(minnumlist)
			elif stringIn[i]=='5' and stringIn[i-1]!='1':
				minnumlist=[0,1,0,1]
				minlist.append(minnumlist)
			elif stringIn[i]=='6':
				minnumlist=[0,1,1,0]
				minlist.append(minnumlist)
				
		dclist=[]
		for i in range(a+1,len(stringIn)):
			if stringIn[i]=='0' and stringIn[i-1]!='1':
				dcnumlist=[0,0,0,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='6':
				dcnumlist=[0,1,1,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='7':
				dcnumlist=[0,1,1,1]
				dclist.append(dcnumlist)
			elif stringIn[i]=='8':
				dcnumlist=[1,0,0,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='9':
				dcnumlist=[1,0,0,1]
				dclist.append(dcnumlist)
			elif stringIn[i:i+2]=='10':
				dcnumlist=[1,0,1,0]
				dclist.append(dcnumlist)
			elif stringIn[i:i+2]=='11':
				dcnumlist=[1,0,1,1]
				dclist.append(dcnumlist)
			elif stringIn[i:i+2]=='12':
				dcnumlist=[1,1,0,0]
				dclist.append(dcnumlist)
			elif stringIn[i:i+2]=='13':
				dcnumlist=[1,1,0,1]
				dclist.append(dcnumlist)
			elif stringIn[i:i+2]=='14':
				dcnumlist=[1,1,1,0]
				dclist.append(dcnumlist)
			elif stringIn[i:i+2]=='15':
				dcnumlist=[1,1,1,1]
				dclist.append(dcnumlist)
			elif stringIn[i]=='1' and stringIn[i-1]!='1':
				dcnumlist=[0,0,0,1]
				dclist.append(dcnumlist)
			elif stringIn[i]=='2' and stringIn[i-1]!='1':
				dcnumlist=[0,0,1,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='3' and stringIn[i-1]!='1':
				dcnumlist=[0,0,1,1]
				dclist.append(dcnumlist)
			elif stringIn[i]=='4' and stringIn[i-1]!='1':
				dcnumlist=[0,1,0,0]
				dclist.append(dcnumlist)
			elif stringIn[i]=='5' and stringIn[i-1]!='1':
				dcnumlist=[0,1,0,1]
				dclist.append(dcnumlist)
	minlist2=copy.deepcopy(minlist)
	#print('minlist2=',minlist2)
	minlist.extend(dclist)
	l=len(minlist)	
	s=''
	for i in range(l):
		if numVar==2:
			if minlist[i]==[0,0]:
				string='0'+','
				s=s+string
			elif minlist[i]==[0,1]:
				string='1'+','
				s=s+string
			elif minlist[i]==[1,0]:
				string='2'+','
				s=s+string
			elif minlist[i]==[1,1]:
				string='3'+','
				s=s+string
		elif numVar==3:
			if minlist[i]==[0,0,0]:
				string='0'+','
				s=s+string
			elif minlist[i]==[0,0,1]:
				string='1'+','
				s=s+string
			elif minlist[i]==[0,1,0]:
				string='2'+','
				s=s+string
			elif minlist[i]==[0,1,1]:
				string='3'+','
				s=s+string
			elif minlist[i]==[1,0,0]:
				string='4'+','
				s=s+string
			elif minlist[i]==[1,0,1]:
				string='5'+','
				s=s+string
			elif minlist[i]==[1,1,0]:
				string='6'+','
				s=s+string
			elif minlist[i]==[1,1,1]:
				string='7'+','
				s=s+string
		elif numVar==4:
			if minlist[i]==[0,0,0,0]:
				string='0'+','
				s=s+string
			elif minlist[i]==[0,0,0,1]:
				string='1'+','
				s=s+string
			elif minlist[i]==[0,0,1,0]:
				string='2'+','
				s=s+string
			elif minlist[i]==[0,0,1,1]:
				string='3'+','
				s=s+string
			elif minlist[i]==[0,1,0,0]:
				string='4'+','
				s=s+string
			elif minlist[i]==[0,1,0,1]:
				string='5'+','
				s=s+string
			elif minlist[i]==[0,1,1,0]:
				string='6'+','
				s=s+string
			elif minlist[i]==[0,1,1,1]:
				string='7'+','
				s=s+string
			elif minlist[i]==[1,0,0,0]:
				string='8'+','
				s=s+string
			elif minlist[i]==[1,0,0,1]:
				string='9'+','
				s=s+string
			elif minlist[i]==[1,0,1,0]:
				string='10'+','
				s=s+string
			elif minlist[i]==[1,0,1,1]:
				string='11'+','
				s=s+string
			elif minlist[i]==[1,1,0,0]:
				string='12'+','
				s=s+string
			elif minlist[i]==[1,1,0,1]:
				string='13'+','
				s=s+string
			elif minlist[i]==[1,1,1,0]:
				string='14'+','
				s=s+string
			elif minlist[i]==[1,1,1,1]:
				string='15'+','
				s=s+string
	s=s[0:-1]
	slist=[]
	b=0
	for i in range(len(s)):
		a=s.find(',',b+1)
		if i==0:
			string=s[b:a]
			slist.append(string)
		elif a==-1:
			string=s[b+1:]
			slist.append(string)
			break
		else:
			string=s[b+1:a]
			slist.append(string)
		b=a
	flag=[]
	for i in range(len(minlist)):
		flag.append(0)
	tempminlist=copy.deepcopy(minlist)
	s1=''
	for i in range(l-1):
		for j in range(i+1,l):
			count=0
			for h in range(numVar):
				if minlist[i][h]==minlist[j][h]:
					count=count+1
			if numVar==4:
				if count==3:
					for h in range(numVar):
						if minlist[i][h]!=minlist[j][h]:
							string='('+slist[i]+','+slist[j]+')'+','
							s1=s1+string
							flag[i]=1
							flag[j]=1
			elif numVar==3:
				if count==2:
					for h in range(numVar):
						if minlist[i][h]!=minlist[j][h]:
							string='('+slist[i]+','+slist[j]+')'+','
							s1=s1+string
							flag[i]=1
							flag[j]=1
			else:
				if count==1:
					for h in range(numVar):
						if minlist[i][h]!=minlist[j][h]:
							string='('+slist[i]+','+slist[j]+')'+','
							s1=s1+string
							flag[i]=1
							flag[j]=1
	s1=s1[0:-1]
	l=s1.count('(')
	s1list=[]
	a=0
	for i in range(l):
		b=a
		a=s1.find(')',b+1)
		if i==0:
			s1list.append(s1[b:a+1])
		else:
			s1list.append(s1[b+2:a+1])
	dellist=[]
	l=len(s1list)
	for i in range(l-1):
		for j in range(i+1,l):
			if s1list[i]==s1list[j]:
				dellist.append(j)
	l=len(dellist)
	k=0
	for i in range(l):
		s1list.pop(dellist[i]-k)
		k=k+1
	leftlist=[]
	reqlist=[]
	l=len(minlist)
	i=0
	for i in range(l):
		if flag[i]==0:
			leftlist.append(minlist[i])
			thelist.append(slist[i])
		else:
			reqlist.append(minlist[i])
	leftlist1=copy.deepcopy(leftlist)
	dellist=[]
	l=len(reqlist)
	for i in range(l-1):
		for j in range(i+1,l):
			if reqlist[i]==reqlist[j]:
				dellist.append(j)
	l=len(dellist)
	k=0
	for i in range(l):
		reqlist.pop(dellist[i]-k)
		k=k+1
	tempreqlist=copy.deepcopy(reqlist)	
	l=len(reqlist)
	newlist=[]
	for i in range(0,l-1):
		for j in range(i+1,l):
			h=0
			count=0
			for h in range(numVar):
				if reqlist[i][h]==reqlist[j][h]:
					count=count+1
			if numVar==4:
				if count==3:
					for h in range(numVar):
						if reqlist[i][h]==reqlist[j][h]:
							pass
						else:	
							numlist=copy.deepcopy(reqlist[j])
							numlist[h]='x'
							newlist.append(numlist) 
			elif numVar==3:
				if count==2:
					for h in range(numVar):
						if reqlist[i][h]==reqlist[j][h]:
					 		pass
						else:	
							numlist=copy.deepcopy(reqlist[j])
							numlist[h]='x'
							newlist.append(numlist)
			elif numVar==2:
				if count==1:
					for h in range(numVar):
						if reqlist[i][h]==reqlist[j][h]:
							pass
						else:	
							numlist=copy.deepcopy(reqlist[j])
							numlist[h]='x'
							newlist.append(numlist)  	
	dellist=[]
	l=len(newlist)
	for i in range(l-1):
		for j in range(i+1,l):
			if newlist[i]==newlist[j]:
				dellist.append(j)
	l=len(dellist)
	k=0
	for i in range(l):
		newlist.pop(dellist[i]-k)
		k=k+1
	
	l=len(newlist)
	i=0	
	flag=[]
	for i in range(l):
		flag.append(0)
	tempminlist=copy.deepcopy(newlist)
	s2=''
	s2list=[]
	templist=[]
	for i in range(l-1):
		for j in range(i+1,l):
			count=0
			for h in range(numVar):
				if newlist[i][h]==newlist[j][h]:
					count=count+1
			if numVar==4:
				if count==3:
					for h in range(numVar):
						if newlist[i][h]!=newlist[j][h]:
							string=s1list[i]+s1list[j]
							a=string.find(')')
							b=string.find('(',a)
							string=string[0:a]+','+string[b+1:]
							s2list.append(string)
							flag[i]=1
							flag[j]=1
			elif numVar==3:
				if count==2:
					for h in range(numVar):
						if newlist[i][h]!=newlist[j][h]:
							string=s1list[i]+s1list[j]
							a=string.find(')')
							b=string.find('(',a)	
							string=string[0:a]+','+string[b+1:]
							s2list.append(string)
							flag[i]=1
							flag[j]=1
			else:
				if count==1:
					for h in range(numVar):
						if newlist[i][h]!=newlist[j][h]:
							string=s1list[i]+s1list[j]
							a=string.find(')')
							b=string.find('(',a)
							string=string[0:a]+','+string[b+1:]
							s2list.append(string)
							flag[i]=1
							flag[j]=1
	leftlist=[]
	reqlist=[]
	for i in range(l):
		if flag[i]==0:
			leftlist.append(newlist[i])
			thelist.append(s1list[i])
		else:
			reqlist.append(newlist[i])	
	leftlist2=copy.deepcopy(leftlist)
	dellist=[]
	l=len(reqlist)
	for i in range(l-1):
		for j in range(i+1,l):
			if reqlist[i]==reqlist[j]:
				dellist.append(j)
	l=len(dellist)
	k=0
	for i in range(l):
		reqlist.pop(dellist[i]-k)
		k=k+1
	tempreqlist=copy.deepcopy(reqlist)
	l=len(reqlist)
	newlist2=[]
	for i in range(0,l-1):
		for j in range(i+1,l):
			h=0
			count=0
			for h in range(numVar):
				if reqlist[i][h]==reqlist[j][h]:
					count=count+1
			if numVar==4:
				if count==3:
					for h in range(numVar):
						if reqlist[i][h]==reqlist[j][h]:
							pass
						else:	
							numlist=copy.deepcopy(reqlist[j])
							numlist[h]='x'
							newlist2.append(numlist)
			elif numVar==3:
				if count==2:
					for h in range(numVar):
						if reqlist[i][h]==reqlist[j][h]:
					 		pass
						else:	
							numlist=copy.deepcopy(reqlist[j])
							numlist[h]='x'
							newlist2.append(numlist)
			elif numVar==2:
				if count==1:
					for h in range(numVar):
						if reqlist[i][h]==reqlist[j][h]:
							pass
						else:
							numlist=copy.deepcopy(reqlist[j])
							numlist[h]='x'
							newlist2.append(numlist)  	
	dellist=[]
	l=len(newlist2)
	k=0
	for i in range(l-1):
		for j in range(i+1,l):
			if newlist2[i]==newlist2[j]:
				s2list.pop(j-k)
				dellist.append(j)
				k=k+1
	l=len(dellist)
	k=0
	for i in range(l):
		newlist2.pop(dellist[i]-k)
		k=k+1
	dellist=[]
	l=len(newlist2)
	k=0
	for i in range(l-1):
		for j in range(i+1,l):
			if newlist2[i]==newlist2[j]:
				s2list.pop(j-k)
				dellist.append(j)
				k=k+1
	l=len(dellist)
	k=0
	for i in range(l):
		newlist2.pop(dellist[i]-k)
		k=k+1
	dellist=[]
	l=len(newlist2)
	k=0
	for i in range(l-1):
		for j in range(i+1,l):
			if newlist2[i]==newlist2[j]:
				s2list.pop(j-k)
				dellist.append(j)
				k=k+1
	l=len(dellist)
	k=0
	for i in range(l):
		newlist2.pop(dellist[i]-k)
		k=k+1	
	if numVar==3 or numVar==4:
		flag=[]
		l=len(newlist2)
		for i in range(l):
			flag.append(0)
		tempnewlist=copy.deepcopy(newlist2)
		s3list=[]
		for i in range(l-1):
			for j in range(i+1,l):
				count=0
				for h in range(numVar):
					if newlist2[i][h]==newlist2[j][h]:
						count=count+1
				if numVar==4:
					if count==3:
						for h in range(numVar):
							if newlist2[i][h]!=newlist2[j][h]:
								string=s2list[i]+s2list[j]
								a=string.find(')')
								b=string.find('(',a)
								string=string[0:a]+','+string[b+1:]
								s3list.append(string)
								flag[i]=1
								flag[j]=1
				elif numVar==3:
					if count==2:
						for h in range(numVar):
							if newlist2[i][h]!=newlist2[j][h]:
								string=s2list[i]+s2list[j]
								a=string.find(')')
								b=string.find('(',a)
								string=string[0:a]+','+string[b+1:]
								s3list.append(string)
								flag[i]=1
								flag[j]=1
				else:
					if count==1:
						for h in range(numVar):
							if newlist2[i][h]!=newlist2[j][h]:
								string=s2list[i]+s2list[j]
								a=string.find(')')
								b=string.find('(',a)
								string=string[0:a]+','+string[b+1:]
								s3list.append(string)
								flag[i]=1
								flag[j]=1
		leftlist=[]
		reqlist=[]
		for i in range(l):
			if flag[i]==0:
				leftlist.append(newlist2[i])
				thelist.append(s2list[i])
			else:
				reqlist.append(newlist2[i])
		dellist=[]
		l=len(reqlist)
		for i in range(l-1):
			for j in range(i+1,l):
				if reqlist[i]==reqlist[j]:
					dellist.append(j)
		l=len(dellist)
		k=0
		for i in range(l):
			reqlist.pop(dellist[i]-k)
			k=k+1
		tempreqlist=copy.deepcopy(reqlist)
		leftlist3=copy.deepcopy(leftlist)
		l=len(reqlist)
		newlist=[]
		s3=[]
		for i in range(0,l-1):
			for j in range(i+1,l):
				h=0
				count=0
				for h in range(numVar):
					if reqlist[i][h]==reqlist[j][h]:
						count=count+1
				if numVar==4:
					if count==3:
						for h in range(numVar):
							if reqlist[i][h]==reqlist[j][h]:
								pass
							else:	
								numlist=copy.deepcopy(reqlist[j])
								numlist[h]='x'
								newlist.append(numlist) 
				elif numVar==3:
					if count==2:
						for h in range(numVar):
							if reqlist[i][h]==reqlist[j][h]:
						 		pass
							else:
								numlist=copy.deepcopy(reqlist[j])
								numlist[h]='x'
								newlist.append(numlist) 
								
				elif numVar==2:
					if count==1:
						for h in range(numVar):
							if reqlist[i][h]==reqlist[j][h]:
								pass
							else:	
								numlist=copy.deepcopy(reqlist[j])
								numlist[h]='x'
								newlist.append(numlist) 
		dellist=[]
		l=len(newlist)
		#print('newlist=',newlist)
		k=0
		for i in range(l-1):
			for j in range(i+1,l):
				if newlist[i]==newlist[j]:				
					if l-1 in dellist:
						break
					dellist.append(j)
		l=len(dellist)
		k=0
		for i in range(l):
			newlist.pop(dellist[i]-k)
			s3list.pop(dellist[i]-k)
			k=k+1
		if numVar==4:
			l=len(newlist)	
			i=0
			flag=[]
			for i in range(l):
				flag.append(0)
			tempminlist=copy.deepcopy(newlist)
			s4list=[]
			for i in range(l-1):
				for j in range(i+1,l):
					count=0
					for h in range(numVar):
						if newlist[i][h]==newlist[j][h]:
							count=count+1
					if numVar==4:
						if count==3:
							for h in range(numVar):
								if newlist[i][h]!=newlist[j][h]:
									string=s3list[i]+s3list[j]
									a=string.find(')')
									b=string.find('(',a)
									string=string[0:a]+','+string[b+1:]
									s4list.append(string)
									flag[i]=1
									flag[j]=1
					elif numVar==3:
						if count==2:
							for h in range(numVar):
								if newlist[i][h]!=newlist[j][h]:
									string=s3list[i]+s3list[j]
									a=string.find(')')
									b=string.find('(',a)
									string=string[0:a]+','+string[b+1:]
									s4list.append(string)
									flag[i]=1
									flag[j]=1
					else:	
						if count==1:
							for h in range(numVar):
								if newlist[i][h]!=newlist[j][h]:
									string=s3list[i]+s3list[j]
									a=string.find(')')
									b=string.find('(',a)
									string=string[0:a]+','+string[b+1:]
									s4list.append(string)
									flag[i]=1
									flag[j]=1
			leftlist=[]	
			reqlist=[]
			i=0
			for i in range(l):
				if flag[i]==0:
					leftlist.append(newlist[i])
					thelist.append(s3list[i])
				else:
					reqlist.append(newlist[i])
			leftlist4=copy.deepcopy(leftlist)
			if len(s4list)==1 or len(minlist)==16:
				ans='wxyz'
				#print(ans)
				return(ans)			
			elif numVar==3 and (len(s3list)==1 or len(minlist)==8):
				ans='wxy'
				#print(ans)
				return(ans)
			elif numVar==2 and (len(s2list)==1 or len(minlist)==4):	
				ans='wx'
				#print(ans)
				return(ans)
	if ans=='':	
		fllist=[]
		#print('newlist=',newlist)
		fllist.extend(leftlist1)
		fllist.extend(leftlist2)
		if numVar==3 or numVar==4:
			fllist.extend(leftlist3)
		if numVar==4:
			fllist.extend(leftlist4)
		dellist=[]
		l=len(fllist)
		k=0
		for i in range(l-1):
			for j in range(i+1,l):
				if fllist[i]==fllist[j]:				
					if l-1 in dellist:
						break
					dellist.append(j)
		l=len(dellist)
		k=0
		for i in range(l):
			fllist.pop(dellist[i]-k)
			thelist.pop(dellist[i]-k)
			k=k+1
		string1=''
		string2=''
		l=len(fllist)
		if l==0:
			if numVar==2:
				string2='wx'
			elif numVar==3:
				string2='wxy'
			elif numVar==4:
				string2='wxyz'
		for i in range(l):
			for h in range(numVar):
				if h==0:
					if fllist[i][h]==0:
						string="w'"
					elif fllist[i][h]==1:
						string="w"			
					elif fllist[i][h]=='x':
						string=''
				elif h==1:	
					if fllist[i][h]==0:
						string="x'"
					elif fllist[i][h]==1:
						string="x"
					elif fllist[i][h]=='x':
						string=''
				elif h==2:
					if fllist[i][h]==0:
						string="y'"
					elif fllist[i][h]==1:
						string="y"
					elif fllist[i][h]=='x':
						string=''
				elif h==3:
					if fllist[i][h]==0:
						string="z'"
					elif fllist[i][h]==1:
						string="z"
					elif fllist[i][h]=='x':
						string=''
				string1=string1+string
			if i==0:
				string2=string2+''+string1
				string1=''
			else:
				string2=string2+'+'+string1
				string1=''
		minbinlist=[]
		for i in range(len(minlist2)):
			if numVar==4:
				if minlist2[i]==[0,0,0,0]:
					minbinlist.append(0)
				elif minlist2[i]==[0,0,0,1]:
					minbinlist.append(1)
				elif minlist2[i]==[0,0,1,0]:
					minbinlist.append(2)
				elif minlist2[i]==[0,0,1,1]:
					minbinlist.append(3)
				elif minlist2[i]==[0,1,0,0]:
					minbinlist.append(4)
				elif minlist2[i]==[0,1,0,1]:
					minbinlist.append(5)
				elif minlist2[i]==[0,1,1,0]:
					minbinlist.append(6)
				elif minlist2[i]==[0,1,1,1]:
					minbinlist.append(7)
				elif minlist2[i]==[1,0,0,0]:
					minbinlist.append(8)
				elif minlist2[i]==[1,0,0,1]:
					minbinlist.append(9)
				elif minlist2[i]==[1,0,1,0]:
					minbinlist.append(10)
				elif minlist2[i]==[1,0,1,1]:
					minbinlist.append(11)
				elif minlist2[i]==[1,1,0,0]:
					minbinlist.append(12)
				elif minlist2[i]==[1,1,0,1]:
					minbinlist.append(13)
				elif minlist2[i]==[1,1,1,0]:
					minbinlist.append(14)
				elif minlist2[i]==[1,1,1,1]:
					minbinlist.append(15)
			elif numVar==3:
				if minlist[i]==[0,0,0]:
					minbinlist.append(0)
				elif minlist[i]==[0,0,1]:
					minbinlist.append(1)
				elif minlist[i]==[0,1,0]:
					minbinlist.append(2)
				elif minlist[i]==[0,1,1]:
					minbinlist.append(3)
				elif minlist[i]==[1,0,0]:
					minbinlist.append(4)
				elif minlist[i]==[1,0,1]:
					minbinlist.append(5)
				elif minlist[i]==[1,1,0]:
					minbinlist.append(6)
				elif minlist[i]==[1,1,1]:
					minbinlist.append(7)
			elif numVar==2:
				if minlist[i]==[0,0]:
					minbinlist.append(0)
				elif minlist[i]==[0,1]:
					minbinlist.append(1)
				elif minlist[i]==[1,0]:
					minbinlist.append(2)
				elif minlist[i]==[1,1]:
					minbinlist.append(3)
		counter=[]	
		for i in range(len(minbinlist)):
			counter.append(0)
		for i in range(len(thelist)):
			for j in range(len(thelist[i])):
				if thelist[i][j] in str(minbinlist) and thelist[i][j].isdigit():
					if str(thelist[i][j-1])=='1':
						if str(thelist[i][j])=='1':
							if 11 in minbinlist:
								for k in range(len(minbinlist)):
									if minbinlist[k]==11:
										counter[k]=counter[k]+1
						elif str(thelist[i][j])=='2':
							if 12 in minbinlist:
								for k in range(len(minbinlist)):
									if minbinlist[k]==12:
										counter[k]=counter[k]+1
						elif str(thelist[i][j])=='3':
							if 13 in minbinlist:
								for k in range(len(minbinlist)):
									if minbinlist[k]==13:
										counter[k]=counter[k]+1
						elif str(thelist[i][j])=='4':
							if 14 in minbinlist:
								for k in range(len(minbinlist)):
									if minbinlist[k]==14:
										counter[k]=counter[k]+1
						elif str(thelist[i][j])=='5':
							if 15 in minbinlist:
								for k in range(len(minbinlist)):
									if minbinlist[k]==15:
										counter[k]=counter[k]+1
						elif str(thelist[i][j])=='0':
							if 10 in minbinlist:
								for k in range(len(minbinlist)):
									if minbinlist[k]==10:
										counter[k]=counter[k]+1
					elif thelist[i][j]=='1' and thelist[i][j-1].isdigit()==False and thelist[i][j+1].isdigit()==False:
						if 1 in minbinlist:
							for k in range(len(minbinlist)):
								if minbinlist[k]==1:
									counter[k]=counter[k]+1
					elif thelist[i][j]!='1':
						for k in range(len(minbinlist)):
							if str(minbinlist[k])==str(thelist[i][j]):
								counter[k]=counter[k]+1
		flminlist=[]
		#print('fllist=',fllist)
		string=''
		string2=''
		for i in range(len(fllist)):
			for h in range(numVar):
				s=''
				if fllist[i][h]==0:
					if h==0:
						s="w'"
						string=string+s
					elif h==1:
						s="x'"
						string=string+s
					elif h==2:
						s="y'"
						string=string+s
					elif h==3:
						s="z'"
						string=string+s
				elif fllist[i][h]==1:
					if h==0:
						s="w"
						string=string+s
					elif h==1:
						s="x"
						string=string+s
					elif h==2:
						s="y"
						string=string+s
					elif h==3:
						s="z"
						string=string+s
				elif fllist[i][h]=='x':
					s=''
					string=string+s
			string2=string2+string
			string=''
			flminlist.append(string2)
			string2=''
		#print('flminlist=',flminlist)
		donemblist=[]
		epilist=[]
		a=0	
		b=0
		for i in range(len(minbinlist)):
			if counter[i]==1:
				b=0
				for j in range(len(thelist)):
					if str(minbinlist[i]) in thelist[j]:
						tempj=copy.deepcopy(j)
						epilist.append(str(flminlist[j]))
						donemblist.append(str(minbinlist[i]))
				for h in range(len(thelist[tempj])):
					a=thelist[tempj].find(',',b+1)
					if a==-1:
						a=thelist[tempj].find(')',b+1)
						string=thelist[tempj][b+1:a]
						if string in str(minbinlist):
							donemblist.append(string)
						break
					string=thelist[tempj][b+1:a]
					b=a
					if string in str(minbinlist):
						donemblist.append(string)
			dellist=[]
			l=len(donemblist)
			k=0
			for i in range(l-1):
				for j in range(i+1,l):
					if donemblist[i]==donemblist[j]:				
						if l-1 in dellist:
							break
						dellist.append(j)
			l=len(dellist)
			k=0
			for i in range(l):
				donemblist.pop(dellist[i]-k)
				k=k+1		
			dellist=[]
			l=len(epilist)
			k=0
			for i in range(l-1):
				for j in range(i+1,l):
					if epilist[i]==epilist[j]:				
						if l-1 in dellist:
							break
						dellist.append(j)
			l=len(dellist)
			k=0
			for i in range(l):
				epilist.pop(dellist[i]-k)
				k=k+1			
		strmblist=[]			
		for i in range(len(minbinlist)):
			strmblist.append(str(minbinlist[i]))
		k=0
		l=copy.deepcopy(len(strmblist))
		for i in range(l-k):
			if strmblist[i-k] in donemblist:
				strmblist.pop(i-k)
				k=k+1
		#print('strmblist=',strmblist)
		#print('donemblist=',donemblist)
		dellist=[]
		l=len(donemblist)
		k=0
		for i in range(l-1):
			for j in range(i+1,l):
				if donemblist[i]==donemblist[j]:				
					if l-1 in dellist:
						break
					dellist.append(j)
		l=len(dellist)
		k=0
		for i in range(l):
			donemblist.pop(dellist[i]-k)
			k=k+1
		#print('donemblist=',donemblist)
		dellist=[]
		l=len(donemblist)
		k=0
		for i in range(l-1):
			for j in range(i+1,l):
				if donemblist[i]==donemblist[j]:				
					if l-1 in dellist:
						break
					dellist.append(j)
		l=len(dellist)
		k=0
		for i in range(l):
			donemblist.pop(dellist[i]-k)
			k=k+1
		#print('donemblist=',donemblist)
		string1=''
		string2=''
		epilist1=[]
		epilist2=[]
		#print('thelist=',thelist)
		#print('strmblist=',strmblist)
		if len(strmblist)!=0:
			countthelist=[]
			for i in range(len(thelist)):
				countthelist.append(0)
			for i in range(len(strmblist)):
				for j in range(len(thelist)):	
					jmax=0
					if strmblist[i] in thelist[j]:
						print('True')
						countthelist[j]=countthelist[j]+1
						maxn=countthelist[0]
						if countthelist[j]>=maxn:
							jmax=j
							maxn=countthelist[j]
			#print('jmax=',jmax)
			for i in range(len(thelist)):
				epilist.append(flminlist[jmax])
			j=jmax
			#print('epilist=',epilist)
			b=0
			for h in range(len(thelist[j])):
				a=thelist[j].find(',',b+1)
				if a==-1:
					a=thelist[j].find(')',b+1)
					string=thelist[j][b+1:a]
					donemblist.append(string)
					break
				string=thelist[j][b+1:a]
				b=a
				donemblist.append(string)
			b=0
			k=0
			l=copy.deepcopy(len(strmblist))
			for i in range(l-k):
				if strmblist[i-k] in donemblist:
					strmblist.pop(i-k)
					k=k+1
			dellist=[]
			l=len(epilist)
			k=0
			for i in range(l-1):
				for j in range(i+1,l):
					if epilist[i]==epilist[j]:				
						if l-1 in dellist:
							break
						dellist.append(j)
			l=len(dellist)
			k=0
			for i in range(l):
				epilist.pop(dellist[i]-k)
				k=k+1	
			dellist=[]
			l=len(donemblist)
			k=0
			for i in range(l-1):
				for j in range(i+1,l):
					if donemblist[i]==donemblist[j]:				
						if l-1 in dellist:
							break
						dellist.append(j)
			dellist2=[]
			l=len(dellist)
			k=0
			for i in range(l-1):
				for j in range(i+1,l):
					if dellist[i]==dellist[j]:				
						if l-1 in dellist:
							break
						dellist2.append(j)
			l=len(dellist2)
			k=0
			for i in range(l):
				dellist.pop(dellist2[i]-k)
				k=k+1
			l=len(dellist)
			k=0
			for i in range(l):
				donemblist.pop(dellist[i]-k)
				k=k+1
			epilist1=copy.deepcopy(epilist)
			epilist2=copy.deepcopy(epilist)
			for i in range(len(thelist)):
				for j in range(len(strmblist)):
					if strmblist[j] in thelist[i]:
						epilist1.append(flminlist[i])
						tempi=copy.deepcopy
					break
			for i in range(len(thelist)):
				for j in range(len(strmblist)):
					if strmblist[j] in thelist[i]:
						epilist2.append(flminlist[i])
						break
			epilist1.pop(len(epilist1)-1)
			epilist2.pop(len(epilist2)-2)
			dellist=[]
			l=len(epilist1)
			k=0
			for i in range(l-1):
				for j in range(i+1,l):
					if epilist1[i]==epilist1[j]:				
						if l-1 in dellist:
							break
						dellist.append(j)
			l=len(dellist)
			k=0
			for i in range(l):
				epilist1.pop(dellist[i]-k)
				k=k+1
			dellist=[]
			l=len(epilist2)
			k=0
			for i in range(l-1):
				for j in range(i+1,l):
					if epilist2[i]==epilist2[j]:				
						if l-1 in dellist:
							break
						dellist.append(j)
			l=len(dellist)
			k=0
			for i in range(l):
				epilist2.pop(dellist[i]-k)
				k=k+1
			#print('epilist1=',epilist1)
			#print('epilist2=',epilist2)
			for i in range(len(epilist1)):
				string=epilist1[i]
				if string in string1:
					pass
				else:
					string1=string1+string+'+'
			string1=string1[:-1]
			#print('string1=',string1)
			for i in range(len(epilist2)):
				string=epilist2[i]
				if string in string2:
					pass
				else:
					string2=string2+string+'+'
			string2=string2[:-1]
			#print('string2=',string2)
		#print('epilist=',epilist)
		stringreq=''
		for i in range(len(epilist)):
			string=epilist[i]
			if string in stringreq:
				pass
			else:
				stringreq=stringreq+string+'+'
		stringreq=stringreq[:-1]
		#print('stringreq=',stringreq) 
		def sortLexo(my_string): 
	
	   		words = my_string.split('+')  
	   		words.sort()  
	   		string=''   
	   		for i in words:
	   	   		string=string+i+'+'
	   		return(string[:-1])
		if(len(epilist)>len(epilist1)):
			answer=sortLexo(stringreq)
		else:
			if len(epilist1)>len(epilist2):
				answer=sortLexo(string1)
			elif len(epilist2)>len(epilist1):
				answer=sortLexo(string2)
			elif (len(epilist1)==len(epilist2)) and epilist1!=epilist2:
				answer=sortLexo(string1)+' OR '+sortLexo(string2)
			else:
				answer=sortLexo(string1)
		ans=answer
		print(ans)
		return(ans)		
#minFunc(3,'(0,2,5,6) d(3,7)')
#minFunc(4,'(4,6,9,10,11,13) d(2,12,15)')
#minFunc(4,'(0,1,3,4,5,6,8,10,12) d(2,7,9,11,13,14,15)')
#minFunc(2,'(0,1) d(3)')
#minFunc(4,'(6,7,8,9) d(10,11,12,13,14,15)')
#minFunc(4,'(0,1,3,7,8,9,11,15)')

		
"""The slist's are the lists containing the arithmetic values of the minterms after the respective stages. Each new stage list is made by comparison of elements differing by 1 bit from the previous list. The leftover elements,i.e., which are uncompared are appended into a list and they are then the carried on forward to carry the Patrick's method. The count of the minterms with count as 1 is marked and it's corresponding minterms in the list(thelist[j]) are marked as they are no longer required for the calculation of the E.P.I's. Next the P.I.'s covering the maximum minterms is selected as it would mark most of the other minterms and so is done. Now, the only left P.I.'s will be the ones with count of minterms is one. Both of these can be included in the final answer and so is represented by adding 'OR'.If in case of x variables,we have a list of x dashes, we can directly have the answer as 1."""  
				


	
	
	

	
