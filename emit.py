import numpy as np
import macro

def logpc(kappat, kappatau):
##
## a generic function to compute the logistic penetration curve
##
   
     logit = 1/(1 + np.exp(-kappat + kappatau))

     return logit

###################################################################

def co2(P0, Q0, A0, K0, t, gdpconst, coconst):
##
## computing CO2 emmission time series by Eq. (9)-(14) in keller07
##
## Inputs: P0 --- initial population
##         Q0 --- initial GWP
##         A0 --- initial total factor productivity
##         K0 --- initial capital stock
##          t --- observation time vector
##         gdpconst = [phi1, phi2, phi3, alpha, As, delta, s, lam, pi]
##         coconst = [kappa, rho2, rho3, tau2, tau3, tau4]
##
## Output: Output --- population, GWP and carbon time series
##         Output[:,0] --- population time series
##         Output[:,1] --- GWP time series
##         Output[:,2] --- carbon emission time series
##
    
     kappa = coconst[0]            # technological penetration rate
     rho2 = coconst[1]             # carbon intensity of technology 2
     rho3 = coconst[2]             # carbon intensity of technology 3
     tau2 = coconst[3]             # half saturation time of technology 2
     tau3 = coconst[4]             # half saturation time of technology 3
     tau4 = coconst[5]             # half saturation time of technology 4

     kappat = kappa * t
     kappa2 = kappa * tau2
     kappa3 = kappa * tau3
     kappa4 = kappa * tau4

     logpc2 = logpc(kappat, kappa2)
     logpc3 = logpc(kappat, kappa3)
     logpc4 = logpc(kappat, kappa4)

     gamma2 = logpc2 - logpc3
  
     gamma3 = logpc3 - logpc4

     phit = gamma2 * rho2 + gamma3 * rho3

     Nt = len(t)

     Macro = macro.gdp(P0, Q0, A0, K0, Nt, gdpconst)
  
     CO2 = phit * Macro[:,1]

     Output = np.c_[Macro, CO2]

     return Output

#############################################################################

def co2t(Q0, t, gdpconst, coconst):
##
## computing CO2 emmission at the year t by Eq. (9)-(14) in keller07
##
## Inputs: P0 --- initial population
##         Q0 --- initial GWP
##         A0 --- initial total factor productivity
##         K0 --- initial capital stock
##          t --- a specific year
##         gdpconst = [phi1, phi2, phi3, alpha, As, delta, s, lam, pi]
##         coconst = [kappa, rho2, rho3, tau2, tau3, tau4]
##
## Output: Output --- population, GWP and carbon time series
##         Output[:,0] --- population time series
##         Output[:,1] --- GWP time series
##         Output[:,2] --- carbon emission time series
##
    
     kappa = coconst[0]            # technological penetration rate
     rho2 = coconst[1]             # carbon intensity of technology 2
     rho3 = coconst[2]             # carbon intensity of technology 3
     tau2 = coconst[3]             # half saturation time of technology 2
     tau3 = coconst[4]             # half saturation time of technology 3
     tau4 = coconst[5]             # half saturation time of technology 4

     kappat = kappa * t
     kappa2 = kappa * tau2
     kappa3 = kappa * tau3
     kappa4 = kappa * tau4

     logpc2 = logpc(kappat, kappa2)
     logpc3 = logpc(kappat, kappa3)
     logpc4 = logpc(kappat, kappa4)

     gamma2 = logpc2 - logpc3
  
     gamma3 = logpc3 - logpc4

     phit = gamma2 * rho2 + gamma3 * rho3
  
     CO2 = phit * Q0

     return CO2


