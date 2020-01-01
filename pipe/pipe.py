#one way communication Himanshu

import os 

def communication(parent_writes): 
	r, w = os.pipe() 
	processid=os.fork()
	if processid:
		os.close(r) 
		w = os.fdopen(w, 'w') 
		print ("parent writing") 
		w.write(parent_writes) 
		print("parent writes = ",parent_writes) 
		w.close()
	else:
		os.close(w) 
		r = os.fdopen(r) 
		print ("child reading") 
		str = r.read() 
		print( "child reads =" ,str)


parent_writes=''
n=input("enter how many numbers")
for i in range(n):
  a=input("enter number")
  parent_writes=parent_writes+str(a)+' '
 
communication(parent_writes)

"""
OUTPUT:-
 enter how many numbers5
enter number2
enter number6
enter number7
enter number9
enter number8
parent writing
('parent writes = ', '2 6 7 9 8 ')
child reading
('child reads =', '2 6 7 9 8 ')

"""
