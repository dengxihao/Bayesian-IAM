#!/bin/bash

#############################################
#
# runit.sh		March 3 2015
#
# Script for running bayesian-iam code steps
# provided for convenience
#
# Run this script from the bayesian-iam
# root directory to perform the analysis
# as published in:
# INSERT CITATION HERE
#
#############################################

# Simple error handling function
function error_exit
{
	echo "Script failed. Exiting with error code 1" 1>&2
	exit 1
}

echo " "
echo "------ Running bayesian-iam analysis --------"
echo "This script will run each of the python and R"
echo "scripts in the proper order to reporduce the "
echo "results in the publication. Note that some"
echo "steps may take some time."
echo "---------------------------------------------"

######## python running #####################

echo "Running \"test.py 1\" (Note: This could take awhile)... "
$(python test.py) || error_exit 
echo "Running \"concatenate.py 1\"... "
$(python concatenate.py 1) ||  error_exit 

echo "Running \"priorpro.py 1\"... "
$(python priorpro.py 1) || error_exit 
echo "Running \"priorf.py 1\" (Note: This step could take a few minutes)..."
$(python priorf.py 1) || error_exit 


echo "Running \"interval.py Pop\"... "
$(python interval.py Pop) || error_exit 
echo "Running \"interval.py GDP\"... "
$(python interval.py GDP) || error_exit  
echo "Running \"interval.py CO2\"... "
$(python interval.py CO2) || error_exit 

echo "Running \"projection.py 1 Posterior Pop\"... "
$(python projection.py 1 Posterior Pop) || error_exit  
echo "Running \"projection.py 1 Posterior GDP\"... "
$(python projection.py 1 Posterior GDP) || error_exit 
echo "Running \"projection.py 1 Posterior CO2\"... "
$(python projection.py 1 Posterior CO2) || error_exit 
echo "Running \"projection.py 1 Prior Pop\"... "
$(python projection.py 1 Prior Pop) || error_exit 
echo "Running \"projection.py 1 Prior GDP\"... "
$(python projection.py 1 Prior GDP) || error_exit 
echo "Running \"projection.py 1 Prior CO2\"... "
$(python projection.py 1 Prior CO2) || error_exit 

echo "Running \"bestfit.py\"... "
$(python bestfit.py) || error_exit 

############# R plotting ######################

for i in {1..25}
do
	echo "Running \"dplot.R 1 Posterior $i\"... "
 $(Rscript dplot.R 1 Posterior "$i" > /dev/null) || error_exit 
done

echo "Running \"Mfplot.R\"... "
$(Rscript Mfplot.R > /dev/null) || error_exit 
echo "Running \"Cfplot.R\"... "
$(Rscript Cfplot.R > /dev/null) || error_exit 

echo "Running \"pfplot.R Pop\"... "
$(Rscript pfplot.R Pop > /dev/null) || error_exit 
echo "Running \"pfplot.R GDP\"... "
$(Rscript pfplot.R GDP > /dev/null) || error_exit 
echo "Running \"pfplot.R CO2\"... "
$(Rscript pfplot.R CO2 > /dev/null) || error_exit 

echo "Running \"pplot.R Pop\"... "
$(Rscript pplot.R Pop > /dev/null) || error_exit 
echo "Running \"pplot.R GDP\"... "
$(Rscript pplot.R GDP > /dev/null) || error_exit 
echo "Running \"pplot.R CO2\"... "
$(Rscript pplot.R CO2 > /dev/null) || error_exit 

echo "Running \"NormalTest.R Pop\"... "
$(Rscript NormalTest.R Pop > /dev/null) || error_exit 
echo "Running \"NormalTest.R Pop\"... "
$(Rscript NormalTest.R GDP > /dev/null) || error_exit 
echo "Running \"NormalTest.R Pop\"... "
$(Rscript NormalTest.R CO2 > /dev/null) || error_exit 
