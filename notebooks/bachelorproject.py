import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from matplotlib import colors, cm

CONST_AH = 1.008
CONST_AHe = 4.004
CONST_AZ = 30.0
CONST_amu = 1.66053886e-24
CONST_au  = 1.49597892e13
CONST_c = 2.99792458e10
CONST_eV = 1.602176463158e-12
CONST_G = 6.6726e-8
CONST_h = 6.62606876e-27
CONST_kB = 1.3806505e-16
CONST_ly = 0.9461e18
CONST_mp = 1.67262171e-24
CONST_mn = 1.67492728e-24
CONST_me = 9.1093826e-28
CONST_mH = 1.6733e-24
CONST_Msun = 2.e33
CONST_Mearth = 5.9736e27
CONST_NA = 6.0221467e23
CONST_pc = 3.0856775807e18
CONST_Rearth = 6.378136e8
CONST_Rsun = 6.96e10
CONST_sigma = 5.67051e-5
CONST_sigmaT = 6.6524e-25

def plot(ax, im, frame, L0 = 14959789200000.0, code_units = False, *args, norm = None, cmap = cm.plasma, x_min = 0, x_max = -1, y_min = 0, y_max = -1):
    if(x_max == -1):
        x_max = len(frame.x1)
    if(y_max == -1):
        y_max = len(frame.x2)
    im = im[x_min:x_max, y_min:y_max]
    frame.x1 = frame.x1[x_min:x_max]
    frame.x2 = frame.x2[y_min:y_max]
    frame.dx1 = frame.dx1[x_min:x_max]
    frame.dx2 = frame.dx2[y_min:y_max]
    X_max = frame.x1[-1] + frame.dx1[-1]/2
    X_min = frame.x1[0] -frame.dx1[0]/2
    Y_max = frame.x2[-1] + frame.dx2[-1]/2
    Y_min = frame.x2[0] -frame.dx2[0]/2
    extent = (X_min, X_max, Y_min, Y_max)
    if (not code_units):
        extent = L0*np.array(extent)
    im = np.rot90(im, k = 1, axes = (0,1))
    if norm:
        image = ax.imshow(im, extent = extent, cmap = cmap, norm = norm)
    else:
        image = ax.imshow(im, extent = extent, cmap = cmap)
    return image

class units(object):
    def __init__(self, UNIT_DENSITY = CONST_mp, UNIT_LENGTH = CONST_au, UNIT_VELOCITY = 1.e5):
        self.UNIT_DENSITY = UNIT_DENSITY
        self.UNIT_LENGTH = UNIT_LENGTH
        self.UNIT_VELOCITY = UNIT_VELOCITY
        self.UNIT_TIME = UNIT_LENGTH/UNIT_VELOCITY 
        self.UNIT_FIELD = 2*UNIT_VELOCITY*np.sqrt(np.pi * UNIT_DENSITY)
        self.UNIT_PRESSURE = UNIT_DENSITY*UNIT_LENGTH*UNIT_LENGTH

