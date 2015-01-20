import numpy as np
import macro

def logpc(kappat, kappatau):
##
## logistic penetration curve
##
   
     logit = 1/(1 + np.exp(-kappat + kappatau))

     return logit

###################################################################

def co2(P0, Q0, A0, K0, t, gdpconst, coconst):
##
##  CO2 emmission
##
    
     kappa = coconst[0]
     rho2 = coconst[1]
     rho3 = coconst[2]
     tau2 = coconst[3]
     tau3 = coconst[4]
     tau4 = coconst[5]

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
##  CO2 emmission
##
    
     kappa = coconst[0]
     rho2 = coconst[1]
     rho3 = coconst[2]
     tau2 = coconst[3]
     tau3 = coconst[4]
     tau4 = coconst[5]

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

#     Nt = len(t)
  
     CO2 = phit * Q0

 #    Output = np.c_[Macro, CO2]

     return CO2

