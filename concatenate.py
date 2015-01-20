import numpy as np
import sys

def concatenate():

     folder = sys.argv[1]

     directory =  folder + '/' + 'Posterior/'

     samps = np.load('temp/samps1.npy')  
     fPop = np.load('temp/fPop1.npy')
     fGDP = np.load('temp/fGDP1.npy')
     fCO2 = np.load('temp/fCO21.npy')     

     for i in range(1,10):
       sampsi = np.load('temp/samps' + str(i+1) + '.npy')
       fPopi = np.load('temp/fPop'+str(i+1)+'.npy')
       fGDPi = np.load('temp/fGDP'+str(i+1)+'.npy')
       fCO2i = np.load('temp/fCO2'+str(i+1)+'.npy')
       
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

