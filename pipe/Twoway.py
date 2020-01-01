#Name:Himanshu Kumar
#Two way communication

import os
import sys
import time
import array
l=list()
n=input("enter how many numbers:")
str2="" 
for i in range(n):
	a=input()
	str2 = str2 + str(a) + " "
	
r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()
if pid==0:
	os.close(w)
	r = os.fdopen(r)
	print("Child Reading....")
	d=(r.read())
	r.close()
	print("Child reads :"+d)
	l1=d.split()
	for x in l1:
		y=int(x)
		l.append(y)
	prime=""
	notprime=""
	
	for i in range(n):
	        flag=0
	        if l[i]==1:
	            flag=1
		for j in range(2,l[i]):
			if l[i]%j==0:
				flag=1
				break
			
		if flag==0:
			prime=prime+str(l[i])+" "
	        		
	os.close(r1)
	print("Child is writing...")
	w1=os.fdopen(w1,'w')
	w1.write(prime)
	
else:
	os.close(r)
	print ("Parent writing....")
	w = os.fdopen(w,'w')
	w.write(str2)
	w.close()
	os.close(w1)
	r1=os.fdopen(r1)
	
	print("Parent reading...")
	str1=r1.read()
	#print(str1)
	print("Parents reads :"+str1)
	
	
'''Output:-
enter how many numbers:5
3
2
7
6
5
Parent writing....
Parent reading...
Child Reading....
Child reads :3 2 7 6 5 
Child is writing...
Parents reads :3 2 7 

'''
	
