#GAUSS JORDAN ELEMINIATI
import numpy as np
from sympy import *

row=int(input("rows"))
col=int(input('cols'))
arr=np.zeros((row,col),float) #creates array with zero entry as # numpy.zeros(shape, dtype=float, order='C', *, like=None); (r,c)=shapes 2d array
# arr[1:2]=5 .... #starts like 0,1,2... rows and 0,1,2... cols so, in reality its selecting  2nd row and 3rd column
print(arr)

n= input("n")
arr[2:3]=n
print(arr)

'''
for r in arr:
   for c in r:
      arr[r:c]=input("enter thevalue of") 
      print(r,c)
   print()
'''
"""
for r in arr:
     j = 0 
     for j in range(0,z2):
         y[i,j]=input()
     print(y[i,j])


 
y[1,1]=5
print(y)
"""
