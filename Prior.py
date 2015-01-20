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

    indN = np.array([2, 6, 7, 8, 15])
#    indN = np.array([6, 8, 15])
#    indN = np.array([6, 7, 8, 15])  

    lnptau = 0 
    if par[12] >= par[13] or par[13] >= par[14]:
        lnptau = -float("inf")

    lnprho2 = 0
    if par[10] < par[11]: 
        lnprho2 = -float("inf")

    meanN = (parb[indN, 0] + parb[indN, 1])/2

    varN = ((parb[indN, 1] - parb[indN, 0])/4)**2

    lnpN = -0.5 * np.sum((par[indN] - meanN)**2/varN)

    lnpe = lnptau + lnprho2

    # log normal prior for rho2
#    mlogrho2 = np.log(3/(parb[10, 1] - parb[10, 0])) 
#    sdlogrho2 = 0.5
#    lnrho2 = -np.log(par[10]) - (np.log(par[10]) - mlogrho2)**2/0.5

   
    lnp = logunipdf(par, parb) + lnpe + lnpN - np.log(par[23]) \
          - np.log(par[24]) #+ lnrho2

    return lnp

##############################################################################

def lnpdf(t, t0, ind, dPop, dGDP, dCO2, parb, par):
##
## log posterior distribution
##

   loglike, fPop, fGDP, fCO2 = lnLklhd(t, t0, ind, dPop, dGDP, dCO2, par)
   lnp = lnPrior(parb, par)
   lnposter = loglike + lnp
   
   return (lnposter, fPop, fGDP, fCO2)

