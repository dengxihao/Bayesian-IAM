import numpy as np
from forecast import project

def sarlike(sPop, sGDP, sCO2, Nm, NC, A, Sigma):
##
## log likelihood of 3 dimensional scaled autoregression 
##

  xPop = sPop[1:Nm] - A[0] * sPop[0:(Nm-1)]
  xGDP = sGDP[1:Nm] - A[1] * sGDP[0:(Nm-1)]
  xCO2 = sCO2[1:NC] - A[2] * sCO2[0:(NC-1)]

  loglikP = -0.5 * np.sum(xPop**2/(Sigma[0]**2)) - (Nm-1) * np.log(Sigma[0])

  loglikG = -0.5 * np.sum(xGDP**2/(Sigma[1]**2)) - (Nm-1) * np.log(Sigma[1])
 
  loglikC = -0.5 * np.sum(xCO2**2/(Sigma[2]**2)) - (NC-1) * np.log(Sigma[2])

  loglik = loglikP + loglikG + loglikC

  return loglik

##################################################################################

def lnLklhd(t, t0, ind, dPop, dGDP, dCO2, par):

 parm = par[0:17]
 A = par[17:20]
 Sigma = par[20:23]
 SigmaP = par[23]
 SigmaG = par[24]

 fPop, fGDP, fCO2, Pop, GDP, CO2 = project(t, t0, ind, par)

 if sum(fCO2) >= 6000 or sum(CO2) >= 6000:
    loglike = -float("inf")
     
 else:
    Nm = len(dPop)
    NC = len(dCO2)

    Pop = Pop[0:Nm]
    GDP = GDP[0:Nm]
    CO2 = CO2[1:(NC+1)]

    sPop = np.log(dPop[6:Nm]) - np.log(Pop[6:Nm])
    sGDP = np.log(dGDP[6:Nm]) - np.log(GDP[6:Nm])
    sCO2 = np.log(dCO2) - np.log(CO2)

    loglike = sarlike(sPop, sGDP, sCO2, Nm-6, NC-6, A, Sigma) 
    WPop = dPop[0:6] - Pop[0:6]
    loglikePW = -0.5 * np.sum(WPop[0:6]**2/(SigmaP**2)) - 6 * np.log(SigmaP)
    WGDP = dGDP[0:6] - GDP[0:6]
    loglikeGW = -0.5 * np.sum(WGDP[0:6]**2/(SigmaG**2)) - 6 * np.log(SigmaG)
    loglike = loglike + loglikePW + loglikeGW

 return (loglike, fPop, fGDP, fCO2)



 
