#PRIORITY NON PREMPTIVE HIMANSHU
class process:
    def __init__(self, bt=0,at=0,prt=0,wt=0,tat=0,flag=0,name=''):
          self.bt = bt
          self.at = at
          self.prt=prt
          self.name =name
          self.tat=tat
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
     
def prioritynon(p,n):
         print('PRIORITY NON PREMPTIVE\n')
         temp1= [process() for i in range(20)]
         for i in range(0,n):
             #temp1[i]=process()
             temp1[i]=p[i]
         b_sort(temp1,n)
         
         for i in range(0,n):
             for j in range(1,n-i-1):
                 if temp1[j].prt > temp1[j+1].prt:
                      t=temp1[j]
                      temp1[j]=temp1[j+1]
                      temp1[j+1]=t
		
         
         print('\n proc Bt AT\n')
         for i in range(0,n):
             print(temp1[i].name,temp1[i].bt,temp1[i].at)
		

         sumw = temp1[0].wt = 0
	 sumt = temp1[0].tat = temp1[0].bt - temp1[0].at
	 for i in range(1,n):
			temp1[i].wt = (temp1[i-1].bt + temp1[i-1].at + temp1[i-1].wt) - temp1[i].at
			temp1[i].tat = (temp1[i].wt + temp1[i].bt)
			sumw+=temp1[i].wt
			sumt+=temp1[i].tat
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
               g=temp1[i].bt + k
               m.append(g)
               k=g
               print(m)
              
	       
	 print('Average WT{} and Average TAT{}'.format(avgwt,avgta))     
         print("\nGANTT CHART\n ")
		
         print("0"),
         x=0
         for i in range(1,n+1):
                     
			x+=temp1[i-1].bt;
			#print(x)
			print('%s'%temp1[i-1].name),
			print('%d'%x),
         
def main():
    p = [process() for i in range(20)]
    #p=[]
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
       #k=raw_input('name of process')
       #l=int(input('burst time'))
       #z=int(input('arrival time'))
       #p[i]=process()
       p[i].processdata(k[i],l[i],z[i],v[i])
    
    m=["Select An Option: \n1.PRIORITY NON PREMPTIVE\n"]   
    print(m)
    prioritynon(p,n)
    
main()         


          
          
          
    
 
        


