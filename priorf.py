import sys
import numpy as np
from forecast import project
from Input import t1, t0, ind

def priorf():

    foldername = 'Result' + sys.argv[1] + '/Prior/'

    samps = np.load(foldername + 'samps.npy')

    N = len(samps)

    Nm = len(ind) + 1
    Nc = len(t1) + 1

    fPop = np.zeros((N, Nm))
    fGDP = np.zeros((N, Nm))
    fCO2 = np.zeros((N, Nc))    
       
    for i in xrange(N):
     fPopi, fGDPi, fCO2i, Pop, GDP, CO2 = project(t1, t0, ind, samps[i, :])
     if sum(fCO2i) < 6000 and sum(CO2) < 6000:
      fPop[i, :] = fPopi
      fGDP[i, :] = fGDPi
      fCO2[i, :] = fCO2i
     
    indC = np.flatnonzero(np.sum(fCO2, axis=1))     
    
    fPop = fPop[indC, :]
    fGDP = fGDP[indC, :]
    fCO2 = fCO2[indC, :]

    samps = samps[indC, :]    

    np.save(foldername+'fPop', fPop)
    np.save(foldername+'fGDP', fGDP)
    np.save(foldername+'fCO2', fCO2)
    np.save(foldername+'samps', samps)

if __name__ == '__main__':
     priorf() 
