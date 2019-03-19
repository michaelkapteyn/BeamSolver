# import the geometry module from aswing.py
import sys
sys.path.append("C:\\Users\\wybot\\Desktop\\Git\\Aswing.py")
print(sys.path)
from aswingpy import geometry


def readwingfromasw(filepath):
    #create a new aswing geometry
    aswgeom = geometry.aswGeometry()

    #read the aswing file
    aswgeom.readaswfile(filepath)
    wing = aswgeom.beams["Wing"].spanwise
    return wing
