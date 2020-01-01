#SJf PREMPOTIVE
n = input("Enter number of processes : ")
process = []
ct = [0]*n
tat = []
wt = []

for i in range(n):
		process.append([])
	    	process[i].append(raw_input('Enter process id: '))
		process[i].append(input('Enter Arrival time: '))
    		process[i].append(input('Enter burst time: '))	
    		process[i].append(0)			
		print ''

process.sort(key=lambda process:process[1])	#to sort according to arrival time

                      
ct[0]=process[0][1]+process[0][2]
t_total=0
tcurr=0
burst=[]
for i in range(0,n):
   burst.append(process[i][2])
   t_total+=process[i][2]

l=0    					
for tcurr in range(0,t_total):
	       if(burst[l]>0 and process[l][1]<=tcurr):
	            burst[l]=burst[l]-1
	          
	       if(burst[l]<=0 and process[l][3]!=1):
	                process[l][3] = 1
			ct[l]=tcurr+1
		 
	       min_bt=999
	       for x in range(0,n):
	           if(process[x][1] <= (tcurr+1) and process[x][3] != 1):
				if(min_bt != burst[x]  and  min_bt > burst[x]):
					min_bt = burst[x]
					l=x
      
for i in range(n):			#to calculate tat and wt for each process
	tat.append(ct[i]-process[i][1])
	wt.append(tat[i]-process[i][2])
	
print "PID	AT      BT     CT     TAT      WT"
for i in range(n):
	print process[i][0],"\t",process[i][1],"\t",process[i][2],"\t",ct[i],"\t",tat[i],"\t",wt[i]



