import numpy as np
#from Likelihood import Model
#from Input import t, t0, ind
import emit
import macro


def Model(t, t0, ind, par):
##
## log likelihood of population and GDP
##

 gdpconst = par[0:9] 
 coconst = par[9:15]
 P0 = par[15]
 A0 = par[16]
 delta = gdpconst[5]
 s = gdpconst[6]
 lam = gdpconst[7]
 pi = gdpconst[8]
 L0 = pi * P0
 K0 = (s * A0/delta)**(1/lam) * L0
 Q0 = A0 * (L0**lam) * (K0**(1-lam))

 CO20 = emit.co2t(Q0, t0, gdpconst, coconst)

 t1 = t[0]

 Macro1 = macro.gdpt(P0, Q0, A0, K0, t0, t1, gdpconst)

 P1 = Macro1[0]
 Q1 = Macro1[1]
 A1 = Macro1[2]
 K1 = Macro1[3]
 
 Output = emit.co2(P1, Q1, A1, K1, t, gdpconst, coconst)

 Pop = np.append(P0, Output[ind, 0])
 GDP = np.append(Q0, Output[ind, 1])
 CO2 = np.append(CO20, Output[:,2])

 if not(np.prod(np.greater(Pop, 0))) or not(np.prod(np.greater(GDP, 0))) or not(np.prod(np.greater(CO2, 0))):
   Pop = 10.0**(-10) * np.ones(len(ind)+1)
   GDP = 10.0**(-10) * np.ones(len(ind)+1)
   CO2 = 10.0**(-10) * np.ones(len(t)+1)

 return (Pop, GDP, CO2)


###############################################################################

def arf1(X0, parr):
##
## forecast next-step of AR model
## 

  X1 = parr[0] * X0 + parr[1] * np.random.randn()

  return X1

###############################################################################  

def arf(X0, T, parr):
##
## forecast T steps of AR model
##
  X = X0 * np.ones(T)
  
  for i in range(1, T):
    X[i] = arf1(X[i-1], parr)

  return X
    
 

###############################################################################

def project(t, t0, ind, par):
##
## forecast Pop, GDP and CO2 
##
  parrP = [par[17], par[20]]
  parrG = [par[18], par[21]]
  parrC = [par[19], par[22]]

  TP = len(ind)
  TC = len(t) 

  Pop, GDP, CO2 = Model(t, t0, ind, par)

  epsilon = 10.0**(-9)

  stdSPop = par[20]/((1+epsilon-par[17]**2)**(0.5))
  SPop0 = stdSPop * np.random.randn()

  stdSGDP = par[21]/((1+epsilon-par[18]**2)**(0.5))
  SGDP0 = stdSGDP * np.random.randn()

  stdSCO2 = par[22]/((1+epsilon-par[19]**2)**(0.5))
  SCO20 = stdSCO2 * np.random.randn(2)

  SPop = arf(SPop0, TP-5, parrP)
  SGDP = arf(SGDP0, TP-5, parrG)
  SCO2 = arf(SCO20[1], TC, parrC)

  WPop = par[23] * np.random.randn(6)
  WGDP = par[24] * np.random.randn(6)
  WCO2 = stdSCO2 * np.random.randn()

  SCO2 = np.append(WCO2, SCO2)

  fPop = np.concatenate((Pop[0:6]+WPop, Pop[6:(TP+1)]*np.exp(SPop)))
  fGDP = np.concatenate((GDP[0:6]+WGDP, GDP[6:(TP+1)]*np.exp(SGDP)))
  fCO2 = CO2 * np.exp(SCO2)

  return (fPop, fGDP, fCO2, Pop, GDP, CO2)



  
