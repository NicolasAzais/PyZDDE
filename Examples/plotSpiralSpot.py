#-------------------------------------------------------------------------------
# Name:        plotSpiralSpot.py
# Purpose:     Example of using the "spiral spot" member function of pyZDDE.
#              Please note that this code uses matplotlib plotting library from
#              http://matplotlib.org/ for 2D-plotting
#
# Author:      Indranil Sinharoy
#
# Created:     06/10/2012
# Copyright:   (c) 2012, 2013
# Licence:     MIT License
#-------------------------------------------------------------------------------

import sys, os
import matplotlib.pyplot as plt

cd = os.getcwd()
ind = cd.find('Examples')
cd = cd[0:ind-1]

if cd not in sys.path:
    sys.path.append(cd)

from pyZDDE import *

# The ZEMAX file path
zmxfp = cd+'\\ZMXFILES\\'
zmxfile = 'Cooke 40 degree field.zmx'
filename = zmxfp+zmxfile

# Create a pyzdde object
link0 = pyzdde()

# Initiate the DDE link
status = link0.zDDEInit()
if ~status:
    # Load a lens file into the ZEMAX DDE server
    ret = link0.zLoadFile(filename)
    if ~ret:
        status = link0.zPushLensPermission()
        if status:
            ret = link0.zPushLens(updateFlag=1)
            if ~ret:
                [x,y] = link0.spiralSpot(0.4,0,1,10,10000)
                plt.plot(x,y)
                #plt.ion()
                plt.title('Spiral Spot')
                plt.show()

            else:
                print "Failed to push lens"
        else:
            print "Extension not allowed to push lens. Enable push permission."
    else:
        print "Could not load lens file"
    # close the DDE channel
    link0.zDDEClose()

else:
    print "DDE link could not be established"


