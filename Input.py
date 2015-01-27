# This module load all the inputs of data, initial parameters, parameter bounds, etc.

import numpy as np

macro0 = np.loadtxt("macro.txt")    # observations of population and GWP
co20 = np.loadtxt("co2.txt")        # observations of carbon emission
    
Nm0 = len(macro0[:,0])        # length of population observations          
NC0 = len(co20[:,0])          # length of carbon emission observations
tm = macro0[1:Nm0,0]          # observation times of population after 1700
tm = tm.astype(int)
t = co20[:,0]                 # observation times of carbon emission
t = t.astype(int)
t0 = macro0[0,0]              # initial observation time of population
t0 = t0.astype(int)

# hindcast and forecast time range of population and GWP
tM = np.concatenate((tm, np.array(range(tm[Nm0-2]+1, 2151))))

# hindcast and forecast time range of carbon emission
t1 = np.array(range(t[0], 2151))
 
dPop = macro0[:, 1]               # observations of population
dGDP = macro0[:, 2]               # observations of GWP
dCO2 = co20[:,1]                  # observations of carbon emission

# the indices of population observation times in carbon emission observation time vector
ind = np.searchsorted(t1, tM)

# parameter bounds   
parb = np.array([[0.0001, 0.15], \
                     [1.0, 100.0], \
                     [6.9, 14.4], \
                     [0.0007, 0.0212], \
                     [5.3, 16.11], \
                     [0.01, 0.14], \
                     [0.18, 0.26], \
                     [0.6, 0.8], \
                     [0.51, 0.67], \
                     [0.005, 0.2], \
                     [0, 0.5], \
                     [0, 0.5], \
                     [1700, 2100], \
                     [1700, 2100], \
                     [2010, 2300], \
                     [0.3, 0.9],  \
                     [0.0, 3.0], \
                     [0.85, 1.0], \
                     [0.85, 1.0], \
                     [0.85, 1.0], \
                     [0.00001, 0.006], \
                     [0.00001, 0.05], \
                     [0.00001, 0.1], \
                     [0.00001, 0.6], \
                     [0.00001, 2.0]]) 

# random step sizes in mcmc samples
kappa = 0.0000025*np.array([100] + \
                     [1000] + \
                     [2000] + \
                     [1] + \
                     [3000] +    \
                     [100] +    \
                     [500] +    \
                     [40] +    \
                     [500] +     \
                     [50] +     \
                     [100]+     \
                     [1000] +     \
                     [10**5] +    \
                     [10**5] +      \
                     [1.0*(10**7)] +      \
                     [10] +      \
                     [20] +  \
                     [30] + \
                     [30] + \
                     [50] + \
                     [2] + \
                     [10] + \
                     [2] + \
                     [50] + \
                     [50]) 

