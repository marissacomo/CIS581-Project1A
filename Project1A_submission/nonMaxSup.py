'''
  File name: nonMaxSup.py
  Author:
  Date created:
'''

'''
  File clarification:
    Find local maximum edge pixel using NMS along the line of the gradient
    - Input Mag: H x W matrix represents the magnitude of derivatives
    - Input Ori: H x W matrix represents the orientation of derivatives
    - Output M: H x W binary matrix represents the edge map after non-maximum suppression
'''
#!/usr/local/bin/python3
import utils
import numpy as np

def nonMaxSup(Mag, Ori):
# 1) make a mesh grid of all pixel locations
  nr = Mag.shape[0];
  nc = Mag.shape[1];
  X, Y = np.meshgrid(np.arange(nc), np.arange(nr))

# 2) use the orientation to compute the offset forward and back for each pixel
  delta_xb = np.cos(Ori + np.pi) # delta back x-pixel
  delta_xf = np.cos(Ori) # delta forward x-pixel
  delta_yb = np.sin(Ori + np.pi) # delta backward y-pixel
  delta_yf = np.sin(Ori) # delta forward y-pixel

# 3) make a comparison pixel locations for forward and back for all pixel locations
  xf = delta_xf + X
  xb = delta_xb + X
  yf = delta_yf + Y
  yb = delta_yb + Y

# 4) interpolate the comparison grid to get values for forward and back
  Magb = utils.interp2(Mag, xb,  yb)
  Magf = utils.interp2(Mag, xf, yf)

# 5) compare each direction
  mask = np.logical_and(Mag > Magb, Mag > Magf)

#  from IPython.core.debugger import Pdb
#  Pdb().set_trace()
  
  return mask 
 

