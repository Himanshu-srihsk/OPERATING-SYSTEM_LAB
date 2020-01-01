#PRIORITY PREMPTIVE  HIMANSHU
class process:
    def __init__(self, bt=0,at=0,prt=0,wt=0,tat=0,flag=0,name=''):
          self.bt = bt
          self.at = at
          self.prt=prt
          self.name =name
          self.tat=tat
          self.wt=wt
          self.flag=flag
     
    def processdata(self,name,bt,at,prt):
          self.bt = bt
          self.at = at
          self.prt=prt
          self.name =name
    
def b_sort(temp,n):
          t=process()
          for i in range(0,n):
              for j in range(0,n-i-1):
                  if temp[j].at > temp[j+1].at :
                        t=temp[j]
                        temp[j]=temp[j+1]
                        temp[j+1]=t
     
def priorityprem(p,n):
         print('priority PREMPTIVE\n')
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
	 #print(l,temp1[l].name),
	 g.append(l)
	 g.append(temp1[l].name)
	 #print(temp[1].name)
	 
	 sumw,sumt=0,0
	 tcurr=0
	 for tcurr in range(0,t_total):
	       if(b[l]>0 and temp1[l].at<=tcurr):
	            b[l]=b[l]-1
	            
	       if(l!=m):
	          #print(tcurr,temp1[l].name),
	          g.append(tcurr)
	          g.append(temp1[l].name)
	          
	       if(b[l]<=0 and temp1[l].flag!=1):
	                temp1[l].flag = 1
			temp1[l].wt = (tcurr+1) - temp1[l].bt - temp1[l].at
			temp1[l].tat = (tcurr+1) - temp1[l].at
			sumw+=temp1[l].wt
			sumt+=temp1[l].tat
	       m=l	 
	       min_pr=999
	       for x in range(0,n):
	           if(temp1[x].at <= (tcurr+1) and temp1[x].flag != 1):
				if(min_pr != temp1[x].prt  and  min_pr > temp1[x].prt):
					min_pr = temp1[x].prt
					l=x
				
	
			
	 g.append(tcurr+1)     	
	 avgwt = float(sumw)/float(n)
         avgta = float(sumt)/float(n)
         print('\n proc Bt AT WT TAT\n')
         k=0
         for i in range(0,n):
               m=[]
               m.append(temp1[i].name)
               m.append(temp1[i].bt)
               m.append(temp1[i].at)
               m.append(temp1[i].wt)
               m.append(temp1[i].tat)
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
    print('enter priority all of {} process '.format(n))
    v=list(map(int,raw_input().split()))
    
    
    for i in range(0,n):
       p[i].processdata(k[i],l[i],z[i],v[i])
    
    m=["Select An Option: \n1.priority PREMPTIVE\n"]   
    print(m)
    priorityprem(p,n)
    
main()         


          
          
          
    
 
        


