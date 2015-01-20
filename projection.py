import sys
import numpy as np

def projection():
  
  foldname = sys.argv[1] 
  
  subfold = sys.argv[2]

  filename = sys.argv[3]

  x = np.load('Result'+foldname+'/'+subfold+'/f'+filename+'.npy') 
    
  N = len(x[0, :])   
      
  res = x[:, [N-101, N-51, N-1]]     

  np.savetxt('Result'+foldname+'/Posterior/'+'Pr'+filename+'.dat', res, delimiter=' ')

if __name__ == '__main__':
    projection()
