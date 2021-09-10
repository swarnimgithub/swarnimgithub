#GAUSS JORDAN ELEMINIATION
import numpy as np
from sympy import *

#row=int(input("rows"))
#col=int(input('cols'))
#arr=np.zeros((row,col),float) #creates array with zero entry as # numpy.zeros(shape, dtype=float, order='C', *, like=None); (r,c)=shapes 2d array
# arr[1:2]=5 .... #starts like 0,1,2... rows and 0,1,2... cols so, in reality its selecting  2nd row and 3rd column
#print(arr)

def matrix_maker(row,col):
 arr=np.zeros((row,col),float)
 for r in range(row):
     for c in range(col):
        n=0
        n= input('{}th row and  {}th coloumn'.format(r+1, c+1))
        arr[r,c]=n
       #print(r,c)
 return(arr)





if __name__=='__main__':
  row=int(input("rows"))
  col=int(input('cols')) 
  arr=np.zeros((row,col),float)
  array = matrix_maker(row,col)
  print(array)
