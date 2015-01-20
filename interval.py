import sys
import numpy as np
from percentile import percentile

def interval():

     filename = sys.argv[1]

     x = np.load('Result1/Posterior/'+'f'+filename+'.npy') 
    
     N = len(x[0,:])     
 
     Irange = range(0, 201)
     
     Nr = len(Irange)

     res = np.zeros((Nr, N))
     for i in xrange(N):
       for j in Irange: 
         percentj = 0.005 * j
         res[j, i] = percentile(np.sort(x[:,i]), percentj)

     np.savetxt('Result1/Posterior/'+'P'+filename+'.dat', res, delimiter=' ')

if __name__ == '__main__':
    interval()
