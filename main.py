from beamsolver import io
from beamsolver import plot
import numpy as np
import matplotlib.pyplot as pyp

if __name__ == '__main__':

    #relative file path of the .asw file
    filepath = 'inputfiles/bbeam.asw'

    #read in the wing from the asw file
    wing = io.readwingfromasw(filepath)
    plot.eulerBernoulli(wing)
    plot.plotWing(wing)

    # print all the available spanwise properties (these should match the asw file!)
    #print("\nAvailable Parameters:")
    #print(wing.keys())

    # print the variable EIcc (first column is the spanwise location, second column is the EIcc value)
    #print("\nWing EIcc:")
    #print(wing["EIcc"])
