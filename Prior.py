import numpy as np
from Likelihood import lnLklhd

def logunipdf(x, xb):
##
## log probability density function of uniform distribution of vector x
## xb[:, 0] -- lower bound of x; xb[:, 1] -- upper bound of x
##
    Z = np.sum(np.log(xb[:,1] - xb[:,0]))

    if np.prod(np.greater(x, xb[:, 0])) and np.prod(np.less(x, xb[:, 1])):
       
        lnunipdf = - Z
 
    else:
   
       lnunipdf = -float("inf")

    return lnunipdf

#############################################################################

def lnPrior(parb, par):
##
## log prior distribution
##
## Inputs: parb --- parb[:,0] lower bound and parb[:,1] upper bound
##          par --- model and residual parameters
##

#   phi1 = par[0]
#   phi2 = par[1]
#   phi3 = par[2]
#   alpha = par[3]
#   As = par[4]
#   delta = par[5]
#   s = par[6]
#   lam = par[7]
#   pi = par[8]
#   coconst = par[9:15]
#   kappa = par[9]
#   rho2 = par[10]
#   rho3 = par[11]
#   tau2 = par[12]
#   tau3 = par[13]
#   tau4 = par[14]   
#   P0 = par[15]
#   A0 = par[16]

  # indices of the parameters with Gaussian priors
    indN = np.array([2, 6, 7, 8, 15])   

  # half saturation time constraints: technology 2 < 3 < 4
    lnptau = 0 
    if par[12] >= par[13] or par[13] >= par[14]:
        lnptau = -float("inf")
              
  # carbon intensity constraints: technology 2 > 3
    lnprho2 = 0
    if par[10] < par[11]: 
        lnprho2 = -float("inf")

  # mean and variance of Gaussian priors
    meanN = (parb[indN, 0] + parb[indN, 1])/2
    varN = ((parb[indN, 1] - parb[indN, 0])/4)**2

  # log Gaussian prior
    lnpN = -0.5 * np.sum((par[indN] - meanN)**2/varN)

    lnpe = lnptau + lnprho2
         
  # log prior, last two terms are log Jeffreys priors of standard deviations 
  # of population and GWP sparse data
    lnp = logunipdf(par, parb) + lnpe + lnpN \
          - np.log(par[23]) - np.log(par[24])  

    return lnp

##############################################################################

def lnpdf(t, t0, ind, dPop, dGDP, dCO2, parb, par):
##
## log posterior distribution
##
## Inputs: t --- the observation time vector of carbon emission
##         t0 --- initial observational time of population
##         ind --- the indices of population observation times in carbon
##                 emission observation time vector
##         dPop --- observations of population
##         dGDP --- observations of GWP
##         dCO2 --- observations of carbon emission
##         parb --- parameter bounds
##         par --- parameter set described in macro.py, emit.py and 
##                 AR parameters
##
## Output: lnposter --- log posterior
##         fPop --- forecast of population
##         fGDP --- forecast of GWP
##         fCO2 --- forecast of carbon emission
##

   loglike, fPop, fGDP, fCO2 = lnLklhd(t, t0, ind, dPop, dGDP, dCO2, par)
   lnp = lnPrior(parb, par)
   lnposter = loglike + lnp
   
   return (lnposter, fPop, fGDP, fCO2)

