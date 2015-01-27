from Prior import lnpdf
import numpy as np
np.seterr(all='ignore')
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import multiprocessing
from mcmc import mh
from Input import t1, t0, ind, dPop, dGDP, dCO2, kappa, parb


def main(): 
##
## main function generates mcmc samples
##

    # initial parameters
      par0=np.loadtxt('parm1.txt')      
    
    # size of samples, burn-in and thin-in
      Nsamp = 5000000
      Nburn = 100000
      Nthin = 1000        
    
    # parallel generating 10 mcmc chains            
      res = Parallel(n_jobs=10)(delayed(mh)(Nsamp, Nburn, Nthin, t1, t0, ind, dPop, dGDP, dCO2, parb, kappa, par0) for i in range(10))  

      samps, fPop, fGDP, fCO2, accept = zip(*res)  
  
      print accept
                   
      for j in range(10):
        np.save("temp/samp" + str(j+1), samps[j])
        np.save("temp/fPops" + str(j+1), fPop[j])
        np.save("temp/fGDPs" + str(j+1), fGDP[j])
        np.save("temp/fCO2s" + str(j+1), fCO2[j])

if __name__ == '__main__':
    main()
