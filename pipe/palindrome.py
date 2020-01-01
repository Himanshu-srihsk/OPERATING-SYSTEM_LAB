#HIMANSHU KUMAR
#PROGRAM - PALLINDROME OR NOT USING TWO WAY PIPE

import os,sys
r,w=os.pipe()
r1,w1=os.pipe()
pid=os.fork()
			
if pid>0:
	os.close(r)
	string=raw_input("enter the string : ")
	prnt=os.fdopen(w,"w")
	prnt.write(string)
	print("Parent writing : "+ string)

	os.close(w1)
	prnt=os.fdopen(r1)
	q= prnt.read()
	print("Parent Reading: " + q )
	sys.exit(0)

else:
	os.close(w)
	chld=os.fdopen(r)
	pr=chld.read()
	print("child reading : " + pr )

	os.close(r1)
	chld=os.fdopen(w1,"w")
	for i in range(0,len(pr)/2):
		if pr[i] !=pr[len(pr)-i-1]:
			result="not a pallindrome"
			break
			
		else:
			result="pallindrome "
	chld.write(result)
	print("child writing back : " + result)

	sys.exit(0)
	
	
'''				
OUTPUT:

12170032@csadmin-OptiPlex-3050:~/Desktop$ python palindrome.py
enter the string : hiamm
Parent writing : hiamm
child reading : hiamm
child writing back : not a pallindrome
Parent Reading: not a pallindrome
12170032@csadmin-OptiPlex-3050:~/Desktop$ python palindrome.py
enter the string : abcba
Parent writing : abcba
child reading : abcba
child writing back : pallindrome 
Parent Reading: pallindrome 

'''


		
