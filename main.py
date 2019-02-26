from beamsolver import io
import numpy as np

if __name__ == '__main__':

    #relative file path of the .asw file
    filepath = 'inputfiles/test_aircraft.asw'

    #read in the wing from the asw file
    wing = io.readwingfromasw(filepath)

    # print all the available spanwise properties (these should match the asw file!)
    print("\nAvailable Parameters:")
    print(wing.keys())

    # print the variable EIcc (first column is the spanwise location, second column is the EIcc value)
    print("\nWing EIcc:")
    print(wing["EIcc"])
