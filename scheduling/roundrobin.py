#ROUND ROBIN

class process:
    def __init__(self, bt=0,at=0,prt=0,wt=0,tat=0,flag=0,name=''):
          self.bt = bt
          self.at = at
          self.prt=prt
          self.name =name
          self.tat=tat
          self.wt=wt
          self.flag=flag
     
    def processdata(self,name,bt,at):
          self.bt = bt
          self.at = at
          #self.prt=prt
          self.name =name
    
def b_sort(temp,n):
          t=process()
          for i in range(0,n):
              for j in range(0,n-i-1):
                  if temp[j].at > temp[j+1].at :
                        t=temp[j]
                        temp[j]=temp[j+1]
                        temp[j+1]=t
     
def roundrobin(p,n):
         print('round robin\n')
         temp1= [process() for i in range(20)]
         temp2=[process() for i in range(20)]
         for f in range(0,n):
            p[f].flag=0
            
         for i in range(0,n):
             temp1[i]=p[i]
         
         
         for i in range(0,n):
             temp2[i]=p[i]
                 
         b=[0]*n
         for i in range(0,n):
		b[i] = p[i].bt  
		    
         b_sort(temp1,n)
     
         print('\n proc Bt AT\n')
         for i in range(0,n):
             print(temp1[i].name,temp1[i].bt,temp1[i].at)
		
         
        
	   
         
         tq=input("enter the time Quantum:")
         
         print('Time Quantum:',tq)
         print('gant chart')
         
         
         tcurr=0
         sumw,sumt=0,0
         k=0
         pflag=0
         k=0
         while(k>=0):
		if(k>n-1):
			k=0
			
		if(temp1[k].bt>0):
		        print('%d'%tcurr),
		        print('%s'%temp1[k].name),
			
		t=0
		while(t<tq and temp1[k].bt > 0):
			t=t+1
			tcurr+=1
			temp1[k].bt-=1
		        
	        if(temp1[k].bt <= 0 and temp1[k].flag != 1):
			temp1[k].wt = tcurr - b[k]- temp1[k].at;
			temp1[k].tat = tcurr - temp1[k].at
			pflag+=1
			temp1[k].flag = 1
			sumw+=temp1[k].wt                                             
			sumt+=temp1[k].tat
		
		
                if(pflag==n):
                        break
                k+=1 
	
         
         
         
         
         print(tcurr)
         
         for i in range(0,n):
             temp1[i].bt=b[i]
     
	 avgwt = float(sumw)/float(n)
         avgta = float(sumt)/float(n)
         print('\n proc Bt AT WT TAT CT\n')
         k=0
         for i in range(0,n):
               m=[]
               m.append(temp1[i].name)
               m.append(temp1[i].bt)
               m.append(temp1[i].at)
               m.append(temp1[i].wt)
               m.append(temp1[i].tat)
               m.append(temp1[i].tat+temp1[i].at)
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
    
    
    for i in range(0,n):
       p[i].processdata(k[i],l[i],z[i])
    
    m=["Select An Option: \n1.ROUND ROBIN\n"]   
    print(m)
    roundrobin(p,n)
    
main()         


"""
enter no of process5
enter name of process all of 5 process 
p0 p1 p2 p3 p4
enter Burst time all of 5 process 
5 3 1 2 3
enter Arrival time all of 5 process 
0 1 2 3 4
['Select An Option: \n1.ROUND ROBIN\n']
round robin


 proc Bt AT

('p0', 5, 0)
('p1', 3, 1)
('p2', 1, 2)
('p3', 2, 3)
('p4', 3, 4)
enter the time Quantum:2
('Time Quantum:', 2)
gant chart
0 p0 2 p1 4 p2 5 p3 7 p4 9 p0 11 p1 12 p4 13 p0 14

 proc Bt AT WT TAT CT

['p0', 5, 0, 9, 14, 14]
['p1', 3, 1, 8, 11, 12]
['p2', 1, 2, 2, 3, 5]
['p3', 2, 3, 2, 4, 7]
['p4', 3, 4, 6, 9, 13]
Average WT5.4 and Average TAT8.2
himanshu@himanshu-VirtualBox:~/Downloads$ 
""""          
          
          
    
 
        


