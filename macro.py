## This module programs all the functions needed to compute
## the population and GWP presented in Keller et al. 2007 (denoted as keller07): 
## (http://papers.ssrn.com/sol3/papers.cfm?abstract_id=981135)

import numpy as np

def pop(P1, y1, phi1, phi2, phi3):
##
## computing population for next year by Eq. (1) in keller07
##
## Inputs: P1 --- current population
##         y1 --- current GWP per capita 
##         phi1 --- population growth rate
##         phi2 --- half-saturation constant
##         phi3 --- population carrying capacity
##         phi4 --- population in 1700
## 
## Output: P2 --- population of next year 
##


   eco = y1/(y1 + phi2)
   cap = 1 - P1/phi3

   P2 = P1 * (1 + phi1 * eco * cap)

   return P2

######################################################

def tfp(A1, alpha, As):
##
## computing total factor productivity for next year by Eq. (5) in keller07
## 
## Inputs: A1 --- current total factor productivity
##         alpha --- growth rate parameter for total factor productivity
##         As --- saturation level of total factor productivity
##
## Output: A2 --- next year total factor productivity
##

   A2 = A1 + alpha * A1 * (1 - A1/As)

   return A2

########################################################

def cs(K1, Q1, delta, s):
## 
## computing capital stock for next year by Eq. (6) in keller07
##
## Inputs: K1 --- current capital stock
##         Q1 --- current GWP
##         delta --- capital depreciation rate
##         s --- savings proportion
##
## Output: K2 --- next year capital stock
##

   K2 = (1 - delta) * K1 + s * Q1

   return K2

##########################################################

def twp(P2, A2, K2, lam, pi):
##
## computing total world production (GWP) for next year by Eq. (2) in keller07
##
## Inputs: P2 --- next year population
##         A2 --- next year total factor productivity
##         K2 --- next year capital stock
##         lam --- elasticity of production with respect to labor
##         pi --- labor participation rate
##
## Output: Q2 --- next year GWP
## 

   L2 = pi * P2

   Q2 = A2 * (L2**lam)* (K2**(1-lam))

   return Q2
     
############################################################

def gdp(P0, Q0, A0, K0, Nt, gdpconst):
##
##  computing population and GWP time series covering Nt years
##
##  Inputs: P0 --- initial population
##          Q0 --- initial GWP
##          A0 --- initial total factor productivity
##          K0 --- initial captial stock
##          Nt --- number of years  
##          gdpconst = [phi1, phi2, phi3, alpha, As, delta, s, lam, pi]
##
##  Output: Macro --- population and GWP time series
##          Macro[:,0] --- population time series
##          Macro[:,1] --- GWP time series
##

    phi1 = gdpconst[0]
    phi2 = gdpconst[1]
    phi3 = gdpconst[2]
    alpha = gdpconst[3]
    As = gdpconst[4]
    delta = gdpconst[5]
    s = gdpconst[6]
    lam = gdpconst[7]
    pi = gdpconst[8]
    
 # initialization     
    Pt = P0
    Qt = Q0
    yt = Q0/P0
    At = A0
    Kt = K0 
    
# pre-allocation
    Macro = np.zeros((Nt, 2))    
    Macro[0, 0] = P0
    Macro[0, 1] = Q0

 # loop for computing the time series  
    for i in xrange(Nt-1):
      At = tfp(At, alpha, As)
      Kt = cs(Kt, Qt, delta, s)  
      Pt = pop(Pt, yt, phi1, phi2, phi3)
      Qt = twp(Pt, At, Kt, lam, pi)
      Macro[i+1, 0] = Pt
      Macro[i+1, 1] = Qt
      yt = Qt/Pt
      
    return Macro


def gdpt(P0, Q0, A0, K0, t0, t, gdpconst):
##
##  computing population and GWP at the year t
##
##  Inputs: P0 --- initial population
##          Q0 --- initial GWP
##          A0 --- initial total factor productivity
##          K0 --- initial captial stock
##          Nt --- number of years  
##          gdpconst = [phi1, phi2, phi3, alpha, As, delta, s, lam, pi]
##
##  Output: Macro --- popluation and GWP at the year t
##          Macro[0] --- population at the year t
##          Macro[1] --- GWP at the year t
##          Macro[2] --- total factor productivity at the year t
##          Macro[3] --- capital stock at the year t
##

    phi1 = gdpconst[0]
    phi2 = gdpconst[1]
    phi3 = gdpconst[2]
    alpha = gdpconst[3]
    As = gdpconst[4]
    delta = gdpconst[5]
    s = gdpconst[6]
    lam = gdpconst[7]
    pi = gdpconst[8]
    
# initialization      
    Pt = P0
    Qt = Q0
    yt = Q0/P0
    At = A0
    Kt = K0 
    
# pre-allocation
    Macro = np.zeros(4)    

#     
    for i in xrange(t-t0):
      At = tfp(At, alpha, As)
      Kt = cs(Kt, Qt, delta, s)  
      Pt = pop(Pt, yt, phi1, phi2, phi3)
      Qt = twp(Pt, At, Kt, lam, pi)
      yt = Qt/Pt
    
    Macro[0] = Pt
    Macro[1] = Qt    
    Macro[2] = At
    Macro[3] = Kt
  
    return Macro















