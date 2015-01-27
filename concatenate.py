import numpy as np
import sys

def concatenate():
##
## main function to concatenate the 10-chain samples and forecasts into one
##
     folder = sys.argv[1]

     directory =  'Result' + folder + '/' + 'Posterior/'

     samps = np.load('temp/samp1.npy')  
     fPop = np.load('temp/fPops1.npy')
     fGDP = np.load('temp/fGDPs1.npy')
     fCO2 = np.load('temp/fCO2s1.npy')     

     for i in range(1,10):
       sampsi = np.load('temp/samp' + str(i+1) + '.npy')
       fPopi = np.load('temp/fPops'+str(i+1)+'.npy')
       fGDPi = np.load('temp/fGDPs'+str(i+1)+'.npy')
       fCO2i = np.load('temp/fCO2s'+str(i+1)+'.npy')
       
       samps = np.concatenate((samps, sampsi))
       fPop = np.concatenate((fPop, fPopi))
       fGDP = np.concatenate((fGDP, fGDPi))
       fCO2 = np.concatenate((fCO2, fCO2i))
        
     np.savetxt(directory + 'samps.dat', samps)
     np.save(directory + 'fPop', fPop)
     np.save(directory + 'fGDP', fGDP)
     np.save(directory + 'fCO2', fCO2)

if __name__ == '__main__':
    concatenate()

