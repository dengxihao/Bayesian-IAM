import numpy as np
import emit
import macro


def Model(t, t0, ind, par):
##
## generate long trend model for population, GWP and carbon emission 
## at the observation time vector t.
## population and GWP observed from 1700 to 2010, with only 6 sparse 
## data points before 
##
## Inputs: t --- observation time vector
##         t0 --- initial time for population and GWP observations
##         ind --- the indices of population observation times in carbon
##                 emission observation time vector
##         par --- parameter set described in macro.py and emit.py
##
## Output: Pop --- population time series
##         GDP --- GWP time series
##         CO2 --- carbon emission time series
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
 K0 = (s * A0/delta)**(1/lam) * L0      # initial condition for capital stock
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

# set the limits that population, GWP and carbon emission should all be positive
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
## Inputs: X0 --- initial step of an AR process
##         parr --- AR parameters
##         parr[0] --- AR coefficient
##         parr[1] --- standard deviation of AR error
##
## Output: X1 --- next step of the AR process
##

  X1 = parr[0] * X0 + parr[1] * np.random.randn()

  return X1

###############################################################################  

def arf(X0, T, parr):
##
## forecast T steps of AR model
##
## Inputs: X0 --- initial step of an AR process
##          T --- time steps of AR process 
##          parr --- AR parameters
##
## Output: X --- T steps forecast of the AR process 
##
  X = X0 * np.ones(T)
  
  for i in range(1, T):
    X[i] = arf1(X[i-1], parr)

  return X
    
 

###############################################################################

def project(t, t0, ind, par):
##
## forecast total population, GWP and carbon emission by 
## adding the long trend model and the AR short run fluctuations
##
## Inputs: t --- the observation time vector of carbon emission
##         t0 --- initial observational time of population
##         ind --- the indices of population observation times in carbon
##                 emission observation time vector
##         par --- parameter set described in macro.py, emit.py and 
##                 AR parameters
##
## Output: fPop --- population forecast
##         fGDP --- GWP forecast
##         fCO2 --- carbon emission forecast
##          Pop --- long trend population
##          GDP --- long trend GWP
##          CO2 --- long trend carbon emission
##

  parrP = [par[17], par[20]]      # AR parameters for population
  parrG = [par[18], par[21]]      # AR parameters for GWP
  parrC = [par[19], par[22]]      # AR parameters for carbon emission

  TP = len(ind)
  TC = len(t) 

  # long trend model forecasts
  Pop, GDP, CO2 = Model(t, t0, ind, par)

  epsilon = 10.0**(-9)

  # generate initial state of AR residuals of the population
  stdSPop = par[20]/((1+epsilon-par[17]**2)**(0.5))    # standard deviation of AR 
  SPop0 = stdSPop * np.random.randn()

  # generate initial state of AR residuals of the GWP
  stdSGDP = par[21]/((1+epsilon-par[18]**2)**(0.5))    # standard deviation of AR
  SGDP0 = stdSGDP * np.random.randn()

  # generate initial state of AR residuals of the carbon emission
  stdSCO2 = par[22]/((1+epsilon-par[19]**2)**(0.5))    # standard deviation of AR
  SCO20 = stdSCO2 * np.random.randn(2)

  # forecast AR steps
  SPop = arf(SPop0, TP-5, parrP)
  SGDP = arf(SGDP0, TP-5, parrG)
  SCO2 = arf(SCO20[1], TC, parrC)

  # generate white Gaussian steps for the sparse data
  WPop = par[23] * np.random.randn(6)
  WGDP = par[24] * np.random.randn(6)
  WCO2 = stdSCO2 * np.random.randn()

  SCO2 = np.append(WCO2, SCO2)

  # combine long trend model and AR residual forecasts
  fPop = np.concatenate((Pop[0:6]+WPop, Pop[6:(TP+1)]*np.exp(SPop)))
  fGDP = np.concatenate((GDP[0:6]+WGDP, GDP[6:(TP+1)]*np.exp(SGDP)))
  fCO2 = CO2 * np.exp(SCO2)

  return (fPop, fGDP, fCO2, Pop, GDP, CO2)



  
