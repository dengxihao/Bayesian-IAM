from Prior import lnpdf
import numpy as np
from math import pi as PI

def proprnd(parb, kappa, par0):
##
## proposal distribution
##
## Inputs: parb --- parameter bounds
##         par0 --- initial parameters
##         kappa --- step size 
##
## Output: par --- proposed next step parameters
##

    np.random.seed(None)  
 
   # random generation of cauchy distribution 
    Y = -PI/2 + PI * np.random.rand(len(par0))
    par = kappa * np.tan(Y) + par0    
 
   # parameters modulo the bounds
    par = -(parb[:,1]-parb[:,0]) * np.floor((par-parb[:,0])/(parb[:,1]-parb[:,0])) + par

    return par

###########################################################################################

def mh(nSamps, nburn, nthin, t, t0, ind, dPop, dGDP, dCO2, parb, kappa, par0):
##
## metropolis-hasting sampling
##
## Inputs: nSamps --- number of total samples
##          nburn --- burn-in number
##          nthin --- thin-in number
##              t --- the observation time vector of carbon emission
##             t0 --- initial observational time of population
##            ind --- the indices of population observation times in carbon
##                    emission observation time vector
##           dPop --- observations of population
##           dGDP --- observations of GWP
##           dCO2 --- observations of carbon emission
##           parb --- parameter bounds
##          kappa --- step sizes of mcmc sampling
##           par0 --- initial parameters
##
## Output: samps --- parameter samples
##          fPop --- population forecast samples
##          fGDP --- GWP forecast samples
##          fCO2 --- carbon emission forecast samples
##        accept --- acceptance rate       
##

  # size of output samples
   NSamps = (nSamps - nburn - 1)/nthin + 1

  # pre-allocation
   samps = np.zeros((NSamps, len(par0)))
   fPop = np.zeros((NSamps, len(ind)+1))
   fGDP = np.zeros((NSamps, len(ind)+1))
   fCO2 = np.zeros((NSamps, len(t)+1))
   accept = 0.0
       
   np.random.seed(None)     

  # loop
   lnpdfx, fPop0, fGDP0, fCO20 = lnpdf(t, t0, ind, dPop, dGDP, dCO2, parb, par0)
   for kSamp in xrange(nSamps):
     par1 = proprnd(parb, kappa, par0)
     lnpdfy, fPop1, fGDP1, fCO21 = lnpdf(t, t0, ind, dPop, dGDP, dCO2, parb, par1)
     dE = min((lnpdfy - lnpdfx), 0)
     if np.log(np.random.rand()) < dE:
       par0 = par1
       fPop0 = fPop1
       fGDP0 = fGDP1
       fCO20 = fCO21
       lnpdfx = lnpdfy
        
       if kSamp > (nburn-1):
         accept = accept + 1
        
     if kSamp > (nburn-1) and (kSamp - nburn + 1) % nthin == 1:
       iSamp = (kSamp-nburn)/nthin
       samps[iSamp, :] = par0
       fPop[iSamp, :] = fPop0
       fGDP[iSamp, :] = fGDP0
       fCO2[iSamp, :] = fCO20
               
   accept = accept/(nSamps-nburn)

   return (samps, fPop, fGDP, fCO2, accept)                
                      








