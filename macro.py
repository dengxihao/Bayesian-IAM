import numpy as np

def pop(P1, y1, phi1, phi2, phi3):
##
##  population
##

   eco = y1/(y1 + phi2)
   cap = 1 - P1/phi3

   P2 = P1 * (1 + phi1 * eco * cap)

   return P2

######################################################

def tfp(A1, alpha, As):
##
## total factor productivity
## 

   A2 = A1 + alpha * A1 * (1 - A1/As)

   return A2

########################################################

def cs(K1, Q1, delta, s):
## 
## capital stock
##

   K2 = (1 - delta) * K1 + s * Q1

   return K2

##########################################################

def twp(P2, A2, K2, lam, pi):
##
##  total world production
##

   L2 = pi * P2

   Q2 = A2 * (L2**lam)* (K2**(1-lam))

   return Q2
     
############################################################

def gdp(P0, Q0, A0, K0, Nt, gdpconst):
##
##  GDP
##  const = [phi1, phi2, phi3, alpha, As, delta, s, lam, pi]
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
    
      
    Pt = P0
    Qt = Q0
    yt = Q0/P0
    At = A0
    Kt = K0 
    

    Macro = np.zeros((Nt, 2))    
    Macro[0, 0] = P0
    Macro[0, 1] = Q0
  
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
##  GDP
##  const = [phi1, phi2, phi3, alpha, As, delta, s, lam, pi]
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
    
      
    Pt = P0
    Qt = Q0
    yt = Q0/P0
    At = A0
    Kt = K0 
    

    Macro = np.zeros(4)    
 #   Macro[0, 0] = Pt
 #   Macro[0, 1] = Qt
    
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






















