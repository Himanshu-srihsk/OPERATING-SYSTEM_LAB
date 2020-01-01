#fcfs
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
for i in range(0,n):
   ct[i]=ct[i-1]+process[i][2]
      					

    
for i in range(n):			#to calculate tat and wt for each process
	tat.append(ct[i]-process[i][1])
	wt.append(tat[i]-process[i][2])
	
print "PID	AT      BT     CT     TAT      WT"
for i in range(n):
	print process[i][0],"\t",process[i][1],"\t",process[i][2],"\t",ct[i],"\t",tat[i],"\t",wt[i]



