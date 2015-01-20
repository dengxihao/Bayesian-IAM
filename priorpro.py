import sys
import numpy as np
from forecast import project
from scipy.stats import uniform
from scipy.stats import truncnorm
from Input import parb

def priorpro():
 
    foldername = sys.argv[1]

    if int(foldername) == 1:
      indN = np.array([2, 6, 7, 8, 15])
    else:  
      indN = np.array([6, 8, 15]) 
      
    np.random.seed(None)  

    Ns = 50000

    samps = np.zeros((Ns, 25))  

    for i in xrange(25): 
        
      if i in indN:
        mui = (parb[i, 0] + parb[i, 1])/2
        stdi = (parb[i, 1] - parb[i, 0])/4
        ai = (parb[i, 0] - mui) / stdi
        bi = (parb[i, 1] - mui) / stdi
        xi = truncnorm.rvs(ai, bi, size=Ns)
        samps[:, i] = mui + stdi * xi   
      elif i==23 or i==24:
        samps[:, i] = np.exp(np.random.uniform(parb[i, 0], parb[i, 1], Ns))
      elif i == 10 and int(foldername) == 2:
        mlogrho2 = np.log(3/(parb[i, 1] - parb[i, 0])) 
        samps[:, i] = np.random.lognormal(mlogrho2, 0.5, Ns)
      elif i == 11:
        samps[:, i] = np.random.uniform(parb[i, 0], np.minimum(samps[:,i-1], parb[i,1]), Ns)
      elif i==13 or i==14:
        samps[:,i] = np.random.uniform(np.maximum(samps[:,i-1], parb[i,0]), parb[i,1], Ns)
      else:
        samps[:, i] = np.random.uniform(parb[i, 0], parb[i, 1], Ns)
       
        
      filename = 'Result' + foldername + '/Prior/samps'  
       
      np.save(filename, samps) 


if __name__ == '__main__':
    priorpro()

