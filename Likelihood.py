import numpy as np
from forecast import project

def sarlike(sPop, sGDP, sCO2, Nm, NC, A, Sigma):
##
## log likelihood of 3 AR processes
##
## Inputs: sPop --- AR series of population
##         sGDP --- AR series of GWP
##         sCO2 --- AR series of carbon emission
##           Nm --- length of AR series of population
##           NC --- length of AR series of carbon emission
##            A --- vector of three AR coefficients
##        Sigma --- vector of three AR error standard deviation 
##
## Output: loglik --- log likelihood
##

  # AR errors
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
##
## log likelihood function
##
## Inputs: t --- the observation time vector of carbon emission
##         t0 --- initial observational time of population
##         ind --- the indices of population observation times in carbon
##                 emission observation time vector
##         dPop --- observations of population
##         dGDP --- observations of GWP
##         dCO2 --- observations of carbon emission
##         par --- parameter set described in macro.py, emit.py and 
##                 AR parameters
##
## Output: loglike --- log likelihood
##         fPop --- forecast of population
##         fGDP --- forecast of GWP
##         fCO2 --- forecast of carbon emission
##

 parm = par[0:17]
 A = par[17:20]
 Sigma = par[20:23]
 SigmaP = par[23]
 SigmaG = par[24]

 # forecasts 
 fPop, fGDP, fCO2, Pop, GDP, CO2 = project(t, t0, ind, par)

 # limit of total carbon emission less than 6000 G tons
 if sum(fCO2) >= 6000 or sum(CO2) >= 6000:
    loglike = -float("inf")
     
 else:
    Nm = len(dPop)
    NC = len(dCO2)

    Pop = Pop[0:Nm]
    GDP = GDP[0:Nm]
    CO2 = CO2[1:(NC+1)]

   # difference of log observations and log long trend model (AR residuals)
    sPop = np.log(dPop[6:Nm]) - np.log(Pop[6:Nm])
    sGDP = np.log(dGDP[6:Nm]) - np.log(GDP[6:Nm])
    sCO2 = np.log(dCO2) - np.log(CO2)

    loglike = sarlike(sPop, sGDP, sCO2, Nm-6, NC-6, A, Sigma) 
    WPop = dPop[0:6] - Pop[0:6]         # residual of sparse population observations
    loglikePW = -0.5 * np.sum(WPop[0:6]**2/(SigmaP**2)) - 6 * np.log(SigmaP)
    WGDP = dGDP[0:6] - GDP[0:6]         # residual of sparse GWP observations
    loglikeGW = -0.5 * np.sum(WGDP[0:6]**2/(SigmaG**2)) - 6 * np.log(SigmaG)
    loglike = loglike + loglikePW + loglikeGW

 return (loglike, fPop, fGDP, fCO2)



 
