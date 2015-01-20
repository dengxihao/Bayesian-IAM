import numpy as np
from forecast import project
from Input import t1, t0, ind

def bestfit():

   x =  np.loadtxt('parm2.txt')
 
   fPop, fGDP, fCO2, mPop, mGDP, mCO2 = project(t1, t0, ind, x)

   np.savetxt('Result1/Posterior/mPop.dat', mPop, delimiter=' ')
   np.savetxt('Result1/Posterior/mGDP.dat', mGDP, delimiter=' ')
   np.savetxt('Result1/Posterior/mCO2.dat', mCO2, delimiter=' ')



if __name__ == '__main__':
     bestfit() 
