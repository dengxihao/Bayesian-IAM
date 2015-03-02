#!/bin/bash

######## python running #####################

python test.py
python concatenate.py 1 

python priorpro.py 1
python priorf.py 1

python interval.py Pop
python interval.py GDP 
python interval.py CO2

python projection.py 1 Posterior Pop 
python projection.py 1 Posterior GDP
python projection.py 1 Posterior CO2
python projection.py 1 Prior Pop
python projection.py 1 Prior GDP
python projection.py 1 Prior CO2

python bestfit.py

############# R plotting ######################

for i in {1..25}
do
  Rscript dplot.R 1 Posterior "$i"
done

Rscript Mfplot.R        
Rscript Cfplot.R

Rscript pfplot.R Pop
Rscript pfplot.R GDP
Rscript pfplot.R CO2

Rscript pplot.R Pop
Rscript pplot.R GDP
Rscript pplot.R CO2

Rscript NormalTest.R Pop
Rscript NormalTest.R GDP
Rscript NormalTest.R CO2
