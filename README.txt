This is a README file for the package Bayesian-IAM

*.py are python modules and *.R are R modules.

--- Requirements:

 * install joblib for python parallel computing from here: 
             https://pythonhosted.org/joblib/installing.html

 * install the following R packages into the directory /R_packages:
   (1) grid (2) methods (3) spam (4) maps (5) fields
    

##########################################################################################

Steps to run the Python commands in terminal:

1. run 10 mcmc chains and concatenate all the chains:
  
    python test.py 
    python concatenate.py 1 

2. generate prior forecast:

    python priorpro.py 1
    python priorf.py 1

3. compute percentiles of posterior hindcasts & forecasts:

    python interval.py Pop(or GDP or CO2)

4. generate samples of projections for Pop, GWP and CO2 at the year 2050, 2100 and 2150:

    python projection.py 1 Posterior(or Prior) Pop(or GDP or CO2) 

5. generate bestfit model:
  
    python bestfit.py


#######################################################################################

Steps to run R commands in terminal for plotting by:

1. plot density estimation of marginal pdf of parameters:

    Rscript dplot.R 1 Posterior j     # j denotes the jth parameter

2. plot hindcasts and forecasts 

    Rscript Mfplot.R        # Population and GWP 
    Rscript Cfplot.R        # Carbon emission

3. plot density estimation of marginal pdf of Pop, GWP and CO2 at 2050, 2100 and 2150

    Rscript pfplot.R Pop(or GDP or CO2)

4. plot the comparison of maginal pdf of Pop, GWP and CO2 at 2050

    Rscript pplot.R Pop(or GDP or CO2)

5. plot the observations, bestfit model and residuals

    Rscript NormalTest.R Pop(or GDP or CO2)


####################################################################################

List of modules:

-- modules of the long trend model:

 * macro.py: compute the population and GWP

 * emit.py: compute the carbon emission


--- modules of Bayesian statistics:
 
 * forcast.py:  compute the hindcast and forecast of the three components

 * Likelihood.py: compute the log likelihood function

 * Prior.py: compute the prior and posterior distributions 

 * mcmc.py: compute the mcmc sampling


--- modules generating results:

 * Input.py: input data and initial parameters

 * bestfit.py: compute the best-fit model

 * test.py: parallel sampling 10 mcmc chains 
 
 * concatenate.py: concatenate 10 mcmc chains

 * priorpro.py: random generate 50,000 parameter samples from prior distribution
 
 * priorf.py: generate the prior forecasts 

 * percentile.py: a general function to compute percentiles

 * interval.py: compute the percentiles of hindcasts and forecasts

 * projection.py: samples of prosterior predictive distributions for 2050, 2100, 2150 


--- R modules generating figures:
 
 * Input.R: input data initial parameters in R module
