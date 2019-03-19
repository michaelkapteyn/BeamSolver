import numpy as np
import matplotlib.pyplot as plt


def plotWing(wing):

    print("\n\nAttempting to plot the wing specified in the ASW file:")

    try:
        #Find the maximum value of the x-axis
        xUpBound = wing["Xax"][0,0]
        xLowBound = wing["Xax"][0,1]
        length = len(wing["Xax"][:,0])
        for i in wing["Xax"][:,0]:
            if i > xUpBound:
                xUpBound = i
            if i < xLowBound:
                xLowBound = i

        #Give additional Margins
        magnitude = xUpBound - xLowBound
        xLowBound = xLowBound - (magnitude)/8
        xUpBound = xUpBound + (magnitude)/8

        #Plot the Wing
        x = wing["Xax"][:,0]*10
        y = wing["Xax"][:,1]
        plt.figure(0)
        plt.plot(x, y)
        plt.plot(x,y - wing["chord"][:,1])
        plt.axis([xLowBound,xUpBound, -magnitude, magnitude])
        plt.axis('equal')
        plt.xlabel('Distance')
        plt.ylabel('Xax')
        plt.title("Aircraft Wing")
        plt.show()
    except TypeError:
        print("\nThis function requires the Xax and chord keys to function."
        "Please check that they are present in the asw file if you want to plot the wing planform.")
    return None


def eulerBernoulli(wing):

    print("\n\nAttempting to calculate and plot deflection of the wing:")

    try:
        #Takes the load on the right-most tip of the beam
        q = -1*wing["mg"][len(wing["mg"][:,0])-1,1]

        #Finds the spanwise coordinate of the tip of the beam
        yEnd = wing["y"][len(wing["y"][:,0])-1,1]

        #Assume EIcc is Constant
        EIcc = wing["EIcc"][0,1]

        #For a Cantilever Euler-Bernoulli Beam Theory 1-D Beam
        #the solution for a point load at the end of the beam is:
        #delta = (q*x^2)/(6*EIcc)*(3L-x)

        t = np.arange(0, wing["y"][len(wing["y"][:,0])-1,1], 0.01)
        plt.figure(1)

        #Find the max deflection (the tip deflection for a point load at the tip) and print it
        maxDeflec = ((q*yEnd*yEnd)/(6*EIcc))*(3*yEnd - yEnd)
        print("\nThe deflection at the tip of the beam is: ", maxDeflec)

        plt.xlabel('X Position [m]')
        plt.ylabel('Deflection [m]')
        plt.title("Beam Deflection")
        #plots the curve of deflection and creates a horizontal line that marks the maximum deflection
        plt.plot(t, ((q*t*t)/(6*EIcc))*(3*yEnd - t), 'r--', label = 'Deflection')
        plt.axhline(y=maxDeflec, color='y', linestyle='--', label = 'Value of Max Deflection')
        plt.legend(loc='upper right', shadow=False, fontsize='x-large')
        plt.axis('equal')
        plt.show()

    except TypeError:
        print("\nThis function requires the mg, y, and EIcc keys to function."
        "Please check that they are present in the asw file if you want to plot the wing planform.")
