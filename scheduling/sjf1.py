#SJF NON PREMPOTIVE
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
tcurr=ct[0]
process[0][3]=1
for i in range(0,n):
     min_bt=99999
     l=i
     for j in range(0,n):
	           if(process[j][1] <= (tcurr) and process[j][3] != 1):
				if(min_bt != process[j][2]  and  min_bt > process[j][2]):
					min_bt = process[j][2]
					l=j 
     process[l][3]=1					
     ct[l]=tcurr+process[l][2]
     tcurr=ct[l]
      					

  
    
for i in range(n):			#to calculate tat and wt for each process
	tat.append(ct[i]-process[i][1])
	wt.append(tat[i]-process[i][2])
	
print "PID	AT      BT     CT     TAT      WT"
for i in range(n):
	print process[i][0],"\t",process[i][1],"\t",process[i][2],"\t",ct[i],"\t",tat[i],"\t",wt[i]



