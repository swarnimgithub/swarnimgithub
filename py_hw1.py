#Question2 
import numpy as np
from scipy.integrate import quad

def intervalsize(a,b,N):
    h = (b-a)/N
    return h
    
def x_vals(a,b,h):
    list1=[]
    list1.append(a)
    for i in range(N):
        a = a + h
        list1.append(a)
    return list1
    
def y_vals(list1):
    list2=[]
    for i in (list1):
          y = i**2
          list2.append(y)
    return list2      
    

########################################

def simpson(list2,h,N) :
   
   z2=0
   z3=0
   simp_val=0 
   
   if N%2==0 and N%3!=0:
      	for i in range(1,len(list2)):
        	z1=list2[0]+list2[-1]
        	if i%2==0:
          		z2=z2+list2[i]
        	else:
           		z3=z3+list2[i]
      	simp_val= h/3 * (z1 + (4 * (z3)) + (2 * (z2)))
   else:
      	print("can't bro")
      	simp_val = None 
   return simp_val
   




#################################################

def trap(list2,h):
  z2 = 0
  z1=list2[0]+list2[-1]
  for i in range(1,len(list2)):
  	     z2= z2+ list2[i]
  tramp= h/2*(z1+2*z2)
  return tramp

##################################################
#USING SCIPY




##################################################
if __name__ == "__main__":
  a=float(input("enter the lower limit"))
  b=float(input("enter the upper limit"))
  N=int(input("enter the number of intervals"))
  h=intervalsize(a,b,N)
  list1= x_vals(a,b,h)
  list2= y_vals(list1)
  Simpson = simpson(list2,h,N)
  trapezodial = trap(list2,h)
  z1=list2[0]+list2[-1]
  print(list1)
  print(list2)
  print(list2[-1])
  print(Simpson)
  print(trapezodial)
 
