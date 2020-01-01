#Round Robin Himanshu
class process:
    def __init__(self, bt=0,at=0,prt=0,wt=0,tat=0,flag=0,name='',val=0):
          self.bt = bt
          self.at = at
          self.prt=prt
          self.name =name
          self.tat=tat
          self.wt=wt
          self.flag=flag
          self.val=val
     
    def processdata(self,name,bt,at,val):
          self.bt = bt
          self.at = at
          #self.prt=prt
          self.name =name
          self.val=val
    
def b_sort(temp,n):
          t=process()
          for i in range(0,n):
              for j in range(0,n-i-1):
                  if temp[j].at > temp[j+1].at :
                        t=temp[j]
                        temp[j]=temp[j+1]
                        temp[j+1]=t
     
def roundrobin(p,n):
         print('ROUND ROBIN\n')
         temp1= [process() for i in range(20)]
         
         for f in range(0,n):
            p[f].flag=0
         
         t_total=0
   
         for i in range(0,n):
             temp1[i]=p[i]
             t_total+=temp1[i].bt
             
         b_sort(temp1,n)
     
         print('\n proc Bt AT\n')
         for i in range(0,n):
             print(temp1[i].name,temp1[i].bt,temp1[i].at)
             
         
         b=[0]*n
         for i in range(0,n):
		b[i] = temp1[i].bt  
	
	 print(b)
	 
     	
	 l=0
	 m=0	
	 g=[]
	 print("GANTTT CHART")
	 g.append(l)
	 
	 
	 sumw,sumt=0,0
	 tcurr=temp1[0].at
	 #tq=2
	 tq=int(input('enter Time quantum:'))
	 ready_queue=[]
	 check=0
	 ready_queue.append(0)
	 while(tcurr<t_total+temp1[0].at):
	    l=ready_queue.pop(0)
	    if(b[l]>0 and temp1[l].at<=tcurr):	            
	       w=b[l]
	       b[l]=b[l]-tq
	       if(b[l]<0):
	               b[l]=0
	               tcurr=tcurr+w
	                 
	       else:
	               tcurr=tcurr+tq
	                        
	       
	       #print(tcurr,temp1[l].name)
	       g.append(temp1[l].name)
	       g.append(tcurr)
	          
	       if(b[l]<=0 and temp1[l].flag!=1):
	                temp1[l].flag = 1
			temp1[l].wt = (tcurr) - temp1[l].bt - temp1[l].at
			temp1[l].tat = (tcurr) - temp1[l].at
			sumw+=temp1[l].wt
			sumt+=temp1[l].tat
	       
	       m=l
	       for i in range(0,n):
	                if(temp1[i].flag !=1  and temp1[i].at<=tcurr and (i not in ready_queue) and i!=l):
	                           ready_queue.append(i) 
	     
	       if(temp1[l].flag !=1):
	             ready_queue.append(l)
	             
	    else:
	         tcurr+=1 
	         ready_queue.append(temp1[0].val)
	    """                 		
	    print('tcurr= {}'.format(tcurr))
	    print('ready_queue = {}'.format(ready_queue))
	    for i in range(0,n):
	       print(b[i]),
	    print('\n')   
	    for i in range(0,n):
	       print(temp1[i].flag),  
	    print('\n')    
	    """		
	  	
	 avgwt = float(sumw)/float(n)
         avgta = float(sumt)/float(n)
         
         print(g)
         
         print('\n proc Bt AT WT TAT CT\n')
         k=0
         for i in range(0,n):
               m=[]
               m.append(temp1[i].name)
               m.append(temp1[i].bt)
               m.append(temp1[i].at)
               m.append(temp1[i].wt)
               m.append(temp1[i].tat)
               g=temp1[i].bt + k
               m.append(g)
               k=g
               print(m)
              
	 print('Average WT{} and Average TAT{}'.format(avgwt,avgta))             	
		       
         
def main():
    p = [process() for i in range(20)]
    n=int(input('enter no of process'))
    k=[]
    l=[]
    z=[]
    print('enter name of process all of {} process '.format(n))
    k=list(raw_input().split())
    print('enter Burst time all of {} process '.format(n))
    l=list(map(int,raw_input().split()))
    print('enter Arrival time all of {} process '.format(n))
    z=list(map(int,raw_input().split()))
    y=[]
    for i in range(0,n):
        y.append(i)
    
  
    for i in range(0,n):
       p[i].processdata(k[i],l[i],z[i],y[i])
    
    m=["Select An Option: \n1.SJF PREMPTIVE\n"]   
    print(m)
    roundrobin(p,n)
    
main()         


"""
himanshu@himanshu-VirtualBox:~/Desktop$ python rrhim.py
enter no of process6
enter name of process all of 6 process 
p1 p2 p3 p4 p5 p6
enter Burst time all of 6 process 
5 6 7 9 2 3
enter Arrival time all of 6 process 
5 4 3 1 2 6
['Select An Option: \n1.SJF PREMPTIVE\n']
SJF PREMPTIVE


 proc Bt AT

('p4', 9, 1)
('p5', 2, 2)
('p3', 7, 3)
('p2', 6, 4)
('p1', 5, 5)
('p6', 3, 6)
[9, 2, 7, 6, 5, 3]
3 4 2 1 0 5 

GANTTT CHART
enter Time quantum:3
[0, 'p4', 4, 'p5', 6, 'p3', 9, 'p2', 12, 'p4', 15, 'p1', 18, 'p6', 21, 'p3', 24, 'p2', 27, 'p4', 30, 'p1', 32, 'p3', 33]

 proc Bt AT WT TAT

['p4', 9, 1, 20, 29]
['p5', 2, 2, 2, 4]
['p3', 7, 3, 23, 30]
['p2', 6, 4, 17, 23]
['p1', 5, 5, 22, 27]
['p6', 3, 6, 12, 15]
Average WT16.0 and Average TAT21.3333333333
"""

          
          
          
    
 
        


